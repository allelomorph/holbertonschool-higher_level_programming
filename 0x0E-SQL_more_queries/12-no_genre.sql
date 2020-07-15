-- 0x0E. SQL - More queries, task 12. No genre 
-- Lists all shows in `hbtn_0d_tvshows` without genre by title, genre.
   -- DB in args.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
