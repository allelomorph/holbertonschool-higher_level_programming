# (272) 0x0D. SQL - Introduction
Foundations > Higher-level programming > Databases

---

### Project author
Guillaume Salva

### Assignment dates
07-13-2020 to 07-14-2020

### Description
Introduction to database storage via MySQL and creating SQL queries and functions.

### Provided File(s)
* [`temperatures.sql`](./temperatures.sql)

---

## Mandatory Tasks

### :white_check_mark: 0. List databases
Write a script that lists all databases of your MySQL server.

File(s): [`0-list_databases.sql`](./0-list_databases.sql)

### :white_check_mark: 1. Create a database
Write a script that creates the database `hbtn_0c_0` in your MySQL server.
* If the database `hbtn_0c_0` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

File(s): [`1-create_database_if_missing.sql`](./1-create_database_if_missing.sql)

### :white_check_mark: 2. Delete a database
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
* If the database `hbtn_0c_0` doesn’t exist, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

File(s): [`2-remove_database.sql`](./2-remove_database.sql)

### :white_check_mark: 3. List tables
Write a script that lists all the tables of a database in your MySQL server.
* The database name will be passed as argument of `mysql` command

File(s): [`3-list_tables.sql`](./3-list_tables.sql)

### :white_check_mark: 4. First table
Write a script that creates a table called `first_table` in the current database in your MySQL server.
* first_table description:
    * `id` INT
    * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `first_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

File(s): [`4-first_table.sql`](./4-first_table.sql)

### :white_check_mark: 5. Full description
Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command
* You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

File(s): [`5-full_table.sql`](./5-full_table.sql)

### :white_check_mark: 6. List all in table
Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* All fields should be printed
* The database name will be passed as an argument of the `mysql` command

File(s): [`6-list_values.sql`](./6-list_values.sql)

### :white_check_mark: 7. First add
Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
* New row:
    * `id` = 89
    * `name` = `Best School`
* The database name will be passed as an argument of the `mysql` command

File(s): [`7-insert_value.sql`](./7-insert_value.sql)

### :white_check_mark: 8. Count 89
Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command

File(s): [`8-count_89.sql`](./8-count_89.sql)

### :white_check_mark: 9. Full creation
Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
* `second_table` description:
    * `id` INT
    * `name` VARCHAR(256)
    * `score` INT
* The database name will be passed as an argument to the `mysql` command
* If the table `second_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` and `SHOW` statements
* Your script should create these records:
    * `id` = 1, `name` = “John”, `score` = 10
    * `id` = 2, `name` = “Alex”, `score` = 3
    * `id` = 3, `name` = “Bob”, `score` = 14
    * `id` = 4, `name` = “George”, `score` = 8

File(s): [`9-full_creation.sql`](./9-full_creation.sql)

### :white_check_mark: 10. List by best
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

File(s): [`10-top_score.sql`](./10-top_score.sql)

### :white_check_mark: 11. Select the best
Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

File(s): [`11-best_score.sql`](./11-best_score.sql)

### :white_check_mark: 12. Cheating is bad
Write a script that updates the score of Bob to 10 in the table `second_table`.
* You are not allowed to use Bob’s id value, only the `name` field
* The database name will be passed as an argument of the `mysql` command

File(s): [`12-no_cheating.sql`](./12-no_cheating.sql)

### :white_check_mark: 13. Score too low
Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command

File(s): [`13-change_class.sql`](./13-change_class.sql)

### :white_check_mark: 14. Average
Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* The result column name should be `average`
* The database name will be passed as an argument of the `mysql` command

File(s): [`14-average.sql`](./14-average.sql)

### :white_check_mark: 15. Number by score
Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* The result should display:
    * the `score`
    * the number of records for this `score` with the label number
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the `mysql` command

File(s): [`15-groups.sql`](./15-groups.sql)

### :white_check_mark: 16. Say my name
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* Don’t list rows without a `name` value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the `mysql` command

File(s): [`16-no_link.sql`](./16-no_link.sql)

## Advanced Tasks

### :white_check_mark: 17. Go to UTF8
Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

You need to convert all of the following to UTF8:
* Database `hbtn_0c_0`
* Table `first_table`
* Field `name` in `first_table`

File(s): [`100-move_to_utf8.sql`](./100-move_to_utf8.sql)

### :white_check_mark: 18. Temperatures #0
Import in `hbtn_0c_0` database this table dump: [`temperatures.sql`](./temperatures.sql)

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

File(s): [`101-avg_temperatures.sql`](./101-avg_temperatures.sql)

### :white_check_mark: 19. Temperatures #1
Import in `hbtn_0c_0` database this table dump: [`temperatures.sql`](./temperatures.sql) (same as Temperatures #0)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

File(s): [`102-top_city.sql`](./102-top_city.sql)

### :white_check_mark: 20. Temperatures #2
Import in `hbtn_0c_0` database this table dump: [`temperatures.sql`](./temperatures.sql) (same as Temperatures #0)

Write a script that displays the max temperature of each state (ordered by State name).

File(s): [`103-max_state.sql`](./103-max_state.sql)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
