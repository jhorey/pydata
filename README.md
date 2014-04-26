Plotting American Community Survey data with Python Bokeh
=========================================================

This is a simple demo created for PyData 2014 showing how to package a simple Python Bokeh application using Docker and Ferry. 
This demo uses the following technologies:

* [Docker](https://www.docker.io/)
* [Ferry](http://ferry.opencore.io)
* [Bokeh](http://bokeh.pydata.org/)

To make things interesting, it also uses data from the American Community Survey. This survey contains economic data at the county
and zip code levels for the United States. The ACS and U.S. Census provides a nice API to access this data. You can find the scripts
that downloads/parses that data under `census`. 

Getting Started
---------------

This demo assumes that you have both [Docker](https://www.docker.io/) and [Ferry](http://ferry.opencore.io) installed. If neither are true, you can grab the Ferry [Vagrant](http://www.vagrantup.com) box like this:

```
        $ vagrant box add opencore/ferry https://s3.amazonaws.com/opencore/ferry.box
        $ vagrant init opencore/ferry
        $ vagrant up
```

This box has both Docker and Ferry pre-installed. Now onto the demos!

There are actually two demos, one relying solely on Docker and another that uses Ferry and incorporates Cassandra. 
The Docker demo can be run using the command:

```
	$ docker pull ferry/pydata
	$ docker run -p 8000:8000 -d ferry/pydata
```

Afterwards, point your browser to `localhost:8000` and you should see a very simple web page with links to a few states. 

To run the more advanced Ferry application, you'll have to clone this repository first (this isn't actually true, you just need one file in this repository):

```
	$ git clone https://github.com/jhorey/pydata
```

Then type:

```
	$ ferry start pydata/cassandra.yml -b pydata/
```

If you are running the latest version of Ferry or if you are restarting the Ferry demo, you can skip the `-b pydata/` part (which tells Ferry to manually build the image). If you take a peek in the `pydata/cassandra.yml` file, you will see: 

```
backend:
   - storage:
        personality: "cassandra"
        instances: 1
connectors:
   - personality: "ferry/pydata-cassandra"
     ports: ["8000:8000"]

```

This file just tells Ferry how to build your application. You can see that it relies on Cassandra and uses exposes port `8000` (just like the plain Docker demo). 

