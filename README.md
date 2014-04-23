## Why Docker? 

- Say you want to use Bokeh
- So you type in "pip install bokeh"
- Normally this works just fine for Python packages. 
- But Bokeh relies on some native libraries like Pandas and Numpy. So
  the installation fails.
- The user doesn't give up and installs python-dev via apt-get or yum (or 
  some other distro specific mechanism). 
- When I ran this command on my fresh Ubuntu 12.04 install, I got the following error
  "gcc: error trying to exec 'cc1plus': execvp: No such file or directory"
  - You do a Google search, and find that means you need to properly install g++ 
  - So you do a apt-get install g++
- Ok installation finished!
- Then the user reads about "bokeh-server". Starting bokeh-server throws an error
  because the user needs to install Redis. 
- Ok install Redis via apt-get or yum. Oh, it turns out that you're running Ubuntu 12.04 which
  comes with an older version of Redis. You'll have to grab a newer version by manually adding
  a PPA. 
- Now finally, they can create a few plots and serve them via bokeh
- But he's just getting started and would like some examples, ideally some that
  he can just clone & run. 

- He reads about this great American Community Survey script from OpenCore, but the author is lazy
  and hasn't uploaded it onto the pypi index. 
- So now our data scientist needs to use "git". Maybe he's familiar with it, but maybe
  not. So apt-get that. 
- So now he has to run a few commands in a very specific order, otherwise things won't
  run the way he wants:
  (1) git clone https://github.com/opencore/census.git
  (2) python census/geography.py ./data
  (3) python census/population.py economic North Carolina ./data ./data/nc_econ.psv
  (4) bokeh-server
  (5) python census/plot.py

- Yes, now you're done! Unless you typed in something incorrectly. Then you should figure out what you did wrong :(

- Well you're hard working, so you eventually get this working. You feel like SuperMan. You are SuperMan. You write a blog
  article describing the simple steps you took to get it working. 
- Your friend is impressed. She wants to replicate this on her machine. But she's running she's running Redhat and one of
  these steps failed. Could you be so kind to figure out the problem and update your blog article? 

- Well you are SuperMan. So you're going to fix this once and for all. 
  - But where to start? Maybe a simple shell script that types in all the commands you used? But the Redhat commands will
    be different. What if she's running Python3 by default and the scripts break?
  - Wouldn't it be nice if you could guarantee that she runs the exact same commands in the exactly the right order, and in 
    exactly the same environment that you ran these commands? 
  - I guess you could use Vagrant. But you have create this 1GB "box" file, and then host it somewhere. Who wants to download
    a brand new 1GB VM just to run your demo? 

- This is where Docker steps in. 
- It is a very simple mechanism to create a fully reproducible runtime environment.

- Now you're becoming really famous for your awesome Docker demo. Someone suggests that , 'hey maybe you can turn this demo into
  a startup'. Perhaps a service to generate custom maps using different datasets. Definately you'll include Census and ACS. You're
  thinking of also including daily weather from the Weather Underground. They have a nice API. Also, you could include geospatially
  tagged Tweets. Maybe even traffic related data via the MapQuest API. 
- So you begin thinking, ok how do we do this? 
- You have lots of different data sources, and you need some consistent way of updating and access the data. So you decide to put
  everything into a database. 
- You've heard Cassandra is pretty cool and scalable and all that good stuff. So why not? 

- So you begin developing your application (all in Python of course). You extend the Census & ACS programs to include even more data. 
  You create a new program to fetch and transform the weather data. Another for the traffic data. 
- You really like Docker and the fact that it lets you create reproducible environments, so each application gets its own Dockerfile. This
  also makes it easier to share and test with the rest of the team. 

- So then you also decide you're going to make Cassandra its own Docker service. It's slightly more painful than setting up the Python
  application Dockerfiles, but after a few hours you seem to have a single node Cassandra service. 
- Then you read about how to plug this into each of the application services. They'll need to know the IP of the Cassandra service and have the various
  drivers installed. 
- Now, one of your developers on your team wants their own instance of the entire service (all the application servers and the Cassandra instance) 
  because he's working on the unified web interface and needs to make sure everything works. 
- So you write a bunch of scripts that orchestrates all of this. It's in bash, which has its own sort of horrific beauty. 
- Hopefully no will need to turn these services on and off because, you know, that might break things :(
- So you begin thinking, hmmm is there a better way to do this? 


- This is when you discover Ferry. 
