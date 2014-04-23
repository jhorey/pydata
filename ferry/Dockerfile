FROM ferry/cassandra-client
NAME pydata/census

# Install everything
RUN apt-get --yes install build-essential python-dev python-pip python-scientific python-pandas redis-server
RUN mkdir -p /home/ferry/pydata
WORKDIR /home/ferry/pydata
ADD ./src /home/ferry/pydata/
RUN pip install -r /home/ferry/pydata/requirements.txt

# Add the start script
ADD ./start.sh /home/ferry/

# Default command will run our plot and start the Bokeh server. 
CMD ["/home/ferry/start.sh"]