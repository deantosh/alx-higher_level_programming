-- import in hbtn_0c_0 database a table dump
-- display the average temperatures (Fahrenheit) by city ordered by temperature (descending)
-- display top three cities on the list

SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
