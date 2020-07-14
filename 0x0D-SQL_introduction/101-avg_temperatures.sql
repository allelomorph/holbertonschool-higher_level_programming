-- 0x0D. SQL - Introduction, task 18. Temperatures #0
-- Lists `city` and average temp (F) in desc order from `temperatures`.
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city
       ORDER BY avg_temp DESC;
