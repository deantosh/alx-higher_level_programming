-- lists all records with score >= 10 in the table second_table of database hbtn_0c_0 in MySQL server
-- result should display both the score and the name (respectively)
-- records should be ordered by score (top first)
-- database name passed as an argument of the mysql command

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
