-- 0x0D. SQL - Introduction, task 20. Temperatures #2
-- Lists top 3 max temps in (F), by state code.
SELECT state, MAX(value) AS max_temp FROM temperatures
       GROUP BY state ORDER BY state LIMIT 3;
