-- Create a table 'citiies' in the hbtn_0_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
