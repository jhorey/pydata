FROM ferry/hadoop-client
NAME petsafe/demographics

RUN apt-get --yes install build-essential python-dev python-pip 
RUN mkdir -p /home/ferry/demographics
RUN mkdir -p /home/ferry/demographics/derived
WORKDIR /home/ferry/demographics
ADD ./src /home/ferry/demographics/
# RUN pip install -r /home/ferry/demographics/src/requirements.txt
# RUN /home/ferry/demographics/src/demographics.sh download
