# (252) 0x09. Python - Everything is object
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
05-26-2020 to 05-27-2020

### Description
Investigating the mutability of objects in Python, comparing classes vs objects vs instances, and reference vs assignment vs aliases.

### Provided file(s)
* [`19-main.py`](./tests/19-main.py) [`100-main.py`](./tests/100-main.py) [`101-main.py`](./tests/101-main.py)

---

## Mandatory Tasks

### :white_check_mark: 0. Who am I?
What function would you use to print the type of an object?

Write the name of the function in the file, without `()`.

File(s): [`0-answer.txt`](./0-answer.txt)

### :white_check_mark: 1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

File(s): [`1-answer.txt`](./1-answer.txt)

### :white_check_mark: 2. Right count
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```python
>>> a = 89
>>> b = 100
```

File(s): [`2-answer.txt`](./2-answer.txt)

### :white_check_mark: 3. Right count =
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```python
>>> a = 89
>>> b = 89
```

File(s): [`3-answer.txt`](./3-answer.txt)

### :white_check_mark: 4. Right count =
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```python
>>> a = 89
>>> b = a
```

File(s): [`4-answer.txt`](./4-answer.txt)

### :white_check_mark: 5. Right count =+
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```python
>>> a = 89
>>> b = a + 1
```

File(s): [`5-answer.txt`](./5-answer.txt)

### :white_check_mark: 6. Is equal
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

File(s): [`6-answer.txt`](./6-answer.txt)

### :white_check_mark: 7. Is the same
What do these 3 lines print?
```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

File(s): [`7-answer.txt`](./7-answer.txt)

### :white_check_mark: 8. Is really equal
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

File(s): [`8-answer.txt`](./8-answer.txt)

### :white_check_mark: 9. Is really the same
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

File(s): [`9-answer.txt`](./9-answer.txt)

### :white_check_mark: 10. And with a list, is it equal
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

File(s): [`10-answer.txt`](./10-answer.txt)

### :white_check_mark: 11. And with a list, is it the same
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```

File(s): [`11-answer.txt`](./11-answer.txt)

### :white_check_mark: 12. And with a list, is it really equal
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

File(s): [`12-answer.txt`](./12-answer.txt)

### :white_check_mark: 13. And with a list, is it really the same
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

File(s): [`13-answer.txt`](./13-answer.txt)

### :white_check_mark: 14. List append
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

File(s): [`14-answer.txt`](./14-answer.txt)

### :white_check_mark: 15. List add
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

File(s): [`15-answer.txt`](./15-answer.txt)

### :white_check_mark: 16. Integer incrementation
What does this script print?
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

File(s): [`16-answer.txt`](./16-answer.txt)

### :white_check_mark: 17. List incrementation
What does this script print?
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

File(s): [`17-answer.txt`](./17-answer.txt)

### :white_check_mark: 18. List assignation
What does this script print?
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

File(s): [`18-answer.txt`](./18-answer.txt)

### :white_check_mark: 19. Copy a list object
Write a function `def copy_list(l):` that returns a **copy** of a list.
* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module

File(s): [`19-copy_list.py`](./19-copy_list.py)

### :white_check_mark: 20. Tuple or not?
```python
a = ()
```

Is a a tuple? Answer with `Yes` or `No`.

File(s): [`20-answer.txt`](./20-answer.txt)

### :white_check_mark: 21. Tuple or not?
```python
a = (1, 2)
```

Is a a tuple? Answer with `Yes` or `No`.

File(s): [`21-answer.txt`](./21-answer.txt)

### :white_check_mark: 22. Tuple or not?
```python
a = (1)
```

Is a a tuple? Answer with `Yes` or `No`.

File(s): [`22-answer.txt`](./22-answer.txt)

### :white_check_mark: 23. Tuple or not?
```python
a = (1, )
```

Is a a tuple? Answer with `Yes` or `No`.

File(s): [`23-answer.txt`](./23-answer.txt)

### :white_check_mark: 24. Who I am?
What does this script print?
```python
a = (1)
b = (1)
a is b
```

File(s): [`24-answer.txt`](./24-answer.txt)

### :white_check_mark: 25. Tuple or not
What does this script print?
```python
a = (1, 2)
b = (1, 2)
a is b
```

File(s): [`25-answer.txt`](./25-answer.txt)

### :white_check_mark: 26. Empty is not empty
What does this script print?
```python
a = ()
b = ()
a is b
```

File(s): [`26-answer.txt`](./26-answer.txt)

### :white_check_mark: 27. Still the same?
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

File(s): [`27-answer.txt`](./27-answer.txt)

### :white_check_mark: 28. Same or not?
```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

File(s): [`28-answer.txt`](./28-answer.txt)

### :white_large_square: 29. Python3: Mutable, Immutable... everything is object!
Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):
* introduction
* id and type
* mutable objects
* immutable objects
* why does it matter and how differently does Python treat mutable and immutable objects
* how arguments are passed to functions and what does that imply for mutable and immutable objects

*If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.*

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

<!--
https://www.linkedin.com/pulse/oop-python-samuel-pomeroy
https://www.linkedin.com/posts/activity-6671301903965679616-12_7
-->

## Advanced Tasks

### :white_check_mark: 30. #pythonic
Write a function `magic_string()` that returns a string `Holberton` n times, `, ` delimited, where n is the number of the iterator in the loop calling `magic_string()`:
* Your file should be maximum 4-line long (no documentation needed)
* You are not allowed to import any module

File(s): [`100-magic_string.py`](./100-magic_string.py)

### :white_check_mark: 31. Low memory cost
Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.
* You are not allowed to import any module

File(s): [`101-locked_class.py`](./101-locked_class.py)

### :white_check_mark: 32. int 1/3
```bash
$ cat int.py
a = 1
b = 1
$ 
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:
* How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)
* How many int objects are created by the execution of the second line of the script? (`103-line2.txt`)

File(s): [`103-line1.txt`](./103-line1.txt) [`103-line2.txt`](./103-line2.txt)

### :white_check_mark: 33. int 2/3
```bash
$ cat int.py
a = 1024
b = 1024
del a
del b
c = 1024
$ 
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:
* How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
* How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
* After the execution of line 3, is the int object pointed by `a` deleted? Answer with `Yes` or `No` (`104-line3.txt`)
* After the execution of line 4, is the int object pointed by `b` deleted? Answer with `Yes` or `No` (`104-line4.txt`)
* How many int objects are created by the execution of the last line of the script (`104-line5.txt`)

File(s): [`104-line1.txt`](./104-line1.txt) [`104-line2.txt`](./104-line2.txt) [`104-line3.txt`](./104-line3.txt) [`104-line4.txt`](./104-line4.txt) [`104-line5.txt`](./104-line5.txt)

### :white_check_mark: 34. int 3/3
```bash
$ cat int.py
print("I")
print("Love")
print("Python")
$ 
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:
* Before the execution of line 2 `(print("Love"))`, how many int objects have been created and are still in memory? (`105-line1.txt`)
* Why? (optional blog post)

Hint: `NSMALLPOSINTS`, `NSMALLNEGINTS`

File(s): [`105-line1.txt`](./105-line1.txt)

### :white_check_mark: 35. Clear strings
```bash
$ cat string.py
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
$ 
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:
* How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
* How many string objects are created by the execution of the second line of the script? (`106-line2.txt`)
* After the execution of line 3, is the string object pointed by `a` deleted? Answer with `Yes` or `No` (`106-line3.txt`)
* After the execution of line 4, is the string object pointed by `b` deleted? Answer with `Yes` or `No` (`106-line4.txt`)
* How many string objects are created by the execution of the last line of the script (`106-line5.txt`)

File(s): [`106-line1.txt`](./106-line1.txt) [`106-line2.txt`](./106-line2.txt) [`106-line3.txt`](./106-line3.txt) [`106-line4.txt`](./106-line4.txt) [`106-line5.txt`](./106-line5.txt)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
