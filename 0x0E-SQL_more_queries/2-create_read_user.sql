-- This script creates the database hbtn_0d_2 and the user user_0d_2 (with SELECT privilege)
-- password is user_0d_2_pwd
-- it does not fail if hbtn_0d_2 or user_0d_2 already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
