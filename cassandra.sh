#! /bin/bash

# 
# Download the various geographic datasets. This helps us look up county
# codes, zip coes, etc. 
# 
python /home/ferry/pydata/census/geography.py /home/ferry/pydata/data

#
# Create the economic datasets.
#
python /home/ferry/pydata/census/population.py economic Tennessee /home/ferry/pydata/data/ /home/ferry/pydata/data/tn_econ.psv
python /home/ferry/pydata/census/population.py economic Texas /home/ferry/pydata/data/ /home/ferry/pydata/data/tx_econ.psv
python /home/ferry/pydata/census/population.py economic Kentucky /home/ferry/pydata/data/ /home/ferry/pydata/data/ky_econ.psv

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