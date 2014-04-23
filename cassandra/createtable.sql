CREATE KEYSPACE pydata WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE pydata;

CREATE TABLE economic_raw  (
       state_cd STRING,
       state_name STRING,
       county_cd STRING,
       county_name STRING,
       median INT,
       mean INT,
       capita INT
);

COPY economic_raw FROM '/home/ferry/demographics/data /home/ferry/demographics/derived/economic.data' WITH DELIMITER = '|';
