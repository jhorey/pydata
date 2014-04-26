#! /bin/bash

#
# Read in any environment variables. 
#
source /etc/profile

#
# Start our web server. 
# Wait a couple seconds to make sure that it starts. 
#
nohup python /home/ferry/pydata/bokeh/webserver.py /home/ferry/pydata/data > /tmp/web.log 2> /tmp/web.err &
sleep 2