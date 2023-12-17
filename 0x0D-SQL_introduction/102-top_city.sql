-- import in hbtn_0c_0 database a table dump
-- display the average temperatures (Fahrenheit) by city ordered by temperature (descending)
-- display top three cities on the list
-- between month of july and august

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
