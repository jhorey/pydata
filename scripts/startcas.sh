#! /bin/bash

#
# Create the Cassandra schemas
# Because this script is started right after Cassandra is started, sometimes
# Cassandra isn't quite ready, so we just try a few times. 
# 
for i in {1..10}; do
    python /home/ferry/pydata/bokeh/cassandra.py create > /tmp/cass.log
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
cqlsh -f /home/ferry/pydata/upload.cql /home/ferry/pydata/data/tn_econ.psv >> /tmp/cass.log
cqlsh -f /home/ferry/pydata/upload.cql /home/ferry/pydata/data/tx_econ.psv >> /tmp/cass.log
cqlsh -f /home/ferry/pydata/upload.cql /home/ferry/pydata/data/ky_econ.psv >> /tmp/cass.log

#
# Create the median income plots and output to an HTML file. 
#
python /home/ferry/pydata/bokeh/init.py
python /home/ferry/pydata/bokeh/cassandra.py plot Tennessee tn /home/ferry/pydata/bokeh/templates/
python /home/ferry/pydata/bokeh/cassandra.py plot Texas tx /home/ferry/pydata/bokeh/templates/
python /home/ferry/pydata/bokeh/cassandra.py plot Kentucky ky /home/ferry/pydata/bokeh/templates/

#
# Start our web server. 
#
nohup python /home/ferry/pydata/bokeh/webserver.py /home/ferry/pydata/data &
