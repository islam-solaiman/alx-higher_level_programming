-- script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- CREATE table states (in the database hbtn_0d_usa) on your MySQL server
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(ID));
