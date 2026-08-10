```markdown
# Python Data Types Notebook

This README explains the `DataTypes.ipynb` notebook in simple words with more details.

## What this notebook teaches

The notebook covers the main Python built-in data types:
- Numeric types
- Text type
- Sequence types
- Mapping type
- Set types
- Boolean and None types

It shows:
- how to create each type
- how to check its type
- how to print values
- beginner-friendly examples

## How to open and run

1. Open `DataTypes.ipynb` in VS Code or Jupyter Notebook.
2. Run each cell from top to bottom.
3. Read the text and check the code outputs.
4. Try changing values to learn faster.

## 1. Numeric Types

Numeric types are used for numbers.

### int
- Whole numbers without decimal points
- Example: `42`, `-10`, `0`

Example:
```python
i = 20
type(i)
```

### float
- Numbers with decimal points
- Example: `3.14`, `-0.5`

Example:
```python
f = 54.23
type(f)
```

### complex
- Numbers with a real and imaginary part
- The imaginary part uses `j` or `J`
- Example: `2 + 3j`

Example:
```python
c = 4 + 3j
type(c)
```

Note: `2 + 3k` is invalid because Python only accepts `j` or `J` for imaginary numbers.

## 2. Text Type

### str
- Text values stored in quotes
- Use single quotes, double quotes, or triple quotes
- Example: `'Hello'`, `"Hello"`, `'''Hello'''`

Examples:
```python
str1 = 'Welcome'
print(str1)
type(str1)
```

```python
s2 = "This is a double quotes string"
print(s2)
type(s2)
```

```python
s3 = '''This is a multiline string.
It can span multiple lines.'''
print(s3)
type(s3)
```

## 3. Sequence Types

Sequence types store items in order.

### list
- Ordered collection
- Mutable (can change)
- Can hold different data types
- Example: `[1, "apple", True]`

Example:
```python
l = [1, "apple", True]
print(type(l))
print(l)
```

### tuple
- Ordered collection
- Immutable (cannot change after creation)
- Example: `(3, "Mango", False)`

Example:
```python
t = (10.5, 20.3)
print(t)
type(t)
```

### range
- Immutable sequence of numbers
- Useful for loops
- Example: `range(1, 10)`

Example:
```python
r = range(1, 10)
print(r)
print(type(r))
```

## 4. Mapping Type

### dict
- Stores data as key-value pairs
- Keys must be unique
- Example: `{"name": "Alice", "age": 25}`

Example:
```python
d = {"id": 101, "role": "admin"}
type(d)
```

## 5. Set Types

Set types are unordered and store unique values.

### set
- Unordered collection
- Duplicate values are removed
- Example: `{101, 102, 103}`

Example:
```python
s = {101, 102, 103}
print(s)
print(type(s))
```

### frozenset
- Immutable set
- Cannot change after creation

Example:
```python
fr = frozenset([1, 2, 3])
print(fr)
print(type(fr))
```

## 6. Boolean and None Types

### bool
- Only two values: `True` or `False`
- Used for logic and conditions

Example:
```python
b = True
print(b)
print(type(b))
```

### NoneType
- Represents no value
- Used for empty or missing data

Example:
```python
age = None
print(age)
print(type(age))
```

## Extra notes

- The notebook also shows simple boolean operations like `True + False`.
- Some cells demonstrate incorrect examples intentionally, for learning.
- You can edit the examples and run them again to understand the types better.

## Summary

This notebook is a beginner-friendly guide to Python data types. It helps you learn:
- how values are stored
- the difference between types
- basic Python coding with data types
