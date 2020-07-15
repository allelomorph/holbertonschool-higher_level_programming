-- 0x0E. SQL - More queries, task 15. Only Comedy 
-- Lists all all comedy shows in `hbtn_0d_tvshows`. DB in args.
SELECT tv_shows.title
FROM tv_show_genres
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC; 
