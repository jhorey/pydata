import csv
import sys
from bokeh.sampledata import us_counties, unemployment
from bokeh.plotting import *
from cassandra import AlreadyExists
from cassandra.cluster import Cluster, NoHostAvailable

# The county code is a tuple (state ID, county ID). 
# The "patches" graph is an array of arrays. Each element is a set of
# lat/lon points that represents a polygon. 
# Then for each element, we assign a color to that polygon.

colors = ['#993355',
          '#3333FF',
          '#3399FF',
          '#33FFFF',
          '#33FF99',
          '#33FF33',
          '#99FF33',
          '#FFFF33',
          '#FF9933',
          '#FF3333']

def _connect_to_cassandra():
    """
    Connect to the Cassandra cluster and return the session.
    """

    if 'BACKEND_STORAGE_IP' in os.environ:
        host = os.environ['BACKEND_STORAGE_IP']
    else:
        host = 'localhost'

    try:
        cluster = Cluster([host])
        session = cluster.connect()
    except NoHostAvailable as e:
        print e
        return None

    print "ok"
    return session

def _create_tables(session):
    try:
        query = """
                CREATE KEYSPACE census
                WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
                """
        session.execute(query)
    except AlreadyExists:
        pass

    session.set_keyspace("census")
    try:
        query = """
                CREATE TABLE acs_economic_data  (
                    state_cd TEXT,
                    state_name TEXT,
                    county_cd TEXT,
                    county_name TEXT,
                    median INT,
                    mean INT,
                    capita INT,
                    PRIMARY KEY(state_name, county_name)
            )
            """
        session.execute(query)
    except AlreadyExists:
        pass

def _upload(session, data_file):
    session.set_keyspace("census")
    
    f = open(data_file, 'r')
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        median, mean, capita, state, state_cd, county, county_cd = row
    
        query = """
                INSERT INTO acs_economic_data
                (state_cd, state_name, county_cd, county_name, median, mean, capita)
                VALUES (%(state_cd)s, %(state_name)s, 
                        %(county_cd)s, %(county_name)s,
                        %(median)s, %(mean)s, %(capita)s) 
               """

        values = { 'state_cd' : str(state_cd),
                   'state_name' : str(state),
                   'county_cd' : str(county_cd),
                   'county_name' : str(county),
                   'median' : int(median),
                   'mean' : int(mean),
                   'capita' : int(capita) }
        session.execute(query, values)

def _get_econ_data(state, state_abbr):
    session.set_keyspace("census")
    query = """SELECT * FROM acs_economic_data
               WHERE state_name=%(state)s
            """
    values = { 'state': state }
    rows = session.execute(query, values)

    highest_median = -1
    median_econ_data = {}
    for row in rows:
        median_econ_data[(int(row.state_cd), int(row.county_cd))] = row.median
        if row.median > highest_median:
            highest_median = row.median

    county_xs=[
        us_counties.data[code]['lons'] for code in us_counties.data
        if us_counties.data[code]['state'] == state_abbr
    ]
    county_ys=[
        us_counties.data[code]['lats'] for code in us_counties.data
        if us_counties.data[code]['state'] == state_abbr
    ]

    return county_xs, county_ys, median_econ_data, highest_median

def _color_econ_data(state_abbr, county_xs, county_ys, median_econ_data, highest_median):
    county_colors = []
    for county_id in us_counties.data:
        if us_counties.data[county_id]['state'] != state_abbr:
            continue

        try:
            rate = float(median_econ_data[county_id]) / float(highest_median)
            idx = min(int(10 * rate), 9)
            county_colors.append(colors[idx])
        except KeyError:
            county_colors.append("black")

    return county_colors

def _output_econ_data(county_xs, county_ys, county_colors, width=500, height=200):
    patches(county_xs, county_ys, fill_color=county_colors, fill_alpha=0.7,
            line_color="white", line_width=0.5, plot_height=height, plot_width=width, title="Median Income")
    grid().grid_line_color = None
    axis().axis_line_color = None
    axis().major_tick_line_color = None
    show()

session = _connect_to_cassandra()
if sys.argv[1] == "create":
    _create_tables(session)
elif sys.argv[1] == "upload":
    _upload(session, sys.argv[2])
else:
    state_name = sys.argv[2]
    state_abbr = sys.argv[3]
    template_dir = sys.argv[4]

    output_file(template_dir + '/' + state_name + '.html')

    county_xs, county_ys, econ_data, highest_median = _get_econ_data(state_name, state_abbr)
    county_colors = _color_econ_data(state_abbr, county_xs, county_ys, econ_data, highest_median)
    _output_econ_data(county_xs, county_ys, county_colors, 500, 250)

session.shutdown()
