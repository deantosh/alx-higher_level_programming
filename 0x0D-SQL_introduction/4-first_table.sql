-- creates a table called first_table in the current database in MySQL server
-- first table description:
--    id INT
--    name VARCHAR(256)
-- database name will be passed as argument of the mysql command
-- if table exists script should not fail
-- SELECT or SHOW commands not allowed

CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);
