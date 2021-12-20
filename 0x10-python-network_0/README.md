# (299) 0x10. Python - Network #0
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
08-18-2020 to 08-19-2020

### Description
Introduction to the basics of HTTP requests and responses, URLs and their components, and using `curl` from the command line.

### Provided File(s)
* [`6-main.py`](./tests/6-main.py)

---

## Mandatory Tasks

### :white_check_mark: 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
* The size must be displayed in bytes
* You have to use `curl`

File(s): [`0-body_size.sh`](./0-body_size.sh)

### :white_check_mark: 1. cURL to the end
Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
* Display only body of a 200 status code response
* You have to use `curl`

File(s): [`1-body.sh`](./1-body.sh)

### :white_check_mark: 2. cURL Method
Write a Bash script that sends a `DELETE` request to the URL passed as the first argument, and displays the body of the response
* You have to use `curl`

File(s): [`2-delete.sh`](./2-delete.sh)

### :white_check_mark: 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
* You have to use `curl`

File(s): [`3-methods.sh`](./3-methods.sh)

### :white_check_mark: 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
* A header variable `X-School-User-Id` must be sent with the value 98
* You have to use `curl`

File(s): [`4-header.sh`](./4-header.sh)

### :white_check_mark: 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
* A variable `email` must be sent with the value `test@gmail.com`
* A variable `subject` must be sent with the value `I will always be here for PLD`
* You have to use `curl`

File(s): [`5-post_params.sh`](./5-post_params.sh)

### :white_large_square: 6. Find a peak
**Technical interview preparation**:
* You are not allowed to google anything
* Whiteboard first

Write a function that finds a peak in a list of unsorted integers.
* Prototype: `def find_peak(list_of_integers):`
* You are not allowed to import any module
* Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
* `6-peak.py` must contain the function
* `6-peak.txt` must contain the complexity of your algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`
* Note: there may be more than one peak in the list

File(s): [`6-peak.py`](./6-peak.py) [`6-peak.txt`](./6-peak.txt)

## Advanced Tasks

### :white_check_mark: 7. Only status code
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
* You are not allowed to use any pipe, redirection, etc.
* You are not allowed to use `;` and `&&`
* You have to use `curl`

File(s): [`100-status_code.sh`](./100-status_code.sh)

### :white_check_mark: 8. cURL a JSON file
Write a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
* Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
* You have to use `curl`

File(s): [`101-post_json.sh`](./101-post_json.sh)

### :white_check_mark: 9. Catch me if you can!
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
* You have to use `curl`
* You are not allow to use `echo`, `cat`, etc. to display the final result

File(s): [`102-catch_me.sh`](./102-catch_me.sh)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
