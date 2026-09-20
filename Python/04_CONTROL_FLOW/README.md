# Python Conditional Statements

Conditional statements allow a Python program to make decisions. They evaluate a condition and execute the code block that matches the result.

This lesson introduces the core decision-making structures in Python:

- `if`
- `if...else`
- `if...elif...else`
- Nested `if` statements

## Learning Objectives

By the end of this lesson, you should be able to:

- Write conditions using comparison and logical operators.
- Choose between `if`, `else`, and `elif`.
- Combine conditions to solve practical problems.
- Use indentation to define Python code blocks.
- Build simple programs that respond to different inputs.

## Prerequisites

You should be familiar with:

- Variables and basic data types
- Boolean values: `True` and `False`
- Comparison operators
- Running Python code in a notebook or terminal

## The `if` Statement

An `if` statement runs its indented code block only when the condition is true.

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

Output:

```text
You are eligible to vote.
```

Python uses indentation to identify the statements controlled by the condition. Use consistent four-space indentation.

## The `if...else` Statement

Use `else` to provide an alternative when the `if` condition is false.

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

The `%` operator returns the remainder after division. A number with a remainder of `0` when divided by `2` is even.

## The `if...elif...else` Statement

Use `elif` when there are several possible conditions. Python checks the conditions from top to bottom and executes the first matching block.

```python
score = 80

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Needs improvement"

print(grade)
```

## Nested Conditional Statements

A nested conditional is an `if` statement inside another `if` statement. Use it when a decision depends on an earlier decision.

```python
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown user")
```

For deeply nested logic, consider using logical operators or separate functions to keep the code readable.

## Common Operators in Conditions

| Operator | Meaning | Example |
| --- | --- | --- |
| `==` | Equal to | `x == 10` |
| `!=` | Not equal to | `x != 10` |
| `>` | Greater than | `x > 10` |
| `<` | Less than | `x < 10` |
| `>=` | Greater than or equal to | `x >= 10` |
| `<=` | Less than or equal to | `x <= 10` |
| `and` | Both conditions must be true | `age >= 18 and has_id` |
| `or` | At least one condition must be true | `is_student or is_teacher` |
| `not` | Reverses a Boolean result | `not is_closed` |

Example using logical operators:

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")
```

## Truthy and Falsy Values

Python treats some values as false in a condition, including:

- `False`
- `None`
- `0`
- An empty string: `""`
- An empty list, tuple, set, or dictionary

```python
name = "Nikhil"

if name:
    print(f"Hello, {name}!")
else:
    print("Name is missing")
```

## Best Practices

- Use clear, descriptive variable names.
- Keep conditions short and readable.
- Use `elif` instead of several separate `if` statements when only one branch should run.
- Avoid unnecessary nesting.
- Compare values directly instead of writing `if value == True`.
- Keep all statements in a block at the same indentation level.

## Practice Exercises

1. Check whether a number is positive, negative, or zero.
2. Print whether a person is a child, teenager, adult, or senior based on age.
3. Create a program that converts a score into a grade.
4. Check whether a year is a leap year.
5. Create a simple login check using a username and password.

## Notebook

Practice these concepts in the companion notebook:

[Open ConditionalStatement.ipynb](ConditionalStatement.ipynb)

## Quick Reference

```python
if condition:
    # runs when condition is true
    pass
elif another_condition:
    # runs when the first condition is false
    # and this condition is true
    pass
else:
    # runs when all previous conditions are false
    pass
```
