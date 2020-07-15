-- 0x0E. SQL - More queries, task 13. Number of shows by genre 
-- Lists all genres in `hbtn_0d_tvshows` and total linked shows.
   -- DB in args.
SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
