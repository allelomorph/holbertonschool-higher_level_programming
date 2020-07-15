-- 0x0E. SQL - More queries, task 9. Cities by States
-- Lists all cities found in `hbtn_0d_usa`, and their states. DB in args.
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON states.id = cities.state_id
ORDER BY cities.id;
/* -- alternate with conditional:
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE states.id = cities.state_id
ORDER BY cities.id ASC; */
