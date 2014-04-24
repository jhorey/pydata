CREATE KEYSPACE census WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE census;

CREATE TABLE acs_economic_data  (
       state_cd STRING,
       state_name STRING,
       county_cd STRING,
       county_name STRING,
       median INT,
       mean INT,
       capita INT
);
