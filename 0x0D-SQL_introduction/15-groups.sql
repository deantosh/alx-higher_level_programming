-- lists the number of records with the same score in the table second_table
-- The result should display:
--     -  the score
--     - the number of records for this score with the label number
-- sorted by the number of records (desc)
-- database name will be passed as an argument to the mysql command

SELECT score, COUNT(*) as number FROM second_table
GROUP BY score
ORDER BY number DESC;
