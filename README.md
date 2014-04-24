## Bokeh Example with ACS dataset and Docker

This is a simple demo created for PyData 2014 showing how to package a simple Python application using Docker. 

### ACS dataset

This demo comes with some scripts to download data from the American Community Survey. This dataset
contains income information at the county and zip code level. 

### Docker

The entire demo can be run via Docker using the command:

```
	$ docker pull pydata/census
	$ docker run -p 5006:5006 -d pydata/census
```
