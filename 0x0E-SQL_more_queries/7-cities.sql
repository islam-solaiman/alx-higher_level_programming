-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL, name VARCHAR(256) NOT NULL,
PRIMARY KEY(id), FOREIGN KEY(state_id) REFERENCES states(id));
