#! /bin/bash

# 
# Download the various geographic datasets. This helps us look up county
# codes, zip coes, etc. 
# 
python /home/ferry/pydata/census/geography.py

#
# Create the economic datasets.
# This creates PSV files for North Carolina, Tennessee, and Texas. 
#

python /home/ferry/pydata/census/population.py economic Tennessee /home/ferry/pydata/data/ /home/ferry/pydata/data/tn_econ.psv
python /home/ferry/pydata/census/population.py economic Texas /home/ferry/pydata/data/ /home/ferry/pydata/data/tx_econ.psv
python /home/ferry/pydata/census/population.py economic Kentucky /home/ferry/pydata/data/ /home/ferry/pydata/data/ky_econ.psv

#
# Create the median income plots and output to an HTML file. 
#
python /home/ferry/pydata/bokeh/plot.py

#
# Start our web server. 
#
# python /home/ferry/pydata/webserver.py
