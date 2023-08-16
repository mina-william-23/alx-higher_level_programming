-- This script creates the table force_name on my MySQL server
-- it does not fail if the table force_name already exists

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);
