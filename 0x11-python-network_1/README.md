# (300) 0x11. Python - Network #1
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
08-24-2020 to 08-25-2020

### Description
Continued exploration of the Pythonic approach to HTTP requests and responses, this time using the `urllib` and `requests` packages.

---

## Mandatory Tasks

### :white_check_mark: 0. What's my status? #0
Write a Python script that fetches `https://intranet.hbtn.io/status`
* You must use the package `urllib`
* You are not allowed to import any packages other than `urllib`
* The body of the response must be displayed like the following example (tabulation before `-`)
* You must use a `with` statement
```bash
$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
$ 
```

File(s): [`0-hbtn_status.py`](./0-hbtn_status.py)

### :white_check_mark: 1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
* You must use the packages `urllib` and `sys`
* You are not allow to import packages other than `urllib` and `sys`
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a `with` statement
```bash
$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
$ 
$ ./1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
$ 
```

File(s): [`1-hbtn_header.py`](./1-hbtn_header.py)

### :white_check_mark: 2. POST an email #0
Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`.)
* The email must be sent in the `email` variable
* You must use the packages `urllib` and `sys`
* You are not allowed to import packages other than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement
It is recommended to test your script in a container, using the a web server running on port 5000.
```bash
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
$ 
```

File(s): [`2-post_email.py`](./2-post_email.py)

### :white_check_mark: 3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`.)
* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
* You must use the packages `urllib` and `sys`
* You are not allowed to import other packages than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement
It is recommended to test your script in a container, using the a web server running on port 5000
```bash
$ ./3-error_code.py http://0.0.0.0:5000
Index
$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
$ 
```

File(s): [`3-error_code.py`](./3-error_code.py)

### :white_check_mark: 4. What's my status? #1
Write a Python script that fetches `https://intranet.hbtn.io/status`
* You must use the package `requests`
* You are not allow to import packages other than `requests`
* The body of the response must be display like the following example (tabulation before `-`)
```bash
$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
$ 
```

File(s): [`4-hbtn_status.py`](./4-hbtn_status.py)

### :white_check_mark: 5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
* You must use the packages `requests` and `sys`
* You are not allow to import other packages than `requests` and `sys`
* The value of this variable is different for each request
* You don’t need to check script arguments (number and type)
```bash
$ ./5-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
$ 
$ ./5-hbtn_header.py https://intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
$ 
```

File(s): [`5-hbtn_header.py`](./5-hbtn_header.py)

### :white_check_mark: 6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.
* The email must be sent in the variable `email`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to error check arguments passed to the script (number or type)
It is recommended to test your script in a container, using the a web server running on port 5000
```bash
$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
$ 
```

File(s): [`6-post_email.py`](./6-post_email.py)

### :white_check_mark: 7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
* If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)
It is recommended to test your script in a container, using the a web server running on port 5000
```bash
$ ./7-error_code.py http://0.0.0.0:5000
Index
$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
$ 
```

File(s): [`7-error_code.py`](./7-error_code.py)

### :white_check_mark: 8. Search API
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
* The letter must be sent in the variable `q`
* If no argument is given, set `q=""`
* If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
* Otherwise:
    * Display `Not a valid JSON` if the JSON is invalid
    * Display `No result` if the JSON is empty
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
It is recommended to test your script in a container, using the a web server running on port 5000
```bash
$ ./8-json_api.py 
No result
$ ./8-json_api.py a
[8446] amnirqhtfjq
$ ./8-json_api.py 2
No result
$ ./8-json_api.py b
[7094] bmofakakhke
$ 
```

File(s): [`8-json_api.py`](./8-json_api.py)

### :white_check_mark: 9. My GitHub!
Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/reference/users) to display your `id`
* You must use [Basic Authentication](https://docs.github.com/en/rest/overview/other-authentication-methods) with a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to access to your information (only `read:user` permission is needed)
* The first argument will be your `username`
* The second argument will be your `password` (in your case, a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)
```bash
$ ./10-my_github.py papamuziko cisfun
2531536
$ ./10-my_github.py papamuziko wrong_pwd
None
$ 
```
Note: project expects files that are misnumbered as task 10.

File(s): [`10-my_github.py`](./10-my_github.py)

## Advanced Tasks

### :white_check_mark: 10. Time for an interview!
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation `https://developer.github.com/v3/repos/commits/`
Print all commits by: `<sha>: <author name>` (one by line)
```
Write a Python script that takes 2 arguments in order to solve this challenge.
* The first argument will be the `repository name`
* The second argument will be the `owner name`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)
Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.
```bash
$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França
$ 
```
Be careful: only 60 requests by hour by IP for unauthenticated requests - see GitHub current rate limits.

File(s): [`100-github_commits.py`](./100-github_commits.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
