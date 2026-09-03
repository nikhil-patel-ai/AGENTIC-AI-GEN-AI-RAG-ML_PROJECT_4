# Python Functions

## Overview

A function is a reusable block of Python code that performs a specific task. Functions help you:

- Avoid repeating the same code
- Organize a program into smaller parts
- Improve readability and maintenance
- Accept input through parameters
- Send results back with `return`

This notebook demonstrates how to define and call functions, use parameters, return one or more values, and pass different types of arguments.

---

## Table of Contents

1. [Creating and Calling Functions](#1-creating-and-calling-functions)
2. [Function Naming Rules](#2-function-naming-rules)
3. [Indentation and Function Body](#3-indentation-and-function-body)
4. [Parameters and Arguments](#4-parameters-and-arguments)
5. [Printing Versus Returning a Value](#5-printing-versus-returning-a-value)
6. [Returning Multiple Values](#6-returning-multiple-values)
7. [Types of Function Arguments](#7-types-of-function-arguments)
8. [Common Errors](#8-common-errors)
9. [Best Practices](#9-best-practices)
10. [Practice Exercises](#10-practice-exercises)

---

# 1. Creating and Calling Functions

## What Is a Function?

A function is defined once and can be executed whenever it is called. Python uses the `def` keyword to define a function.

### Defining a Function

```python
def greet():
    print('good evening team')
```

### Line-by-Line Explanation

- `def`: Keyword used to begin a function definition.
- `greet`: Name of the function.
- `()`: Parentheses hold parameters. This function has no parameters.
- `:`: Marks the beginning of the function body.
- `print('good evening team')`: The indented statement that runs when the function is called.

Defining a function does not execute its body immediately. It only creates the function.

### Calling a Function

```python
def greet():
    print('good evening team')

greet()
```

### Line-by-Line Explanation

- The first three lines define the function.
- `greet()`: Calls the function and runs its body.
- Output:

```text
good evening team
```

The parentheses are required when calling a function. Writing only `greet` refers to the function object; writing `greet()` executes it.

---

# 2. Function Naming Rules

Function names follow the same rules as variable names in Python.

## Valid Names

```python
calculate_sum()
_private_function()
myFunction2()
```

### Explanation

- A name may start with a letter or an underscore.
- A name may contain letters, numbers, and underscores.
- A name cannot contain spaces or punctuation such as `-`.
- A name cannot start with a number.
- Function names are case-sensitive. `myFunction` and `myfunction` are different names.
- Python naming convention generally uses `snake_case`, such as `calculate_sum`.

## Function Comments

```python
def greet():  # Declare the function name
    print('good evening team')

greet()  # Call the function
```

- The comment after `def greet():` describes the definition.
- The indented `print()` statement is the function body.
- The final `greet()` statement executes the function.

---

# 3. Indentation and Function Body

Python uses indentation to identify the statements belonging to a function.

## Correct Indentation

```python
def greet():
    print('good evening team')

greet()
```

- The `print()` statement is indented by four spaces.
- The call to `greet()` is not indented, so it is outside the function.

## Incorrect Indentation

```python
def greet():
print('good evening team')
```

This causes an `IndentationError` because Python expects an indented function body after the colon.

## One-Space Indentation

```python
def greet():
 print('good evening team')
```

This may run because Python only requires consistent indentation within the block. However, four spaces are the standard and recommended style.

## Multiple Statements in a Function

```python
def greet():
    print('good evening team')
    print('bye')

greet()
```

### Explanation

- Both `print()` statements are indented, so both belong to `greet()`.
- They execute from top to bottom when `greet()` is called.
- Output:

```text
good evening team
bye
```

## Redefining a Function

```python
def greet():
    print('good evening team')

greet()

def greet():
    print('good evening team')

greet()
```

A later definition with the same name replaces the earlier definition. In normal programs, each function should usually have a unique, meaningful name.

---

# 4. Parameters and Arguments

Parameters allow a function to receive data.

```python
def add(x, y):
    c = x + y
    print(c)

add(5, 6)
```

### Line-by-Line Explanation

- `def add(x, y):`: Defines a function named `add` with two parameters: `x` and `y`.
- `c = x + y`: Adds the values received by the function and stores the result in `c`.
- `print(c)`: Displays the result.
- `add(5, 6)`: Calls the function with two values.
- During the call, `x` receives `5` and `y` receives `6`.
- Output: `11`

## Parameter and Argument Terminology

- **Parameter**: A variable listed in the function definition, such as `x` and `y`.
- **Argument**: A value supplied when calling the function, such as `5` and `6`.
- Parameters receive arguments when the function runs.

## Number of Arguments Must Match

```python
def add(x, y):
    c = x + y
    print(c)

add(5, 6, 7, 8)
```

This raises a `TypeError` because the function expects two arguments but receives four.

```python
def add(x, y, z):
    c = x + y
    print(c)

add(5, 6)
```

This also raises a `TypeError` because the required parameter `z` was not supplied. A function call must provide every required parameter exactly once, unless default or variable-length arguments are used.

---

# 5. Printing Versus Returning a Value

## A Function That Prints

```python
def add(x, y):
    c = x + y
    print(c)

r = add(5, 6)
print(r)
print(type(r))
```

### Explanation

- `add(5, 6)` calculates and prints `11`.
- The function has no `return` statement.
- Python automatically returns `None` when a function finishes without returning a value.
- `r` therefore contains `None`.
- `print(type(r))` displays `<class 'NoneType'>`.

Printing a result shows it on the screen, but does not make it available to the calling code.

## A Function That Returns

```python
def add(x, y):
    c = x + y
    return c

r = add(5, 6)
print(r)
print(type(r))
```

### Line-by-Line Explanation

- `def add(x, y):`: Defines a function with two parameters.
- `c = x + y`: Calculates the sum.
- `return c`: Sends the value of `c` back to the caller and stops the function.
- `r = add(5, 6)`: Stores the returned value in `r`.
- `print(r)`: Displays `11`.
- `print(type(r))`: Displays `<class 'int'>`.

## Main Difference

| `print()` | `return` |
|---|---|
| Displays a value | Sends a value back to the caller |
| Mainly used for output | Used for reuse in later calculations |
| Does not provide a useful result to assignment | Can be stored in a variable |
| A function using only `print()` returns `None` | A function can return any Python object |

## Combining Functions

```python
def add(x, y):
    return x + y

def greet():
    print('good evening team')

greet()
add(5, 6)
```

- `add()` returns a value, but the returned value is not printed or stored in this example.
- To display it, use `print(add(5, 6))` or assign it to a variable.

---

# 6. Returning Multiple Values

Python can return multiple values from one function. Internally, Python packages them into a tuple.

## Returning Two Values

```python
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d

r = greet()
r1 = add_sub(5, 6)

print(r)
print(r1)
print(type(r))
print(type(r1))
```

### Explanation

- `add_sub(x, y)`: Defines a function with two parameters.
- `c = x + y`: Calculates the sum.
- `d = x - y`: Calculates the difference.
- `return c, d`: Returns two values as the tuple `(11, -1)`.
- `r1 = add_sub(5, 6)`: Stores the complete tuple in `r1`.
- `type(r1)`: Is `<class 'tuple'>`.

The `greet()` function returns the string `'hello'`, so `r` has type `str`.

## Unpacking Two Returned Values

```python
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d

r1, r2 = add_sub(5, 6)

print(r1)
print(r2)
```

### Explanation

- `add_sub(5, 6)` returns `(11, -1)`.
- `r1, r2 = ...` unpacks the tuple.
- `r1` receives `11`.
- `r2` receives `-1`.

The number of variables on the left must match the number of returned values.

## Returning Three Values

```python
def add_sub_mul(x, y):
    c = x + y
    d = x - y
    e = x * y
    return c, d, e

r, r1, r2 = add_sub_mul(5, 6)

print(r)
print(r1)
print(r2)
```

### Line-by-Line Explanation

- `c = x + y`: Calculates `11`.
- `d = x - y`: Calculates `-1`.
- `e = x * y`: Calculates `30`.
- `return c, d, e`: Returns `(11, -1, 30)`.
- `r, r1, r2 = ...`: Unpacks the three values into three variables.

Calling `add_sub_mul(5, 6)` without assignment returns the tuple directly. In a notebook, the tuple may be displayed as the cell output.

---

# 7. Types of Function Arguments

The notebook introduces these argument styles:

1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Variable-length positional arguments (`*args`)
5. Variable-length keyword arguments (`**kwargs`)

## 7.1 Positional Arguments

```python
def person(name, age):
    print(name)
    print(age)

person('nit', 23)
```

### Explanation

- `name` and `age` are parameters.
- The first argument, `'nit'`, is assigned to `name`.
- The second argument, `23`, is assigned to `age`.
- Output:

```text
nit
23
```

Position matters with positional arguments.

```python
person(23, 'nit')
```

This call is syntactically valid, but the values are assigned in the opposite order. If the function performs `age + 1`, it causes a `TypeError` because `age` contains the string `'nit'`.

### Incorrect Argument Counts

```python
person('nit')
person('nit', 23, 24)
```

- The first call is missing the `age` argument.
- The second call supplies one extra argument.
- Both calls raise `TypeError`.

## 7.2 Keyword Arguments

```python
def person(name, age):
    print(name)
    print(age + 1)

person(age=23, name='nit')
```

### Explanation

- `age=23` explicitly assigns `23` to `age`.
- `name='nit'` explicitly assigns `'nit'` to `name`.
- Keyword arguments do not depend on their order.
- The output is:

```text
nit
24
```

### Positional Arguments Cannot Follow Keyword Arguments

```python
def person(name, age, mob):
    print(name)
    print(age + 1)
    print(mob)

person(age=23, name='nit', 2345)
```

This is invalid syntax because a positional argument appears after keyword arguments. Use `mob=2345` instead.

### Keyword Names Are Case-Sensitive

```python
person(age=23, name='nit', mob=2345, Addr='hyd')
```

If the parameter is named `addr`, then `Addr` is a different name and causes a `TypeError`. Python uses exact spelling and capitalization.

Correct form:

```python
person(age=23, name='nit', mob=2345, addr='hyd')
```

## 7.3 Default Arguments

A default argument provides a value when the caller does not provide one.

### Missing Required Argument

```python
def person(name, age):
    print(name)
    print(age)

person('vote')
```

This raises a `TypeError` because `age` is required and has no default value.

### Providing a Default Value

```python
def person(name, age=18):
    print(name)
    print(age)

person('vote')
```

### Line-by-Line Explanation

- `name`: Required parameter.
- `age=18`: Optional parameter with a default value of `18`.
- `person('vote')`: Supplies only `name`.
- Python automatically uses `18` for `age`.
- Output:

```text
vote
18
```

A supplied value overrides the default:

```python
person('vote', 21)
```

This prints `vote` and `21`.

## 7.4 Variable-Length Positional Arguments

The notebook lists variable-length arguments as a topic. The standard syntax is `*args`.

```python
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all(1, 2, 3, 4))
```

### Explanation

- `*numbers`: Collects any number of positional arguments into a tuple.
- `total = 0`: Creates an accumulator.
- The `for` loop visits each supplied number.
- `total += number`: Adds each number to the total.
- The function returns `10`.

## 7.5 Variable-Length Keyword Arguments

The standard syntax is `**kwargs`.

```python
def show_details(**details):
    for key, value in details.items():
        print(key, value)

show_details(name='Nit', age=23, city='Hyderabad')
```

### Explanation

- `**details`: Collects keyword arguments into a dictionary.
- `details.items()`: Provides each key-value pair.
- The loop prints every supplied detail.

## Combining Argument Styles

```python
def profile(name, age=18, *skills, **details):
    print(name)
    print(age)
    print(skills)
    print(details)
```

In a function definition, required parameters come first, followed by default parameters, `*args`, and `**kwargs` according to Python's argument rules.

---

# 8. Common Errors

## `IndentationError`

Cause: The function body is not indented.

```python
def greet():
print('hello')
```

Fix:

```python
def greet():
    print('hello')
```

## `TypeError: missing required argument`

Cause: Too few arguments were supplied.

```python
def add(x, y):
    return x + y

add(5)
```

Fix: Supply both arguments or define a default value.

## `TypeError: too many arguments`

Cause: More arguments were supplied than the function accepts.

```python
add(5, 6, 7)
```

## `TypeError` from Wrong Types

```python
def person(name, age):
    print(age + 1)

person(23, 'nit')
```

The value assigned to `age` is a string, so Python cannot add `1` to it.

## `NameError`

Cause: Calling a function with a different spelling or capitalization.

```python
def greet():
    print('hello')

greeted()
```

Fix: Call the function using its exact defined name: `greet()`.

## `None` Result

Cause: A function prints a value but does not return it.

```python
def add(x, y):
    print(x + y)

result = add(2, 3)
print(result)  # None
```

Fix: Use `return x + y` when the result must be reused.

---

# 9. Best Practices

1. Use descriptive names such as `calculate_total()` rather than unclear names.
2. Use four spaces for indentation.
3. Keep each function focused on one task.
4. Use `return` when a result must be reused.
5. Use parameters instead of hard-coding values.
6. Prefer `snake_case` for function names: `calculate_sum()`.
7. Keep argument order clear and consistent.
8. Use keyword arguments when they improve readability.
9. Use default values only when the default is meaningful.
10. Avoid redefining the same function name unnecessarily.
11. Add a docstring to functions that need explanation.

### Example of a Clean Function

```python
def calculate_sum(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number

result = calculate_sum(5, 6)
print(result)
```

### Line-by-Line Explanation

- `def calculate_sum(...):`: Defines a function with descriptive parameter names.
- The triple-quoted text is a docstring describing the function.
- `return first_number + second_number`: Calculates and returns the sum.
- `result = ...`: Stores the returned value.
- `print(result)`: Displays `11`.

---

# 10. Practice Exercises

1. Write a function named `square()` that returns the square of a number.
2. Write a function named `is_even()` that returns `True` for even numbers.
3. Create a function that accepts a name and prints a greeting.
4. Create a function that returns the sum, difference, and product of two numbers.
5. Rewrite the `person()` function using keyword arguments.
6. Create a function with a default country value such as `country='India'`.
7. Write a `sum_all(*numbers)` function that accepts any number of numbers.
8. Write a `display_profile(**details)` function that prints a user's details.
9. Test what happens when a required argument is missing.
10. Compare a function that uses `print()` with one that uses `return`.

---

## Quick Reference

```python
# Define a function
def greet():
    print('Hello')

# Call a function
greet()

# Define parameters and return a value
def add(first, second):
    return first + second

# Store a returned value
result = add(2, 3)

# Return multiple values
def operations(first, second):
    return first + second, first - second

sum_result, difference = operations(8, 3)

# Default argument
def greet_user(name, message='Hello'):
    return f'{message}, {name}'

# Variable-length arguments
def total(*numbers):
    return sum(numbers)

# Variable-length keyword arguments
def details(**values):
    return values
```

## Conclusion

Functions are one of the most important building blocks in Python. Define a function with `def`, place its statements inside an indented body, call it with parentheses, pass data through parameters, and use `return` when the caller needs a result. Understanding argument types and common errors makes functions easier to write, reuse, and debug.

**Notebook:** `Python_Function.ipynb`
