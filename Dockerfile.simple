FROM ubuntu:12.04
NAME pydata/census

RUN mkdir -p /home/ferry/pydata/bokeh /home/ferry/pydata/census /home/ferry/pydata/data /home/ferry/pydata/bokeh/templates

# Install everything
RUN apt-get --yes install g++ build-essential python-dev python-pip python-scientific python-pandas
ADD ./requirements.txt /home/ferry/pydata/
RUN pip install -r /home/ferry/pydata/requirements.txt

# Add the other various scripts. 
ADD ./README.md /home/ferry/pydata/
ADD ./Dockerfile /home/ferry/pydata/
ADD ./bokeh /home/ferry/pydata/bokeh/
ADD ./census /home/ferry/pydata/census/
ADD ./populate.sh /home/ferry/pydata/
ADD ./start.sh /home/ferry/pydata/
RUN chmod a+x /home/ferry/pydata/populate.sh
RUN chmod a+x /home/ferry/pydata/start.sh

# Now go ahead and download all the datasets for our demo. 
RUN /home/ferry/pydata/populate.sh

# Default command will run our plot and start the Bokeh server. 
CMD ["/home/ferry/pydata/start.sh"]