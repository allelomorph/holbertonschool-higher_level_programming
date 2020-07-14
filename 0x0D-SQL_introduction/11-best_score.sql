-- 0x0D. SQL - Introduction, task 11. Select the best
-- Lists scores/names in `second_table` in desc. order by scores >= 10.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
