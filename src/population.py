from collections import OrderedDict
import geography
import get
import json
import os
from prettytable import PrettyTable
import requests
import sys
from requests.exceptions import ConnectionError

class Population(object):
    def __init__(self, input_dir, output_file):
        self.key = 'dd53d44d5549b30b1a2537fdc1d0ad5b6a19030c'
        self.api_url = 'http://api.census.gov/data'
        self.population = 'sf1'
        self.economic = 'acs5/profile'
        self.geo = geography.Geography()
        self.geo.load_state_codes(os.path.join(input_dir, "state_codes"))
        self.geo.load_county_codes(os.path.join(input_dir,"county_codes"))
        self.geo.load_zip_codes(os.path.join(input_dir,"zip_codes"))
        self.output_file = output_file

    def _create_params(self, params):
        args = ''
        for i, p in enumerate(params.keys()):
            if isinstance(params[p], list):
                args += "%s=%s" % (p, ','.join(params[p]))
            else:
                args += "%s=%s" % (p, params[p])
            if i < len(params) - 1:
                args += "&"
        return args

    def _pretty_row(self, column_names, row_data, replace = {}):
        row = [0] * len(column_names)
        for k in row_data.keys():
            if row_data[k] in replace:
                data = replace[row_data[k]]
            else:
                data = row_data[k]

            if k == 'state':
                state_name = self.geo.codes[k][data]
                row[column_names.index(k)] = state_name
                row[column_names.index('state_cd')] = data
            elif k == 'county':
                county_name = self.geo.codes[k][state_name][data]
                row[column_names.index(k)] = county_name
                row[column_names.index('county_cd')] = data
            else:
                row[column_names.index(k)] = data
        return row

    def pretty_print(self, data, header, replace = {}):
        for i, d in enumerate(data):
            if i == 0:
                data_key = header[0]
                column_names = []
                for h in header:
                    if h == 'state':
                        column_names.append('state')
                        column_names.append('state_cd')
                    elif h == 'county':
                        column_names.append('county')
                        column_names.append('county_cd')
                    else:
                        column_names.append(h)
                table = PrettyTable(column_names)
            elif i > 0:
                row_data = OrderedDict()
                for j, e in enumerate(d):
                    if header[j] == 'county':
                        cd = str(int(e))
                        row_data[header[j]] = cd
                    else:
                        row_data[header[j]] = e
                row = self._pretty_row(column_names, row_data, replace)
                table.add_row(row)
        print table.get_string(sortby=data_key)

    def raw_print(self, data, header, print_header=False, replace = {}):
        f = open(self.output_file, 'w')
        for i, d in enumerate(data):
            if i == 0:
                data_key = header[0]
                column_names = []
                for h in header:
                    if h == 'state':
                        column_names.append('state')
                        column_names.append('state_cd')
                    elif h == 'county':
                        column_names.append('county')
                        column_names.append('county_cd')
                    else:
                        column_names.append(h)
                if print_header:
                    o = '|'.join(column_names) + '\n'
                    f.write(o)
            elif i > 0:
                row_data = OrderedDict()
                for j, e in enumerate(d):
                    if header[j] == 'county':
                        cd = str(int(e))
                        row_data[header[j]] = cd
                    else:
                        row_data[header[j]] = e
                row = self._pretty_row(column_names, row_data, replace)
                o = '|'.join(row) + '\n'
                f.write(o)
        f.close()

    def query(self, repo, filters):
        url = self.api_url + '/' + str(repo['year']) + '/' + repo['source']

        payload = { 'get': repo['data'],
                    'key' : self.key }

        if len(filters.keys()) == 1 and 'state' in filters:
                payload['for'] = self.geo.area['state'] + ':' +self.geo.data['state'][filters['state']]
        else:
            for f in filters.keys():
                if f == "state":
                    if filters[f] == '*':
                        loc = '*'
                    else:
                        loc = self.geo.data[f][filters[f]]
                    payload['in'] = self.geo.area['state'] + ':' + loc
                else:
                    if filters[f] == '*':
                        loc = '*'
                    else:
                        loc = self.geo.data[f][filters[f]]
                    payload['for'] = self.geo.area[f] + ':' + loc

        full = url + '?' + self._create_params(payload)
        try:
            res = requests.get(full)
            if res.status_code == 200:
                return json.loads(res.text)
            else:
                print res.text
        except ConnectionError as e:
            print e.explanation

def main(argv=None):    
    pop = Population(input_dir = argv[2],
                     output_file = argv[3])

    if argv[1] == "demographics":                     
        d = pop.query( { 'source' : pop.population,
                         'data' : [get.pop['population']['total'],
                                   get.pop['population']['white'],
                                   get.pop['population']['black'],
                                   get.pop['population']['native'],
                                   get.pop['population']['asian'],
                                   get.pop['population']['pacific'],
                                   get.pop['population']['latino']],
                         'year' : 2010},
                       {'state' : 'Tennessee',
                        'county' : '*' } )

        # pop.pretty_print(d, ['total', 'white', 'black', 'native', 'asian', 'pacific', 'latino', 'state', 'county'])
        pop.raw_print(d, ['total', 'white', 'black', 'native', 'asian', 'pacific', 'latino', 'state', 'county'])
    else:
        d = pop.query( { 'source' : pop.economic,
                         'data' : [get.econ['median'],
                                   get.econ['mean'],
                                   get.econ['capita']],
                         'year' : 2012},
                       {'state' : 'Texas',
                        'county' : '*'} )
                        
        # pop.pretty_print(d, ['median', 'mean', 'capita', 'state', 'county'], replace = {'N':0,'-':0})
        pop.raw_print(d, ['median', 'mean', 'capita', 'state', 'county'], replace = {'N':0,'-':0})

if __name__ == "__main__":
    main(sys.argv)
