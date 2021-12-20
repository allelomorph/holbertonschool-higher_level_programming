# (283) 0x0F. Python - Object-relational mapping
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
08-07-2020 to 08-10-2020

### Description
Bridging the gap between Python and SQL in two ways: using the module `MySQLdb` to connect to a database and execute SQL queries, and using the `SQLAlchemy` module as an introduction to Object Relational Mapping.

### Provided File(s)
* [`0-select_states.sql`](./tests/0-select_states.sql) [`4-cities_by_state.sql`](./tests/4-cities_by_state.sql) [`6-model_state.sql`](./tests/6-model_state.sql) [`6-model_state.py`](./tests/6-model_state.py) [`7-model_state_fetch_all.sql`](./tests/7-model_state_fetch_all.sql) [`14-model_city_fetch_by_state.sql`](./tests/14-model_city_fetch_by_state.sql)
* [`100-relationship_states_cities.sql`](./tests/100-relationship_states_cities.sql) [`101-relationship_states_cities_list.sql`](./tests/101-relationship_states_cities_list.sql) 

### More Info
#### Install `MySQLdb` module version `1.3.x`

For installing `MySQLdb`, you need to have `MySQL` installed: see [repo README](../)
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(1, 3, 10, 'final', 0)
```

#### Install `SQLAlchemy` module version 1.2.x
```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.2.5'
```
If seen, this warning message can be ignored:
```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
  cursor.execute(statement, parameters)
```

---

## Mandatory Tasks

### :white_check_mark: 0. Get all states
Write a script that lists all `states` from the database `hbtn_0e_0_usa`:
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

File(s): [`0-select_states.py`](./0-select_states.py)

### :white_check_mark: 1. Filter states
Write a script that lists all `states with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

File(s): [`1-filter_states.py`](./1-filter_states.py)

### :white_check_mark: 2. Filter states by user input
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and state name searched (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* You must use `format` to create the SQL query with the user input
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

File(s): [`2-my_filter_states.py`](./2-my_filter_states.py)

### :white_check_mark: 3. SQL Injection...
If you test the follwing as an input to the previous task:
```bash
$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
$ ./0-select_states.py root root hbtn_0e_0_usa
$ 
```
Not only is there not output, it is actually a [SQL injection](./https://en.wikipedia.org/wiki/SQL_injection) to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!
* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

File(s): [`3-my_safe_filter_states.py`](./3-my_safe_filter_states.py)

### :white_check_mark: 4. Cities by states
Write a script that lists all `cities` from the database `hbtn_0e_4_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `cities.id`
* You can use only `execute()` once
* Your code should not be executed when imported

File(s): [`4-cities_by_state.py`](./4-cities_by_state.py)

### :white_check_mark: 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `cities.id`
* You can use only `execute()` once
* Your code should not be executed when imported

File(s): [`5-filter_cities.py`](./5-filter_cities.py)

### :white_check_mark: 6. First state model
Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:
* `State` class:
    * inherits from `Base` Tips
    * links to the MySQL table `states`
    * class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    * class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
* You must use the module `SQLAlchemy`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* **WARNING**: all classes who inherit from `Base` **must** be imported before calling `Base.metadata.create_all(engine)`

File(s): [`model_state.py`](./model_state.py)

### :white_check_mark: 7. All states via SQLAlchemy
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

File(s): [`7-model_state_fetch_all.py`](./7-model_state_fetch_all.py)

### :white_check_mark: 8. First state
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* The state you display must be the first in `states.id`
* You are not allowed to fetch all states from the database before displaying the result
* If the table `states` is empty, print `Nothing` followed by a new line
* Your code should not be executed when imported

File(s): [`8-model_state_fetch_first.py`](./8-model_state_fetch_first.py)

### :white_check_mark: 9. Contains `a`
Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

File(s): [`9-model_state_filter_a.py`](./9-model_state_filter_a.py)

### :white_check_mark: 10. Get a state
Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` to search (SQL injection free)
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* You can assume you have one record with the state name to search
* Results must display the `states.id`
* If no state has the name you searched for, display `Not found`
* Your code should not be executed when imported

File(s): [`10-model_state_my_get.py`](./10-model_state_my_get.py)

### :white_check_mark: 11. Add a new state
Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Print the new `states.id` after creation
* Your code should not be executed when imported

File(s): [`11-model_state_insert.py`](./11-model_state_insert.py)

### :white_check_mark: 12. Update a state
Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Change the name of the `State` where `id = 2` to `New Mexico`
* Your code should not be executed when imported

File(s): [`12-model_state_update_id_2.py`](./12-model_state_update_id_2.py)

### :white_check_mark: 13. Delete states
Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Your code should not be executed when imported

File(s): [`13-model_state_delete_a.py`](./13-model_state_delete_a.py)

### :white_check_mark: 14. Cities in state
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.
* `City` class:
    * inherits from `Base` (imported from `model_state`)
    * links to the MySQL table `cities`
    * class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    * class attribute `name` that represents a column of a string of 128 characters and can’t be null
    * class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to states.id`
* You must use the module `SQLAlchemy`

Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `cities.id`
* Results must be display as they are in the example below (`<state name>: (<city id>) <city name>`)
* Your code should not be executed when imported

File(s): [`model_city.py`](./model_city.py) [`14-model_city_fetch_by_state.py`](./14-model_city_fetch_by_state.py)

## Advanced Tasks

### :white_check_mark: 15. City relationship
Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`:
* `City` class:
    * No change
* `State` class:
    * In addition to previous requirements, the class attribute `cities` must represent a relationship with the class `City`. If the `State` object is deleted, all linked `City` objects must be automatically deleted. Also, the reference from a `City` object to his `State` should be named `state`
* You must use the module `SQLAlchemy`

Write a script that creates the State “California” with the `City` “San Francisco” from the database `hbtn_0e_100_usa`: (`100-relationship_states_cities.py`)
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* You must use the `cities` relationship for all `State` objects
* Your code should not be executed when imported

File(s): [`relationship_city.py`](./relationship_city.py) [`relationship_state.py`](./relationship_state.py) [`100-relationship_states_cities.py`](./100-relationship_states_cities.py)

### :white_check_mark: 16. List relationship
Write a script that lists all `State` objects, and corresponding `City` objects, contained in the database `hbtn_0e_101_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* The connection to your MySQL server must be to `localhost` on port `3306`
* You must only use one query to the database
* You must use the `cities` relationship for all `State` objects
* Results must be sorted in ascending order by `states.id` and `cities.id`
* Your code should not be executed when imported
```
<state id>: <state name>
<tabulation><city id>: <city name>
```

File(s): [`101-relationship_states_cities_list.py`](./101-relationship_states_cities_list.py)

### :white_check_mark: 17. From city
Write a script that lists all `City` objects from the database `hbtn_0e_101_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* You must use only one query to the database
* You must use the `state` relationship to access to the `State` object linked to the `City` object
* Results must be sorted in ascending order by `cities.id`
* Your code should not be executed when imported
```
<city id>: <city name> -> <state name>
```

File(s): [`102-relationship_cities_states_list.py`](./102-relationship_cities_states_list.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
