#! /bin/bash

#
# Read in any environment variables. 
#
source /etc/profile

# 
# This downloads the Bokeh sample dataset. It basically contains the geospatial
# information for the mapping part. The next step is to import all this
# into Cassandra (yet another interesting excercise). 
# 
python /home/ferry/pydata/bokeh/init.py

#
# Create the Cassandra schemas
# Because this script is started right after Cassandra is started, sometimes
# Cassandra isn't quite ready, so we just try a few times. 
# 
for i in {1..10}; do
    python /home/ferry/pydata/bokeh/cassplot.py create > /tmp/cass.log 2> /tmp/cass.err
    OUT=$(cat /tmp/cass.log)
    if [[ $OUT == "ok" ]]; then    
	break
    else
	sleep 3
    fi
done

#
# Place PSV files into Cassandra.
#
python /home/ferry/pydata/bokeh/cassplot.py upload /home/ferry/pydata/data/tn_econ.psv 2>> /tmp/cass.err
python /home/ferry/pydata/bokeh/cassplot.py upload /home/ferry/pydata/data/tx_econ.psv 2>> /tmp/cass.err
python /home/ferry/pydata/bokeh/cassplot.py upload /home/ferry/pydata/data/ky_econ.psv 2>> /tmp/cass.err

#
# Create the median income plots and output to an HTML file. 
#
python /home/ferry/pydata/bokeh/cassplot.py plot Tennessee tn /home/ferry/pydata/bokeh/templates/ 2>> /tmp/plots.err
python /home/ferry/pydata/bokeh/cassplot.py plot Texas tx /home/ferry/pydata/bokeh/templates/ 2>> /tmp/plots.err
python /home/ferry/pydata/bokeh/cassplot.py plot Kentucky ky /home/ferry/pydata/bokeh/templates/ 2>> /tmp/plots.err

#
# Start our web server. 
# Wait a couple seconds to make sure that it starts. 
#
nohup python /home/ferry/pydata/bokeh/webserver.py /home/ferry/pydata/data > /tmp/web.log 2> /tmp/web.err &
sleep 2