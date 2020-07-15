-- 0x0E. SQL - More queries, task 6. States table
-- Creates DB `hbtn_0d_usa`
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Creates table `states` with fields `id` and `name`.
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL
); 
