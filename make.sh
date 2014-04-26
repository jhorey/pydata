#! /bin/bash

# Bash colors
GREEN='\e[0;32m'
NC='\e[0m'

function print {
    echo -e "${GREEN} ${1} ${NC}"
}

if [[ $# == 0 ]]; then
    print "usage: make.sh (docker|ferry)"
    exit 1
fi

if [[ $1 == "docker" ]]; then
    print "Creating plain Docker image"
    cp Dockerfile.simple Dockerfile
    docker build -t ferry/pydata .
    rm Dockerfile
elif [[ $1 == "ferry" ]]; then
    print "Creating and starting Cassandra Ferry image"
    cp Dockerfile.ferry Dockerfile
    ferry start cassandra.yml -b ./ 
    rm Dockerfile
fi