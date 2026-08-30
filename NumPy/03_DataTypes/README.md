# NumPy Data Types

This section explains the different data types available in NumPy and how they are used when working with arrays.

## Introduction

In Python, variables can store different kinds of data such as integers, floats, strings, or booleans. NumPy arrays are also designed to store data efficiently, and each element in a NumPy array has a specific data type.

NumPy data types are important because they decide:

- how much memory an array uses
- how values are stored
- how calculations are performed
- whether operations are fast and efficient

---

## Why Data Types Matter in NumPy

When you create an array using NumPy, Python does not store values as generic objects. Instead, it stores them in a specific dtype (data type).

For example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)
```

Output:

```text
int32
```

This means the array stores integers in a 32-bit format.

---

## Common NumPy Data Types

NumPy supports many data types. Some of the most commonly used are:

### 1. int
Used for integers.

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr.dtype)
```

Output:

```text
int32
```

### 2. float
Used for decimal numbers.

```python
import numpy as np

arr = np.array([1.5, 2.7, 3.9])
print(arr.dtype)
```

Output:

```text
float64
```

### 3. complex
Used for numbers with real and imaginary parts.

```python
import numpy as np

arr = np.array([1 + 2j, 3 + 4j])
print(arr.dtype)
```

Output:

```text
complex128
```

### 4. bool
Used for boolean values, True or False.

```python
import numpy as np

arr = np.array([True, False, True])
print(arr.dtype)
```

Output:

```text
bool
```

### 5. str
Used for strings.

```python
import numpy as np

arr = np.array(['apple', 'banana', 'orange'])
print(arr.dtype)
```

Output:

```text
<U6
```

This indicates Unicode strings with a maximum length of 6 characters.

---

## Creating Arrays with Specific Data Types

You can explicitly define the data type while creating an array.

```python
import numpy as np

arr = np.array([1, 2, 3, 4], dtype=np.float64)
print(arr)
print(arr.dtype)
```

Output:

```text
[1. 2. 3. 4.]
float64
```

This is useful when you want to ensure numbers are stored as floats instead of integers.

---

## Converting Data Types

NumPy allows you to change the dtype of an existing array using `astype()`.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
new_arr = arr.astype(np.float64)

print(new_arr)
print(new_arr.dtype)
```

Output:

```text
[1. 2. 3. 4.]
float64
```

### Why use `astype()`?

It is useful when:

- you need floating-point precision
- you want to reduce memory usage
- you need compatibility with specific operations
- you need to convert booleans or integers to a different numeric format

---

## Important NumPy Numeric Types

NumPy provides several numeric dtypes.

### Integer Types

- `np.int8`
- `np.int16`
- `np.int32`
- `np.int64`

These store whole numbers with different memory sizes.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3], dtype=np.int8)
print(arr.dtype)
```

### Floating Types

- `np.float16`
- `np.float32`
- `np.float64`

These store decimal values with varying precision.

Example:

```python
import numpy as np

arr = np.array([1.2, 3.4], dtype=np.float32)
print(arr.dtype)
```

### Unsigned Integer Types

- `np.uint8`
- `np.uint16`
- `np.uint32`
- `np.uint64`

These are integers that cannot be negative.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30], dtype=np.uint8)
print(arr.dtype)
```

---

## Example: Mixed Data Types

If you create an array with a mix of strings and numbers, NumPy may convert everything to a string-like representation or raise an error depending on the values.

```python
import numpy as np

arr = np.array([1, '2', '3'])
print(arr)
print(arr.dtype)
```

This will often convert values to a string type because NumPy cannot store mixed types in a single numeric array.

---

## Checking Data Type

To check the data type of an array, use `.dtype`.

```python
import numpy as np

arr = np.array([10, 20, 30])
print(arr.dtype)
```

### Output

```text
int32
```

---

## Data Type Selection Guidelines

Choose the dtype based on the kind of values you are storing:

- Use `int` for whole numbers
- Use `float` for decimal numbers
- Use `bool` for true/false values
- Use `complex` for complex calculations
- Use `str` for text values

Choosing the right dtype helps in memory optimization and better performance.

---

## Memory and Performance Considerations

Data types affect memory usage.

Example:

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4], dtype=np.int8)
arr2 = np.array([1, 2, 3, 4], dtype=np.int64)

print(arr1.dtype, arr1.nbytes)
print(arr2.dtype, arr2.nbytes)
```

The `int64` version uses more memory than `int8` because it stores more bits per value.

This is important when working with large datasets.

---

## Summary

NumPy data types define how array elements are stored and handled.

Key points:

- Every NumPy array has a `dtype`
- Data type decides the kind of values stored
- You can create arrays with specific dtypes
- You can convert dtypes using `astype()`
- Choosing the correct dtype is important for memory and performance

---

## Practice Questions

1. What does `arr.dtype` return?
2. How do you create an array of floats?
3. How do you convert an integer array to a float array using `astype()`?
4. What is the difference between `int32` and `int64`?
5. Why is dtype important for memory usage?

---

## Next Topics

After learning data types, the next step is to study:

- array indexing
- array slicing
- reshaping arrays
- numerical operations on arrays
- broadcasting in NumPy

---

## Reference

NumPy official documentation: https://numpy.org/doc/
