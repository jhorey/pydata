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
- Ok install Redis via apt-get or yum. 
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



- Now you're becoming really famous for your awesome Docker demo. People think that understanding geospatial economic data is
  actually quite useful. One of your friends wants to integrate this data into their future data warehouse (which isn't built yet). 
  Wouldn't it be great if you could modify your script to work over Cassandra? Or maybe Hadoop? How hard could that be? 

- Ok... you could install Cassandra (and then Hadoop) and encapsulate that into your Dockerfile. So spin up your browser and start
  poking around.

- This is when you discover Ferry. 
