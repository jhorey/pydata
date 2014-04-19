#! /bin/bash

bokeh-server >> /tmp/bokeh.log &
python /home/ferry/pydata/src/plot.py
