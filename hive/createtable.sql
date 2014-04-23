CREATE TABLE economic_raw  (
       state_cd STRING,
       state_name STRING,
       county_cd STRING,
       county_name STRING,
       median INT,
       mean INT,
       capita INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

LOAD DATA INPATH '/home/ferry/pydata/data/nc_econ.psv'
INTO TABLE movielens_users_text;

LOAD DATA INPATH '/home/ferry/pydata/data/tn_econ.psv'
INTO TABLE movielens_users_text;

LOAD DATA INPATH '/home/ferry/pydata/data/tx_econ.psv'
INTO TABLE movielens_users_text;
