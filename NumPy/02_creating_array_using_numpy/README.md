# Creating Arrays in NumPy

This section focuses on creating arrays using NumPy, which is one of the most important basics in numerical computing.

## What is an Array?

An array is a collection of elements stored in a single variable. In NumPy, arrays are used to store numeric data efficiently.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

Output:

```text
[1 2 3 4 5]
```

---

## Why Use NumPy Arrays?

NumPy arrays are useful because:

- They are faster than Python lists for numerical work
- They support multi-dimensional data
- They allow mathematical operations on entire arrays
- They are widely used in data science and machine learning

---

## Creating Arrays

### 1. From a Python list

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)
```

### 2. Creating a 2D array

```python
import numpy as np

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

### 3. Creating arrays with zeros

```python
import numpy as np

zeros = np.zeros((2, 3))
print(zeros)
```

Output:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

### 4. Creating arrays with ones

```python
import numpy as np

ones = np.ones((3, 2))
print(ones)
```

### 5. Creating arrays with a range of values

```python
import numpy as np

arr = np.arange(10)
print(arr)
```

Output:

```text
[0 1 2 3 4 5 6 7 8 9]
```

---

## Important Array Concepts

### Shape
The shape tells us the number of rows and columns in the array.

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
print(arr.shape)
```

Output:

```text
(2, 2)
```

### Dimension
The dimension tells how many axes the array has.

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr.ndim)
```

Output:

```text
1
```

### Data Type
NumPy arrays can store different datatypes such as integers, floats, and strings.

```python
import numpy as np

arr = np.array([1, 2, 3], dtype=float)
print(arr)
```

---

## Typical Use Cases

NumPy arrays are used for:

- Storing large datasets
- Mathematical calculations
- Matrix operations
- Image processing
- Machine learning inputs
- Scientific research

---

## Summary

This lesson introduces the basic ways to create NumPy arrays and understand their structure. Once you learn these fundamentals, you can move on to slicing, indexing, reshaping, and advanced numerical operations.

---

## Next Topics

After this section, you can continue with:

- Array indexing
- Array slicing
- Reshaping arrays
- Data types in NumPy
- Mathematical operations with arrays

---

## Reference

NumPy Official Documentation: https://numpy.org/doc/
