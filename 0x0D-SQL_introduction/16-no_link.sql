-- lists the number of records with the same score in the table second_table
-- The result should display:
--     -  the score and name (respectively)
-- sorted by the score (desc)
-- database name will be passed as an argument to the mysql command

SELECT score, name FROM second_table
ORDER BY score DESC;
