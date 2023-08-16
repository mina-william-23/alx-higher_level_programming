-- This script creates the table unique_id on my MySQL server
-- it does not fail if unique_id already exists
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
