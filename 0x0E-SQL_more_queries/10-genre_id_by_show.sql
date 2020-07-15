-- 0x0E. SQL - More queries, task 10. Genre ID by show 
-- Lists all shows in `hbtn_0d_tvshows` that have 1+ genre linked. DB in args.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
