# (274) 0x0E. SQL - More queries
Foundations > Higher-level programming > Databases

---

### Project author
Guillaume Salva

### Assignment dates
07-14-2020 to 07-15-2020

### Description
Addtional database and SQL concepts: managing user privileges, `PRIMARY KEY`/`FOREIGN KEY`, querying multiple tables, `JOIN`s and `UNION`s. 

### Provided File(s)
* [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) [`hbtn_0d_tvshows_rate.sql`](./hbtn_0d_tvshows_rate.sql)

---

## Mandatory Tasks

### :white_check_mark: 0. My privileges!
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`.)

File(s): [`0-privileges.sql`](./0-privileges.sql)

### :white_check_mark: 1. Root user
Write a script that creates the MySQL server user `user_0d_1`.
* `user_0d_1` should have all privileges on your MySQL server
* The `user_0d_1` password should be set to `user_0d_1_pwd`
* If the user `user_0d_1` already exists, your script should not fail

File(s): [`1-create_user.sql`](./1-create_user.sql)

### :white_check_mark: 2. Read user
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
* `user_0d_2` should have only `SELECT` privilege in the database `hbtn_0d_2`
* The `user_0d_2` password should be set to `user_0d_2_pwd`
* If the database `hbtn_0d_2` already exists, your script should not fail
* If the user `user_0d_2` already exists, your script should not fail

File(s): [`2-create_read_user.sql`](./2-create_read_user.sql)

### :white_check_mark: 3. Always a name
Write a script that creates the table `force_name` on your MySQL server.
* force_name description:
    * `id` INT
    * `name` VARCHAR(256) can’t be null
* The database name will be passed as an argument of the `mysql` command
* If the table `force_name` already exists, your script should not fail

File(s): [`3-force_name.sql`](./3-force_name.sql)

### :white_check_mark: 4. ID can't be null
Write a script that creates the table `id_not_null` on your MySQL server.
* `id_not_null` description:
    * `id` INT with the default value 1
    * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `id_not_null` already exists, your script should not fail

File(s): [`4-never_empty.sql`](./4-never_empty.sql)

### :white_check_mark: 5. Unique ID
Write a script that creates the table `unique_id` on your MySQL server.
* `unique_id` description:
    * `id` INT with the default value 1 and must be unique
    * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `unique_id` already exists, your script should not fail

File(s): [`5-unique_id.sql`](./5-unique_id.sql)

### :white_check_mark: 6. States table
Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.
* `states` description:
    * `id` INT unique, auto generated, can’t be null and is a primary key
    * `name` VARCHAR(256) can’t be null
* If the database `hbtn_0d_usa` already exists, your script should not fail
* If the table `states` already exists, your script should not fail

File(s): [`6-states.sql`](./6-states.sql)

### :white_check_mark: 7. Cities table
Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.
* `cities` description:
    * `id` INT unique, auto generated, can’t be null and is a primary key
    * `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
    * `name` VARCHAR(256) can’t be null
* If the database `hbtn_0d_usa` already exists, your script should not fail
* If the table `cities` already exists, your script should not fail

File(s): [`7-cities.sql`](./7-cities.sql)

### :white_check_mark: 8. Cities of California
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
* The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)
* Results must be sorted in ascending order by `cities.id`
* You are not allowed to use the `JOIN` keyword
* The database name will be passed as an argument of the `mysql` command

File(s): [`8-cities_of_california_subquery.sql`](./8-cities_of_california_subquery.sql)

### :white_check_mark: 9. Cities by States
Write a script that lists all cities contained in the database `hbtn_0d_usa`.
* Each record should display: `cities.id` - `cities.name` - `states.name`
* Results must be sorted in ascending order by `cities.id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`9-cities_by_state_join.sql`](./9-cities_by_state_join.sql)

### :white_check_mark: 10. Genre ID by show
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.
* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`10-genre_id_by_show.sql`](./10-genre_id_by_show.sql)

### :white_check_mark: 11. Genre ID for all shows
Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `10-genre_id_by_show.sql`)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.
* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* If a show doesn’t have a genre, display `NULL`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`11-genre_id_all_shows.sql`](./11-genre_id_all_shows.sql)

### :white_check_mark: 12. No genre
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `11-genre_id_all_shows.sql`)

Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and tv_show_genres.genre_id
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`12-no_genre.sql`](./12-no_genre.sql)

### :white_check_mark: 13. Number of shows by genre
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `12-no_genre.sql`)

Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
* Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`
* First column must be called `genre`
* Second column must be called `number_of_shows`
* Don’t display a genre that doesn’t have any shows linked
* Results must be sorted in descending order by the number of shows linked
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`13-count_shows_by_genre.sql`](./13-count_shows_by_genre.sql)

### :white_check_mark: 14. My genres
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `13-count_shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.
* The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
* Each record should display: `tv_genres.name`
* Results must be sorted in ascending order by the genre name
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`14-my_genres.sql`](./14-my_genres.sql)

### :white_check_mark: 15. Only Comedy
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `14-my_genres.sql`)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.
* The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
* Each record should display: `tv_shows.title`
* Results must be sorted in ascending order by the show title
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`15-comedy_only.sql`](./15-comedy_only.sql)

### :white_check_mark: 16. List shows and genres
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `15-comedy_only.sql`)

Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
* If a show doesn’t have a genre, display `NULL` in the genre column
* Each record should display: `tv_shows.title` - `tv_genres.name`
* Results must be sorted in ascending order by the show title and genre name
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`16-shows_by_genre.sql`](./16-shows_by_genre.sql)

## Advanced Tasks

### :white_check_mark: 17. Not my genre
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `16-shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`
* The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
* Each record should display: `tv_genres.name`
* Results must be sorted in ascending order by the genre name
* You can use a maximum of two `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`100-not_my_genres.sql`](./100-not_my_genres.sql)

### :white_check_mark: 18. No Comedy tonight!
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [`hbtn_0d_tvshows.sql`](./hbtn_0d_tvshows.sql) (same as `100-not_my_genres.sql`)

Write a script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.
* The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
* Each record should display: `tv_shows.title`
* Results must be sorted in ascending order by the show title
* You can use a maximum of two `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`101-not_a_comedy.sql`](./101-not_a_comedy.sql)

### :white_check_mark: 19. Rotten tomatoes
Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [`hbtn_0d_tvshows_rate.sql`](./hbtn_0d_tvshows_rate.sql)

Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.
* Each record should display: `tv_shows.title` - `rating sum`
* Results must be sorted in descending order by the rating
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`102-rating_shows.sql`](./102-rating_shows.sql)

### :white_check_mark: 20. Best genre
Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [`hbtn_0d_tvshows_rate.sql`](./hbtn_0d_tvshows_rate.sql)
 (same as `102-rating_shows.sql`)

Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.
* Each record should display: `tv_genres.name` - `rating sum`
* Results must be sorted in descending order by their rating
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

File(s): [`103-rating_genres.sql`](./103-rating_genres.sql)

### :white_large_square: 21. How Do SQL Database Engines Work?
Based on this [video](https://youtu.be/Z_cX3bzkExE) and [presentation](https://raw.githubusercontent.com/maxmcd/how-sqlite-works/master/how-sqlite-works.pdf), write a blog post to explain to your mother “How Do SQL Database Engines Work?”. Your blog post should contain:
* an introduction
* complete explanation
* examples (not the same as the video)
* diagrams
* a summary/conclusion

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
