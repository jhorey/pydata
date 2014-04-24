#! /bin/bash

#
# Place PSV files into Cassandra.
#
python /home/ferry/pydata/census/upload.py /home/ferry/pydata/data/tn_econ.psv
python /home/ferry/pydata/census/upload.py /home/ferry/pydata/data/tx_econ.psv
python /home/ferry/pydata/census/upload.py /home/ferry/pydata/data/ky_econ.psv

#
# Create the median income plots and output to an HTML file. 
#
python /home/ferry/pydata/bokeh/init.py
python /home/ferry/pydata/bokeh/cassandra.py Tennessee tn /home/ferry/pydata/bokeh/templates/
python /home/ferry/pydata/bokeh/cassandra.py Texas tx /home/ferry/pydata/bokeh/templates/
python /home/ferry/pydata/bokeh/cassandra.py Kentucky ky /home/ferry/pydata/bokeh/templates/