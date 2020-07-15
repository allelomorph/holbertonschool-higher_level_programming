-- 0x0E. SQL - More queries, task 4. ID can't be null
-- Creates table `id_not_null` with `id and `name` fields. DB in args.
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
); 
