# NumPy: First Code

NumPy is a Python library for numerical computing. Its main data structure, the `ndarray`, stores values in one or more dimensions and supports efficient mathematical operations.

This lesson introduces the first steps for creating and inspecting NumPy arrays.

## Learning Objectives

By the end of this lesson, you should be able to:

- Import NumPy using the standard alias `np`.
- Convert a Python list into a NumPy array.
- Create evenly spaced values with `np.arange()`.
- Create arrays filled with zeros or ones.
- Generate random floating-point and integer arrays.
- Create a matrix and access one of its rows.
- Choose an array data type with `dtype`.

## Prerequisites

You should be familiar with:

- Python variables and lists
- Function calls and arguments
- Basic indexing
- Running Python code in a notebook or terminal

## Installation

Install NumPy in the active Python environment if it is not already available:

```bash
python -m pip install numpy
```

## Import NumPy

Use the conventional `np` alias when importing NumPy.

```python
import numpy as np

print(np.__version__)
```

## Convert a List to an Array

A Python list can be converted into a NumPy array with `np.array()`.

```python
values = [0, 1, 2, 3, 4, 5]
array = np.array(values)

print(array)
print(type(array))
```

The result is a one-dimensional NumPy array. Unlike a list, an array is designed for numerical operations and has a consistent data type for its values.

## Create Ranges with `arange`

`np.arange(start, stop, step)` creates values from `start` up to, but not including, `stop`.

```python
print(np.arange(5))
print(np.arange(5, 10))
print(np.arange(5, 100, 10))
```

Output:

```text
[0 1 2 3 4]
[5 6 7 8 9]
[ 5 15 25 35 45 55 65 75 85 95]
```

The `stop` value is excluded. When using a positive step, the range must move toward a larger stop value. A negative step can be used to count backward.

## Create Arrays of Zeros and Ones

Use `np.zeros()` and `np.ones()` to create arrays with a chosen shape.

```python
print(np.zeros(5))
print(np.ones(4))
print(np.zeros((2, 3), dtype=int))
print(np.ones((2, 3), dtype=int))
```

The tuple `(2, 3)` creates an array with 2 rows and 3 columns. By default, zeros and ones use floating-point values. Use `dtype=int` when integer values are required.

## Generate Random Values

NumPy provides functions for generating random data.

```python
random_floats = np.random.rand(2, 3)
random_integers = np.random.randint(10, 40, size=(3, 3))

print(random_floats)
print(random_integers)
```

For `np.random.randint(low, high, size)`, `low` is included and `high` is excluded.

To make random results repeatable while learning or testing, set a seed before generating values:

```python
np.random.seed(7)
print(np.random.randint(2, 9, size=4))
```

## Create and Index a Matrix

A two-dimensional array can represent a matrix. The first index selects a row.

```python
matrix = np.random.randint(10, 40, size=(10, 10))

print(matrix)
print(matrix[5])
```

`matrix[5]` returns the sixth row because NumPy uses zero-based indexing.

## Common Array Properties

Inspect an array with these useful attributes:

```python
array = np.zeros((2, 3), dtype=int)

print(array.ndim)   # number of dimensions
print(array.shape)  # rows and columns
print(array.size)   # total number of values
print(array.dtype)  # data type of the values
```

## Best Practices

- Use `import numpy as np` consistently.
- Remember that the `stop` value in `np.arange()` is excluded.
- Use `size=(rows, columns)` to make matrix dimensions clear.
- Set `dtype` when the required numeric type matters.
- Set a random seed when results need to be reproducible.
- Use descriptive names such as `matrix`, `values`, and `random_integers`.

## Practice Exercises

1. Convert a list of temperatures into a NumPy array.
2. Create an array containing the even numbers from 2 through 20.
3. Create a 3 by 4 array of zeros with integer data type.
4. Generate five random integers from 1 through 100.
5. Create a 5 by 5 matrix of random integers from 10 through 40 and print its third row.
6. Inspect the `ndim`, `shape`, `size`, and `dtype` of each array you create.
