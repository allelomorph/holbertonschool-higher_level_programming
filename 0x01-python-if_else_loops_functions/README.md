# (233) 0x01. Python - if/else, loops, functions
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
04-28-2020 to 04-29-2020

### Description
Introduction to functions and basic flow control in Python.

### Provided file(s)
* original incomplete versions of [`0-positive_or_negative.py`](./0-positive_or_negative.py) [`1-last_digit_py`](./1-last_digit_py)
* [`7-main.py`](./tests/7-main.py) [`8-main.py`](./tests/8-main.py) [`9-main.py`](./tests/9-main.py) [`10-main.py`](./tests/10-main.py) [`11-main.py`](./tests/11-main.py) [`12-main.py`](./tests/12-main.py) [`13-main.py`](./tests/13-main.py) [`101-main.py`](./tests/101-main.py)
* [`lists.h`](./lists.h) [`linked_lists.c`](./linked_lists.c) [`13-main.c`](./tests/13-main.c)

---

## Mandatory Tasks

### :white_check_mark: 0. Positive anything is better than negative nothing
```Python
import random
number = random.randint(-10, 10)
```
 will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
* The variable number will store a different value every time you will run this program
* The output of the program should be:
    * The number, followed by
        * if the number is greater than 0: is positive
        * if the number is 0: is zero
        * if the number is less than 0: is negative
    * followed by a new line

File(s): [`0-positive_or_negative.py`](./0-positive_or_negative.py)

### :white_check_mark: 1. The last digit
```Python
import random
number = random.randint(-10000, 10000)
```
will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
* The variable `number` will store a different value every time you will run this program
* The output of the program should be:
    * The string `Last digit of`, followed by
    * the number, followed by
    * the string `is`, followed by the last digit of `number`, followed by
        * if the last digit is greater than 5: the string `and is greater than 5`
        * if the last digit is 0: the string `and is 0`
        * if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
    * followed by a new line

File(s): [`1-last_digit.py`](./1-last_digit.py)

### :white_check_mark: 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

File(s): [`2-print_alphabet.py`](./2-print_alphabet.py)

### :white_check_mark: 3. When I was having that alphabet soup, I never thought that it would pay off
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
* Print all the letters except `q` and `e`
* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

File(s): [`3-print_alphabt.py`](./3-print_alphabt.py)

### :white_check_mark: 4. Hexadecimal printing
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal, formatted `<decimal> = 0x<hex>`
* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

File(s): [`4-print_hexa.py`](./4-print_hexa.py)

### :white_check_mark: 5. 00...99
Write a program that prints numbers from 0 to 99.
* Numbers must be separated by `,`, followed by a space
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 2 print functions with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

File(s): [`5-print_comb2.py`](./5-print_comb2.py)

### :white_check_mark: 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
Write a program that prints all possible different combinations of two digits.
* Numbers must be separated by `,`, followed by a space
* The two digits must be different
* 01 and 10 are considered the same combination of the two digits 0 and 1
* Print only the smallest combination of two digits
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 3 `print` functions with string format
* You can only use no more than 2 loops in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

File(s): [`6-print_comb3.py`](./6-print_comb3.py)

### :white_check_mark: 7. islower
Write a function that checks for lowercase character.
* Prototype: `def islower(c):`
* Returns `True` if c is lowercase
* Returns `False` otherwise
* You are not allowed to import any module
* You are not allowed to use `str.upper()` and `str.isupper()`
* Tips: [`ord()`](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

File(s): [`7-islower.py`](./7-islower.py)

### :white_check_mark: 8. To uppercase
Write a function that prints a string in uppercase followed by a new line.
* Prototype: `def uppercase(str):`
* You can only use no more than 2 `print` functions with string format
* You can only use one loop in your code
* You are not allowed to import any module
* You are not allowed to use `str.upper()` and `str.isupper()`
* Tips: [`ord()`](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

File(s): [`8-uppercase.py`](./8-uppercase.py)

### :white_check_mark: 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
Write a function that prints the last digit of a number.
* Prototype: `def print_last_digit(number):`
* Returns the value of the last digit
* You are not allowed to import any module

File(s): [`9-print_last_digit.py`](./9-print_last_digit.py)

### :white_check_mark: 
10. a + b
Write a function that adds two integers and returns the result.
* Prototype: `def add(a, b):`
* Returns the value of `a + b`
* You are not allowed to import any module

File(s): [`10-add.py`](./10-add.py)

### :white_check_mark: 11. a ^ b
Write a function that computes `a` to the power of `b` and return the value.
* Prototype: `def pow(a, b):`
* Returns the value of `a ^ b`
* You are not allowed to import any module

File(s): [`11-pow.py`](./11-pow.py)

### :white_check_mark: 12. Fizz Buzz
Write a function that prints the numbers from 1 to 100 separated by a space.
* For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
* For numbers which are multiples of both three and five print `FizzBuzz`.
* Prototype: `def fizzbuzz():`
* Each element should be followed by a space
* You are not allowed to import any module

File(s): [`12-fizzbuzz.py`](./12-fizzbuzz.py)

### :white_check_mark: 13. Insert in sorted linked list
**Technical interview preparation**:
* You are not allowed to google anything
* Whiteboard first

Write a function in C that inserts a number into a sorted singly linked list.
* Prototype: `listint_t *insert_node(listint_t **head, int number);`
* Return: the address of the new node, or `NULL` if it failed

File(s): [`13-insert_number.c`](./13-insert_number.c) [`lists.h`](./lists.h)
Compiled: `gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert`

## Advanced Tasks

### :white_check_mark: 14. Smile in the mirror
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
* You can only use one print function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

File(s): [`100-print_tebahpla.py`](./100-print_tebahpla.py)

### :white_check_mark: 15. Remove at position
rite a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).
* Prototype: `def remove_char_at(str, n):`
* You are not allowed to import any module

File(s): [`101-remove_char_at.py`](./101-remove_char_at.py)

### :white_check_mark: 16. ByteCode -> Python #2
Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
tips - [ByteCode](https://docs.python.org/3.4/library/dis.html)

File(s): [`102-magic_calculation.py`](./102-magic_calculation.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
