-- 0x0E. SQL - More queries, task 8. Cities of California
-- Lists all cities in CA found in `hbtn_0d_usa`. DB in args.
SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
