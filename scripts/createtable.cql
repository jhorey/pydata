CREATE KEYSPACE census WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE census;

CREATE TABLE acs_economic_data  (
       state_cd TEXT,
       state_name TEXT,
       county_cd TEXT,
       county_name TEXT,
       median INT,
       mean INT,
       capita INT,
       PRIMARY KEY(count_cd, state_cd)
);
