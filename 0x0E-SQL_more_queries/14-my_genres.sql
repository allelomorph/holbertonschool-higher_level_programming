-- 0x0E. SQL - More queries, task 14. My genres 
-- Lists all genres of show `Dexter` in `hbtn_0d_tvshows`. DB in args.
SELECT tv_genres.name
FROM tv_show_genres
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
/* -- alternate: conditional instead of join
SELECT tv_genres.name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id = tv_show_genres.genre_id
      AND tv_show_genres.show_id = tv_shows.id
      AND tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC; */
