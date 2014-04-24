USE census;
COPY acs_economic_data FROM '${1}' WITH DELIMITER = '|';