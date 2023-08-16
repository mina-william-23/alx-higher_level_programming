-- This script creates the MySQL server user user_0d_1 (with all privileges)
-- password is user_0d_1_pwd
-- it does not fail if user_0d_1 already exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
