# Python Operators

This README explains the `Operators.ipynb` notebook in detail and helps you learn the most important operator types used in Python programming.

## What you will learn

The notebook introduces operator categories and shows how each one works with beginner-friendly Python examples.

Topics covered:
- Arithmetic operators
- Assignment operators
- Comparison (relational) operators
- Logical operators
- Unary operators

## How to use this notebook

1. Open `Operators.ipynb` in VS Code or Jupyter Notebook.
2. Run each code cell from top to bottom.
3. Read the markdown explanation, then execute the example code.
4. Change values and expressions to see how results change.

## 1. What is an operator?

In Python, an operator is a symbol or keyword that performs an action on values or variables.
Operators let you calculate numbers, compare values, combine boolean expressions, and update variables.

The notebook organizes operators into the following groups:
- Arithmetic: math calculations
- Assignment: saving or updating values
- Comparison: comparing values
- Logical: combining boolean conditions
- Unary: operating on a single value

---

## 2. Arithmetic operators

Arithmetic operators perform standard mathematical calculations. They work on numeric values such as integers and floats.

Examples in the notebook:
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` floor division
- `%` modulus (remainder)
- `**` exponentiation

### Example explanation

In the notebook, the following values are used:
```python
a = 6
b = 4
```

- `a + b` returns `10`
- `a - b` returns `2`
- `a * b` returns `24`
- `a / b` returns `1.5` (division always returns a float)
- `a // b` returns `1` (floor division discards the fractional part)
- `a % b` returns `2` (remainder of the division)
- `a ** b` returns `1296` (6 raised to the power of 4)

### Notes
- Use `/` when you need a precise division result.
- Use `//` when you need an integer quotient.
- Use `%` when you need the remainder of a division.
- Use `**` for powers and exponentials.

---

## 3. Assignment operators

Assignment operators are used to store values in variables and to update existing values.

Examples in the notebook:
- `=` simple assignment
- `+=` add and assign
- `-=` subtract and assign
- `*=` multiply and assign
- `/=` divide and assign
- `:=` walrus operator

### Example explanation

In the notebook, these assignments are shown:
```python
a = 20
b = 59
print(a, b)
```
This stores the values `20` and `59` in variables `a` and `b`.

Then these shorthand updates are shown:
```python
aa = 3
aa += 5   # same as aa = aa + 5
```
The variable `aa` changes from `3` to `8`.

Similarly:
- `sa -= 10` changes `sa` from `58` to `48`
- `ma *= 5` changes `ma` from `9` to `45`
- `da /= 5` changes `da` from `45` to `9.0`

### Walrus operator

The notebook demonstrates the walrus operator:
```python
print(wo := 6)
```
This assigns `6` to `wo` and prints the same value in a single expression.

### Notes
- Use `=` for initial assignment.
- Use `+=`, `-=`, `*=`, and `/=` when you want to update a variable using its current value.
- The walrus operator `:=` is useful when you want to assign a value while also using it immediately.

---

## 4. Comparison (relational) operators

Comparison operators compare two values and return a boolean result: `True` or `False`.

Examples in the notebook:
- `==` equal
- `!=` not equal
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

### Example explanation

The notebook uses:
```python
a = 12
b = 21
```

- `a == b` is `False`
- `b == a` is `False`
- `a == a` is `True`
- `b != a` is `True`
- `a > b` is `False`
- `b > a` is `True`
- `a < b` is `True`
- `a >= b` is `False`
- `b >= a` is `True`
- `a <= a` is `True`

### Notes
- Comparison operators are often used in `if` statements and loops.
- They do not change values; they only compare them.
- The result is always a boolean: `True` or `False`.

---

## 5. Logical operators

Logical operators combine boolean values or expressions. They help build more complex conditions.

Examples in the notebook:
- `and` returns `True` only when both expressions are true.
- `or` returns `True` when at least one expression is true.
- `not` reverses the boolean value.

### Logical AND

Examples:
```python
print(False and False)
print(False and True)
print(True and False)
print(True and True)
```

`and` also uses short-circuit evaluation in Python, which means it stops as soon as the result is known.

Examples:
```python
print(5 and 10)   # returns 10 because both are truthy
print(0 and 10)   # returns 0 because the first value is falsy
```

### Logical OR

Examples:
```python
print(False or False)
print(False or True)
print(True or False)
print(True or True)
```

Additional examples:
```python
print(5 or 39)      # returns 5 because it is truthy
print(0 or 39)      # returns 39 because 0 is falsy
print(False or 56)  # returns 56
print(True or 45)   # returns True
```

### Logical NOT

Examples:
```python
print(not 5)   # returns False because 5 is truthy
print(not 0)   # returns True because 0 is falsy
```

### Notes
- `and` returns the first falsy operand, or the last operand if all are truthy.
- `or` returns the first truthy operand, or the last operand if all are falsy.
- `not` always returns a boolean value.
- In Python, many values are truthy or falsy; logical operators use that truthiness when evaluating expressions.

---

## 6. Unary operators

Unary operators act on a single operand. The notebook demonstrates the unary negative operator.

Examples:
```python
x = 5
print(-x)

y = -10
print(-y)
```

### Explanation
- `-x` changes `5` to `-5`.
- `-y` changes `-10` to `10`.

### Notes
- Unary negation flips the sign of a numeric value.
- It does not change the original variable unless you assign the result back to the variable.

---

## Suggested exercises

1. Change the values of `a` and `b` in arithmetic examples and predict each result.
2. Practice compound assignment operators with a new variable, such as `count = 10`.
3. Write simple `if` statements using comparison and logical operators.
4. Use `not` with boolean variables and check how results invert.

## Summary

This notebook gives you a solid foundation in Python operators. It explains how to perform calculations, update values, compare results, and combine conditions with clear examples.

Use the notebook to practice by editing code and observing how each operator behaves.
