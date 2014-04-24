#! /bin/bash

# Bash colors
GREEN='\e[0;32m'
NC='\e[0m'

function print {
    echo -e "${GREEN} ${1} ${NC}"
}

if [[ $1 == "docker" ]]; then
    print "Creating plain Docker image"
    cp Dockerfile.simple Dockerfile
    docker build -t pydata/census .
    rm Dockerfile
else
    print "Creating Cassandra Ferry image"
    cp Dockerfile.ferry Dockerfile
    ferry start pydata.yaml -b ./ 
    rm Dockerfile
fi