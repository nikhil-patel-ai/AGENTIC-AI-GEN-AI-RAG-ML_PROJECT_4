# NumPy Array Attributes & Functions

This notebook covers essential NumPy array attributes that provide information about array structure, size, and memory usage. Understanding these attributes is fundamental for working with arrays effectively.

---

## Introduction

When working with NumPy arrays, you often need to understand their properties:
- How many dimensions they have
- What their shape is
- How many elements they contain
- How much memory they use

This notebook explores the key attributes that answer these questions.

---

## Array Types Covered

### 1. 1D Array (Vector)
```python
a1 = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
```
A linear sequence of elements.

### 2. 2D Array (Matrix)
```python
a2 = np.arange(12, dtype=float).reshape(3,4)
# [[0. 1. 2. 3.]
#  [4. 5. 6. 7.]
#  [8. 9. 10. 11.]]
```
A rectangular grid with rows and columns.

### 3. 3D Array (Tensor)
```python
a3 = np.arange(8).reshape(2,2,2)
# [[[0 1]
#   [2 3]]
#  [[4 5]
#   [6 7]]]
```
A multi-dimensional structure with depth.

---

## Array Attributes

### 1. ndim - Number of Dimensions

**What it is:**
The `ndim` attribute returns the number of dimensions (axes) of an array.

**Syntax:**
```python
array.ndim
```

**Return Value:**
An integer representing the number of dimensions.

**Examples:**

```python
a1 = np.arange(10)
print(a1.ndim)  # Output: 1
# 1D array has 1 dimension

a2 = np.arange(12, dtype=float).reshape(3,4)
print(a2.ndim)  # Output: 2
# 2D array (matrix) has 2 dimensions

a3 = np.arange(8).reshape(2,2,2)
print(a3.ndim)  # Output: 3
# 3D array (tensor) has 3 dimensions
```

**Terminology:**
- **1D array** = Vector
- **2D array** = Matrix
- **3D array** = Tensor
- **nD array** = Multidimensional array

**Use Cases:**
```python
# Check if array is 1D before certain operations
if array.ndim == 1:
    print("This is a vector")

# Handle different array dimensions differently
if array.ndim == 2:
    rows, cols = array.shape
else:
    print("Array is not 2D")
```

---

### 2. shape - Array Dimensions

**What it is:**
The `shape` attribute returns the dimensions of the array as a tuple. Each element in the tuple represents the size along that dimension.

**Syntax:**
```python
array.shape
```

**Return Value:**
A tuple of integers representing the size along each dimension.

**Examples:**

```python
a1 = np.arange(10)
print(a1.shape)  # Output: (10,)
# 1D array with 10 elements

a2 = np.arange(12, dtype=float).reshape(3,4)
print(a2.shape)  # Output: (3, 4)
# 3 rows and 4 columns

a3 = np.arange(8).reshape(2,2,2)
print(a3.shape)  # Output: (2, 2, 2)
# 2 blocks, each with 2 rows and 2 columns
```

**Shape Interpretation:**

| Array | Shape | Meaning |
|-------|-------|---------|
| 1D Vector | (10,) | 10 elements in a line |
| 2D Matrix | (3, 4) | 3 rows × 4 columns |
| 3D Tensor | (2, 2, 2) | 2 × 2 × 2 structure |
| 4D Array | (2, 3, 4, 5) | 2 × 3 × 4 × 5 structure |

**Shape Manipulation:**

```python
# Reshaping arrays
original = np.arange(12)  # shape: (12,)
reshaped = original.reshape(3, 4)  # shape: (3, 4)
reshaped_3d = original.reshape(2, 2, 3)  # shape: (2, 2, 3)

# Verifying shape compatibility
# Reshape requires: product of new dimensions = total elements
# (2, 2, 3) → 2 × 2 × 3 = 12 ✓
```

**Use Cases:**

```python
# Extract dimensions
rows, cols = array.shape  # For 2D arrays
print(f"Array has {rows} rows and {cols} columns")

# Verify expected dimensions
assert array.shape == (100, 50), "Array shape mismatch"

# Get last dimension (useful for processing)
last_dim = array.shape[-1]

# Check if array is square (2D only)
if len(array.shape) == 2 and array.shape[0] == array.shape[1]:
    print("This is a square matrix")
```

---

### 3. size - Total Number of Elements

**What it is:**
The `size` attribute returns the total number of elements in the array, which is the product of all dimensions.

**Syntax:**
```python
array.size
```

**Return Value:**
An integer representing the total number of elements.

**Formula:**
```
size = shape[0] × shape[1] × shape[2] × ... × shape[n-1]
```

**Examples:**

```python
a1 = np.arange(10)
print(a1.size)  # Output: 10
# 1D array: 10 elements

a2 = np.arange(12, dtype=float).reshape(3,4)
print(a2.size)  # Output: 12
# 2D array: 3 × 4 = 12 elements

a3 = np.arange(8).reshape(2,2,2)
print(a3.size)  # Output: 8
# 3D array: 2 × 2 × 2 = 8 elements
```

**Calculation Examples:**

| Array | Shape | Size Calculation | Size |
|-------|-------|------------------|------|
| Vector | (10,) | 10 | 10 |
| Matrix | (3, 4) | 3 × 4 | 12 |
| Tensor | (2, 2, 2) | 2 × 2 × 2 | 8 |
| 4D | (2, 3, 4, 5) | 2 × 3 × 4 × 5 | 120 |

**Use Cases:**

```python
# Allocate memory based on array size
required_memory = array.size * array.itemsize

# Flatten array and verify flattening
flat_array = array.flatten()
assert flat_array.size == array.size, "Flattening failed"

# Check if array is empty
if array.size == 0:
    print("Array is empty")

# Loop through all elements
for i in range(array.size):
    element = array.flat[i]  # Access via flat iterator
```

---

### 4. itemsize - Memory Per Element

**What it is:**
The `itemsize` attribute returns the size of each element in the array in bytes. This depends on the data type of the array.

**Syntax:**
```python
array.itemsize
```

**Return Value:**
An integer representing the number of bytes per element.

**Data Type to itemsize Mapping:**

| Data Type | itemsize (bytes) | Description |
|-----------|-----------------|-------------|
| int8 | 1 | 8-bit signed integer |
| int16 | 2 | 16-bit signed integer |
| int32 | 4 | 32-bit signed integer |
| int64 | 8 | 64-bit signed integer |
| float32 | 4 | 32-bit floating-point |
| float64 | 8 | 64-bit floating-point (default) |
| complex64 | 8 | 64-bit complex number |
| complex128 | 16 | 128-bit complex number |
| bool | 1 | Boolean value |

**Examples:**

```python
a1 = np.arange(10)  # default: int64
print(a1.itemsize)  # Output: 8 bytes

a2 = np.arange(12, dtype=float).reshape(3,4)  # float64
print(a2.itemsize)  # Output: 8 bytes

a3 = np.arange(8, dtype=np.int32).reshape(2,2,2)  # int32
print(a3.itemsize)  # Output: 4 bytes

a4 = np.array([1.5, 2.5, 3.5], dtype=np.float32)
print(a4.itemsize)  # Output: 4 bytes
```

**Total Memory Calculation:**

```python
total_memory = array.size * array.itemsize

# Example:
a2 = np.arange(12, dtype=float).reshape(3,4)
# size = 12, itemsize = 8 bytes
# total_memory = 12 × 8 = 96 bytes
print(f"Total memory: {a2.size * a2.itemsize} bytes")
print(f"Total memory: {(a2.size * a2.itemsize) / 1024} KB")
```

**Use Cases:**

```python
# Memory optimization - choose appropriate data type
# Instead of float64, use float32 if precision allows
a_float64 = np.arange(1000000, dtype=float)  # 8MB
a_float32 = np.arange(1000000, dtype=np.float32)  # 4MB

# Calculate total memory usage of multiple arrays
total_mem = sum(arr.size * arr.itemsize for arr in [a1, a2, a3])
print(f"Total memory used: {total_mem} bytes")

# Check data type from itemsize
if array.itemsize == 8 and array.dtype.kind == 'f':
    print("This is float64")
```

---

## Complete Example: Array Analysis

```python
import numpy as np

# Create sample arrays
arrays = {
    "1D Vector": np.arange(10),
    "2D Matrix": np.arange(12, dtype=float).reshape(3, 4),
    "3D Tensor": np.arange(8).reshape(2, 2, 2)
}

# Analyze each array
for name, arr in arrays.items():
    print(f"\n{name}:")
    print(f"  ndim:     {arr.ndim}")
    print(f"  shape:    {arr.shape}")
    print(f"  size:     {arr.size}")
    print(f"  dtype:    {arr.dtype}")
    print(f"  itemsize: {arr.itemsize} bytes")
    print(f"  total memory: {arr.size * arr.itemsize} bytes")

# Output:
# 1D Vector:
#   ndim:     1
#   shape:    (10,)
#   size:     10
#   dtype:    int64
#   itemsize: 8 bytes
#   total memory: 80 bytes
#
# 2D Matrix:
#   ndim:     2
#   shape:    (3, 4)
#   size:     12
#   dtype:    float64
#   itemsize: 8 bytes
#   total memory: 96 bytes
#
# 3D Tensor:
#   ndim:     3
#   shape:    (2, 2, 2)
#   size:     8
#   dtype:    int64
#   itemsize: 8 bytes
#   total memory: 64 bytes
```

---

## Quick Reference Table

| Attribute | Returns | Example | Use Case |
|-----------|---------|---------|----------|
| **ndim** | Integer | 1, 2, 3 | Check array dimensions (is it a vector, matrix, tensor?) |
| **shape** | Tuple | (10,), (3,4), (2,2,2) | Get/verify array dimensions; reshape operations |
| **size** | Integer | 10, 12, 8 | Total element count; memory calculations |
| **itemsize** | Integer (bytes) | 4, 8, 16 | Memory per element; total memory usage; type info |
| **dtype** | Data type | int64, float32, bool | Element data type and precision |

---

## Relationship Between Attributes

```python
# These relationships always hold true:

# 1. Size is the product of shape dimensions
arr = np.arange(24).reshape(2, 3, 4)
assert arr.size == 2 * 3 * 4  # size = 24
assert arr.size == np.prod(arr.shape)  # General formula

# 2. Total memory = size × itemsize
total_bytes = arr.size * arr.itemsize

# 3. Number of dimensions = length of shape tuple
assert arr.ndim == len(arr.shape)
```

---

## Practical Tips

1. **Before reshaping:** Verify the product of new dimensions equals current size
   ```python
   new_shape = (3, 8)
   assert np.prod(new_shape) == array.size
   ```

2. **Memory optimization:** Check itemsize when dealing with large arrays
   ```python
   # If you only need integers 0-255, use uint8 instead of int64
   arr = np.arange(256, dtype=np.uint8)  # 1 byte per element
   ```

3. **Array validation:** Use attributes to validate input arrays
   ```python
   def process_matrix(arr):
       assert arr.ndim == 2, "Input must be 2D"
       assert arr.shape[0] == arr.shape[1], "Input must be square"
   ```

4. **Iteration:** Use `size` and `flat` for complete iteration
   ```python
   for i in range(array.size):
       element = array.flat[i]
   ```

---

## Related Attributes & Methods

```python
# dtype - Data type of elements
print(array.dtype)  # e.g., dtype('int64')

# nbytes - Total bytes (convenience method)
print(array.nbytes)  # Equivalent to size × itemsize

# T - Transpose (swap dimensions in 2D)
transposed = array.T

# flatten() - Convert to 1D array
flat = array.flatten()

# reshape() - Change dimensions without copying
reshaped = array.reshape(new_shape)
```

---

## Summary

| Attribute | What It Tells You |
|-----------|-------------------|
| **ndim** | Number of axes/dimensions |
| **shape** | Size along each dimension |
| **size** | Total number of elements |
| **itemsize** | Bytes per element |
| **dtype** | Data type of elements |
| **nbytes** | Total bytes (size × itemsize) |

These attributes are fundamental to understanding and working with NumPy arrays efficiently. They help with:
- Array validation
- Memory management
- Reshaping operations
- Performance optimization
- Debugging array operations

---

## Practice Exercises

1. Create arrays of different dimensions and check their `ndim`
2. Create a 4D array and determine its `shape`
3. Calculate total elements using `shape` and verify with `size`
4. Compare memory usage of different data types using `itemsize`
5. Create a 3×4 matrix and reshape it to 2×6, then verify `size` remains the same
6. Write a function that accepts an array and prints all its attributes

---

## References

- [NumPy Array Attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes)
- [NumPy Data Types](https://numpy.org/doc/stable/reference/arrays.dtypes.html)
- [NumPy Shape Manipulation](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)

