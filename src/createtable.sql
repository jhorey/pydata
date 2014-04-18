CREATE TABLE population_raw  (
       state_cd STRING,
       state_name STRING,
       county_cd STRING,
       county_name STRING,
       zip_cd STRING,
       pop_total INT,
       pop_adults INT,
       pop_white INT,
       pop_black INT,
       pop_native INT,
       pop_asian INT,
       pop_pacific INT,
       pop_latino INT
) 
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

CREATE TABLE economic_raw  (
       zip_cd STRING,
       median INT,
       mean INT,
       capita INT
) 
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

LOAD DATA INPATH '/demographics/population.data'
OVERWRITE INTO TABLE population_raw;

LOAD DATA INPATH '/demographics/economic.data'
OVERWRITE INTO TABLE economic_raw;
