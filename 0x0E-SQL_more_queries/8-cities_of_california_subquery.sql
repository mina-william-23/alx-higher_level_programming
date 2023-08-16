--  lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, state_id, name FROM states WHERE state_id = (SELECT cities.id FROM cities WHERE name = "California") WHERE ORDER BY id;
