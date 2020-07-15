-- 0x0E. SQL - More queries, task 2. Read user
-- Creates DB `hbtn_0d_2` user `user_0d_2`, sets pwd, and grants select prvg.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2; 
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
