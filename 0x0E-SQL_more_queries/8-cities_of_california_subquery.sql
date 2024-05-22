-- Script lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Requirements:
--   The states table contains only one record where name = California (but the id can be different, as per the example)
--   Results must be sorted in ascending order by cities.id
--   You are not allowed to use the JOIN keyword
--   The database name will be passed as an argument of the mysql command

-- find the id in states table
SET @california_id = (SELECT id FROM states WHERE name = "California");

SELECT * FROM cities WHERE state_id = @california_id ORDER BY id ASC;
