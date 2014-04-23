#! /bin/bash

#
# Create the economic datasets.
# This creates PSV files for North Carolina, Tennessee, and Texas. 
#
python /home/ferry/pydata/population.py economic North Carolina /home/ferry/pydata/data/ /home/ferry/pydata/data/nc_econ.psv
python /home/ferry/pydata/population.py economic Tennessee /home/ferry/pydata/data/ /home/ferry/pydata/data/tn_econ.psv
python /home/ferry/pydata/population.py economic Texas /home/ferry/pydata/data/ /home/ferry/pydata/data/tx_econ.psv

#
# Create the median income plots and output to an HTML file. 
#
python /home/ferry/pydata/plot.py

#
# Start our web server. 
#
python /home/ferry/pydata/webserver.py
