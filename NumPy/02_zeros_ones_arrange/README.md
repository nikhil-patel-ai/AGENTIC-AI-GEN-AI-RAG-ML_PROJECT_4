# NumPy Arrays: `zeros()`, `ones()`, and `arange()`

This lesson introduces practical NumPy tools for creating and initializing arrays. You will learn how NumPy stores values with a shared data type, how to generate numeric sequences, how to create arrays filled with zeros or ones, and how to generate random values for experiments and testing.

> Note: The NumPy function is named `arange()`, not `arrange()`.

## Learning Objectives

By the end of this lesson, you should be able to:

- Create one-dimensional NumPy arrays with `np.array()`.
- Inspect an array's type and data type with `type()` and `.dtype`.
- Understand automatic and explicit type conversion.
- Generate evenly spaced values with `np.linspace()`.
- Generate step-based sequences with `np.arange()`.
- Create zero-filled and one-filled arrays with `np.zeros()` and `np.ones()`.
- Control array shape and data type with `shape` and `dtype`.
- Generate random floating-point and integer arrays.
- Index a two-dimensional array to access a row.

## Prerequisites

You should be familiar with:

- Python lists and variables
- Basic numerical data types
- Function arguments
- Indexing and slicing
- Installing and importing Python packages

## Import NumPy

Use the conventional alias `np` when importing NumPy:

```python
import numpy as np
```

The alias keeps NumPy calls readable and makes it clear which library provides a function. Avoid `from numpy import *` in professional code because it can overwrite existing names and make the source of functions unclear.

## Creating an Array with `np.array()`

`np.array()` converts a Python sequence, such as a list, into a NumPy array.

```python
values = [0, 1, 2, 3, 4, 5]
array = np.array(values)

print(array)
print(type(values))
print(type(array))
```

Output:

```text
[0 1 2 3 4 5]
<class 'list'>
<class 'numpy.ndarray'>
```

A Python list and a NumPy array are different objects. NumPy arrays support efficient numerical operations and are designed for multidimensional data.

## Data Types and Automatic Conversion

A NumPy array normally stores one common data type for all of its elements. NumPy may promote values to a compatible type when the input contains mixed numeric types.

```python
integer_array = np.array([1, 2, 3, 4, 5])
print(integer_array)
print(integer_array.dtype)

mixed_array = np.array([1, 2, 3, 4, 5.9])
print(mixed_array)
print(mixed_array.dtype)
```

Because the second array contains a decimal value, NumPy converts the integer values to a floating-point type.

### Set the Data Type Explicitly

Pass `dtype` to request a specific type:

```python
float_array = np.array([1, 2, 3, 4, 5.9], dtype=float)
integer_array = np.array([1, 2, 3, 4, 5.6], dtype=int)

print(float_array)
print(integer_array)
```

Converting decimal values to `int` removes the fractional part; it does not round to the nearest integer. For example, `5.6` becomes `5`.

Use explicit dtypes when memory usage, precision, or compatibility with another library matters.

## `np.arange()`

`np.arange()` creates values at a regular interval. Its syntax is:

```python
np.arange(start, stop, step)
```

- `start` is the first value and defaults to `0`.
- `stop` is the upper boundary and is excluded.
- `step` is the difference between consecutive values and defaults to `1`.

```python
print(np.arange(5))
print(np.arange(5, 10))
print(np.arange(5, 100, 10))
print(np.arange(-20, 10, 5))
```

Output:

```text
[0 1 2 3 4]
[5 6 7 8 9]
[ 5 15 25 35 45 55 65 75 85 95]
[-20 -15 -10  -5   0   5]
```

The stop value is excluded, just like Python's built-in `range()`. For a descending sequence, provide a negative step:

```python
print(np.arange(10, 0, -2))
```

When the step is positive and `start` is greater than or equal to `stop`, the result is empty. A negative step is required for descending output.

### `arange()` or `linspace()`?

Use `arange()` when the step size is the important requirement. Use `linspace()` when the number of values, including the endpoints, is the important requirement.

## `np.linspace()`

`np.linspace(start, stop, number_of_values)` returns a specified number of evenly spaced values. By default, both endpoints are included.

```python
values = np.linspace(0, 16, 10)
print(values)
```

The result may contain decimal values because NumPy divides the interval into equal parts. The third argument means “generate 10 values,” not “use a step of 10.”

For numerical work, `linspace()` is often more predictable than `arange()` when decimal steps are involved.

## `np.zeros()`

`np.zeros()` creates an array filled with `0` values.

```python
vector = np.zeros(5)
print(vector)

integer_vector = np.zeros(5, dtype=int)
print(integer_vector)
```

Output:

```text
[0. 0. 0. 0. 0.]
[0 0 0 0 0]
```

The default dtype is usually a floating-point type. Specify `dtype=int` when integer values are required.

### Create Multidimensional Zero Arrays

Pass a tuple to define the shape. A shape of `(rows, columns)` creates a two-dimensional array:

```python
zeros_matrix = np.zeros((2, 3), dtype=int)
print(zeros_matrix)
```

Output:

```text
[[0 0 0]
 [0 0 0]]
```

Other examples include `np.zeros((2, 2))` for a 2-by-2 matrix and `np.zeros((10, 3), dtype=int)` for a 10-by-3 integer matrix.

## `np.ones()`

`np.ones()` creates an array filled with `1` values:

```python
ones_vector = np.ones(4)
print(ones_vector)

ones_matrix = np.ones((2, 3), dtype=int)
print(ones_matrix)
```

Output:

```text
[1. 1. 1. 1.]
[[1 1 1]
 [1 1 1]]
```

Like `zeros()`, `ones()` accepts either an integer length or a tuple describing the shape.

There are no standard NumPy functions named `np.two()` or `np.three()`. Use `np.full()` when every element should contain another constant:

```python
threes = np.full((2, 3), 3)
print(threes)
```

## Random Arrays

NumPy can generate random values for simulations, testing, and machine-learning experiments.

### Random Floating-Point Values

`np.random.rand()` returns values in the interval $[0, 1)$:

```python
random_values = np.random.rand(2, 3)
print(random_values)
```

The arguments specify the shape. `np.random.rand(2)` creates a one-dimensional array with two values, while `np.random.rand(2, 3)` creates two rows and three columns.

### Random Integers

`np.random.randint(low, high, size)` returns random integers from `low` inclusive to `high` exclusive.

```python
random_numbers = np.random.randint(2, 9, 4)
print(random_numbers)

random_matrix = np.random.randint(10, 40, size=(3, 3))
print(random_matrix)
```

The first example produces four integers from `2` through `8`. The second produces a 3-by-3 matrix with values from `10` through `39`.

For reproducible results, use a random generator with a seed:

```python
random_generator = np.random.default_rng(42)
random_numbers = random_generator.integers(10, 40, size=(3, 3))
print(random_numbers)
```

Using a local generator is preferred in modern NumPy code because it avoids changing global random state.

## Array Shape and Indexing

The `.shape` attribute describes the size of each dimension. NumPy uses zero-based indexing.

```python
matrix = np.random.randint(10, 40, size=(10, 10))

print(matrix.shape)
print(matrix[5])
print(matrix[5, 2])
```

- `matrix.shape` returns `(10, 10)`.
- `matrix[5]` returns the sixth row.
- `matrix[5, 2]` returns the value at the sixth row and third column.

## Choosing the Right Function

| Function | Best used for | Stop or endpoint behavior |
| --- | --- | --- |
| `np.array()` | Converting existing sequences | Uses the supplied values |
| `np.arange()` | Creating values with a known step | Stop value is excluded |
| `np.linspace()` | Creating a fixed number of evenly spaced values | Endpoints included by default |
| `np.zeros()` | Allocating zero-filled arrays | Shape controls the dimensions |
| `np.ones()` | Allocating one-filled arrays | Shape controls the dimensions |
| `np.full()` | Filling an array with any constant | Shape controls the dimensions |
| `np.random.rand()` | Random floats from 0 up to 1 | Upper bound is excluded |
| `np.random.randint()` | Random integers in a range | High value is excluded |

## Common Mistakes

- Writing `arrange()` instead of NumPy's correct name, `arange()`.
- Assuming the stop value is included in `arange()` or `randint()`.
- Confusing the step argument of `arange()` with the count argument of `linspace()`.
- Forgetting that `np.zeros()` and `np.ones()` default to floating-point values.
- Passing `(rows, columns)` incorrectly and creating the wrong shape.
- Expecting integer conversion to round decimal values.
- Using `np.two()` or `np.three()`, which are not NumPy functions.
- Using `from numpy import *`, which makes code harder to read and maintain.
- Expecting random output to be identical between runs without setting a seed or generator.

## Best Practices

- Import NumPy as `np`.
- Use descriptive names such as `values`, `matrix`, and `random_generator`.
- Inspect `.shape` and `.dtype` when learning or debugging array behavior.
- Use `dtype` deliberately when creating arrays.
- Prefer `linspace()` for a fixed number of decimal samples.
- Prefer `default_rng()` for new random-number code.
- Use `size=(rows, columns)` to make random matrix dimensions explicit.
- Keep array shapes consistent with the downstream operation.

## Practice Exercises

1. Create an integer array containing the numbers from 10 through 50 in steps of 5.
2. Generate 8 evenly spaced values between `0` and `1` with `linspace()`.
3. Create a 3-by-4 zero matrix and a 3-by-4 one matrix with integer dtype.
4. Use `np.full()` to create a 2-by-5 matrix filled with `7`.
5. Generate a reproducible 4-by-4 matrix of random integers from `1` through `100`.
6. Inspect the shape, dtype, first row, and last column of a two-dimensional array.
7. Convert a list containing integers and floats into arrays with `dtype=float` and `dtype=int`, then compare the results.

## Summary

NumPy provides concise, efficient functions for constructing arrays. Use `np.array()` for existing data, `np.arange()` for step-based sequences, `np.linspace()` for a fixed number of evenly spaced values, and `np.zeros()`, `np.ones()`, or `np.full()` for initialized arrays. Add random-generation tools when you need test data, and always pay attention to shape, dtype, and endpoint behavior.
