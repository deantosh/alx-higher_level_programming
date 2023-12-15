-- lists all records of the table second_table of database hbtn_0c_0 in MySQL server
-- result should display both the scoreand the name (respectively)
-- records should be ordered by score (top first)
-- database name passed as an argument of the mysql command

SELECT score, name FROM second_table
ORDER BY score DESC;
