#! /bin/bash

# Bash colors
GREEN='\e[0;32m'
NC='\e[0m'

function run_as_ferry {
    echo -e "${GREEN} ${2} ${NC}"
    if [ $USER == "root" ]; then
	su ferry -c "$1"
    else
	$1
    fi
}

if [[ $1 == "download" ]]; then
    GEN='python geography.py /home/ferry/demographics/data'
    run_as_ferry "$GEN" "Downloading geospatial dataset"
elif [[ $1 == "load" ]]; then
    GEN1='python population.py demographics /home/ferry/demographics/data /home/ferry/demographics/derived/population.data'
    GEN2='python population.py economics /home/ferry/demographics/data /home/ferry/demographics/derived/economic.data'
    MKDIR='hdfs dfs -mkdir -p /demographics'
    COPY1='hdfs dfs -copyFromLocal /home/ferry/demographics/derived/population.data /demographics/'
    COPY2='hdfs dfs -copyFromLocal /home/ferry/demographics/derived/economic.data /demographics/'
    HIVE='hive -f /home/ferry/demographics/src/createtable.sql'

    run_as_ferry "$GEN1" "Generating population dataset"
    run_as_ferry "$GEN2" "Generating economic dataset"
    run_as_ferry "$MKDIR" "Making demographics directory"
    run_as_ferry "$COPY1" "Copy population dataset to HDFS"
    run_as_ferry "$COPY2" "Copy economic dataset to HDFS"
    run_as_ferry "$HIVE" "Loading Hive tables"
fi