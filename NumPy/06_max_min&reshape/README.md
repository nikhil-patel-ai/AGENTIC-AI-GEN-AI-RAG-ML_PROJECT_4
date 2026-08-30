# NumPy Array: Max, Min & Reshape

## 📚 Overview
This section covers three essential NumPy array operations:
1. **`max()`** - Finding the maximum value in an array
2. **`min()`** - Finding the minimum value in an array
3. **`reshape()`** - Changing the dimensions of an array without changing its data

These operations are fundamental for data analysis, array manipulation, and preparing data for machine learning algorithms.

---

## 📖 Table of Contents
1. [Introduction](#introduction)
2. [Max Function](#max-function)
3. [Min Function](#min-function)
4. [Reshape Function](#reshape-function)
5. [Combining Operations](#combining-operations)
6. [Practical Examples](#practical-examples)
7. [Performance Considerations](#performance-considerations)
8. [Common Errors and Solutions](#common-errors-and-solutions)

---

## Introduction

These three operations are among the most commonly used NumPy functions:

| Function | Purpose | Returns |
|----------|---------|---------|
| **max()** | Find largest value | Scalar value |
| **min()** | Find smallest value | Scalar value |
| **reshape()** | Change array dimensions | New array with same data |

### Key Points
- **max() and min()** are reduction operations (reduce array to single value or smaller)
- **reshape()** is a structural operation (change shape without changing data)
- All three are highly optimized in NumPy for performance

---

## Max Function

### Purpose
The `max()` function returns the **largest value** in an array.

### Syntax
```python
np.max(array)
# or
array.max()
```

### Basic Example
```python
import numpy as np

# Create a simple array
arr = np.array([0, 1, 2, 3, 4, 5])

# Find maximum value
max_value = arr.max()
print(max_value)  # Output: 5
```

### Finding Max in 2-D Arrays

#### Max of Entire Array
```python
import numpy as np

arr = np.array([[1, 5, 3],
                [9, 2, 8],
                [4, 6, 7]])

# Find maximum value in entire array
overall_max = arr.max()
print(overall_max)  # Output: 9
```

#### Max Along Specific Axis

**Axis=0** (Column-wise - along rows):
```python
arr = np.array([[1, 5, 3],
                [9, 2, 8],
                [4, 6, 7]])

# Maximum value in each column
max_per_column = arr.max(axis=0)
print(max_per_column)  # Output: [9 6 8]

# Explanation:
# Column 0: max(1, 9, 4) = 9
# Column 1: max(5, 2, 6) = 6
# Column 2: max(3, 8, 7) = 8
```

**Axis=1** (Row-wise - along columns):
```python
arr = np.array([[1, 5, 3],
                [9, 2, 8],
                [4, 6, 7]])

# Maximum value in each row
max_per_row = arr.max(axis=1)
print(max_per_row)  # Output: [5 9 7]

# Explanation:
# Row 0: max(1, 5, 3) = 5
# Row 1: max(9, 2, 8) = 9
# Row 2: max(4, 6, 7) = 7
```

### Getting the Index of Maximum Value

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Find the value
max_val = arr.max()
print(max_val)  # Output: 9

# Find the index of maximum value
max_index = arr.argmax()
print(max_index)  # Output: 5

# Verify
print(arr[max_index])  # Output: 9
```

### Max with 2-D Array Indices

```python
arr = np.array([[1, 5, 3],
                [9, 2, 8],
                [4, 6, 7]])

# Find maximum value
max_val = arr.max()
print(max_val)  # Output: 9

# Find indices (flattened)
max_index = arr.argmax()
print(max_index)  # Output: 4 (position in flattened array [1,5,3,9,...])

# Convert to 2-D indices
row, col = np.unravel_index(max_index, arr.shape)
print(f"Position: row {row}, column {col}")  # Output: Position: row 1, column 0
```

### Practical Use Cases

**Example: Temperature Analysis**
```python
# Daily temperatures for a week
temperatures = np.array([22, 24, 28, 26, 25, 29, 27])

hottest_day = temperatures.max()
print(f"Hottest temperature: {hottest_day}°C")  # 29

hottest_day_index = temperatures.argmax()
print(f"Hottest day (index): Day {hottest_day_index + 1}")  # Day 6
```

---

## Min Function

### Purpose
The `min()` function returns the **smallest value** in an array.

### Syntax
```python
np.min(array)
# or
array.min()
```

### Basic Example
```python
import numpy as np

# Create a simple array
arr = np.array([0, 1, 2, 3, 4, 5])

# Find minimum value
min_value = arr.min()
print(min_value)  # Output: 0
```

### Finding Min in 2-D Arrays

#### Min of Entire Array
```python
import numpy as np

arr = np.array([[5, 3, 8],
                [2, 9, 1],
                [6, 4, 7]])

# Find minimum value in entire array
overall_min = arr.min()
print(overall_min)  # Output: 1
```

#### Min Along Specific Axis

**Axis=0** (Column-wise):
```python
arr = np.array([[5, 3, 8],
                [2, 9, 1],
                [6, 4, 7]])

# Minimum value in each column
min_per_column = arr.min(axis=0)
print(min_per_column)  # Output: [2 3 1]

# Column 0: min(5, 2, 6) = 2
# Column 1: min(3, 9, 4) = 3
# Column 2: min(8, 1, 7) = 1
```

**Axis=1** (Row-wise):
```python
arr = np.array([[5, 3, 8],
                [2, 9, 1],
                [6, 4, 7]])

# Minimum value in each row
min_per_row = arr.min(axis=1)
print(min_per_row)  # Output: [3 1 4]

# Row 0: min(5, 3, 8) = 3
# Row 1: min(2, 9, 1) = 1
# Row 2: min(6, 4, 7) = 4
```

### Getting the Index of Minimum Value

```python
arr = np.array([8, 3, 5, 1, 9, 2, 7])

# Find the minimum value
min_val = arr.min()
print(min_val)  # Output: 1

# Find the index of minimum value
min_index = arr.argmin()
print(min_index)  # Output: 3

# Verify
print(arr[min_index])  # Output: 1
```

### Practical Use Cases

**Example: Price Analysis**
```python
# Product prices
prices = np.array([29.99, 45.50, 12.99, 78.00, 34.50])

cheapest_price = prices.min()
print(f"Cheapest price: ${cheapest_price}")  # $12.99

cheapest_index = prices.argmin()
print(f"Cheapest product index: {cheapest_index}")  # Index 2
```

---

## Reshape Function

### Purpose
The `reshape()` function changes the **dimensions** of an array without changing its **data**. It reorganizes the same elements into a different shape.

### Important Concept
- Original array size must match the new shape size
- No data is lost or reordered (by default, uses row-major/C-order)
- Very efficient operation

### Syntax
```python
arr.reshape(new_shape)
# or
np.reshape(arr, new_shape)
```

### Basic Example
```python
import numpy as np

# Create a 1-D array with 6 elements
arr = np.array([0, 1, 2, 3, 4, 5])
print("Original shape:", arr.shape)  # (6,)
print(arr)  # [0 1 2 3 4 5]

# Reshape to 2-D array (3 rows, 2 columns)
reshaped = arr.reshape(3, 2)
print("New shape:", reshaped.shape)  # (3, 2)
print(reshaped)
# [[0 1]
#  [2 3]
#  [4 5]]
```

### Reshape a 1-D to 2-D Array

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# 2 rows, 3 columns
arr_2d = arr.reshape(2, 3)
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]

# 3 rows, 2 columns
arr_2d_alt = arr.reshape(3, 2)
print(arr_2d_alt)
# [[1 2]
#  [3 4]
#  [5 6]]
```

### Reshape a 2-D to 1-D Array

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Flatten to 1-D
arr_1d = arr.reshape(6)  # or arr.reshape(-1)
print(arr_1d)  # [1 2 3 4 5 6]
```

### Reshape to 3-D Array

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Reshape to 2x2x2 (3-D)
arr_3d = arr.reshape(2, 2, 2)
print(arr_3d)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

print("Shape:", arr_3d.shape)  # (2, 2, 2)
```

### Using -1 for Automatic Dimension

The `-1` parameter tells NumPy to automatically calculate that dimension:

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape to 3 rows, let NumPy calculate columns
arr_reshaped = arr.reshape(3, -1)
print(arr_reshaped)
# [[1  2  3  4]
#  [5  6  7  8]
#  [9 10 11 12]]
# NumPy calculated 12 / 3 = 4 columns

# Reshape to 4 rows, let NumPy calculate columns
arr_reshaped2 = arr.reshape(4, -1)
print(arr_reshaped2)
# [[1  2  3]
#  [4  5  6]
#  [7  8  9]
#  [10 11 12]]
# NumPy calculated 12 / 4 = 3 columns

# Flatten to 1-D using -1
arr_1d = arr.reshape(-1)
print(arr_1d)  # [1 2 3 4 5 6 7 8 9 10 11 12]
```

### Reshape with Different Orders

#### Row-Major Order (Default - 'C')
```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Default: fills rows first (C-order)
arr_c = arr.reshape(2, 3, order='C')
print(arr_c)
# [[1 2 3]
#  [4 5 6]]
```

#### Column-Major Order ('F')
```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Fills columns first (Fortran-order)
arr_f = arr.reshape(2, 3, order='F')
print(arr_f)
# [[1 3 5]
#  [2 4 6]]
```

### View vs. Copy

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# reshape() returns a view (not a copy)
reshaped = arr.reshape(2, 3)

# Modifying the reshaped array affects original
reshaped[0, 0] = 99
print(arr)  # [99 2 3 4 5 6] - original changed!

# Use copy() if you need independent array
reshaped_copy = arr.reshape(2, 3).copy()
reshaped_copy[0, 0] = 99
print(arr)  # [1 2 3 4 5 6] - original unchanged
```

### Common Reshape Patterns

```python
import numpy as np

# Create sample array
arr = np.arange(24)  # [0, 1, 2, ..., 23]

# Flatten all dimensions
flat = arr.reshape(-1)  # Shape: (24,)

# 2-D matrix
matrix = arr.reshape(4, 6)  # Shape: (4, 6)

# 3-D tensor
tensor = arr.reshape(2, 3, 4)  # Shape: (2, 3, 4)

# Transpose using reshape (limited cases)
# For 2-D, use .T attribute instead
transposed = arr.reshape(6, 4).T  # Shape: (4, 6)
```

---

## Combining Operations

### Max/Min on Reshaped Arrays

```python
import numpy as np

# Original 1-D array
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# Reshape to 2-D and find max per row
arr_2d = arr.reshape(-1, 3)  # 4 rows, 3 columns (one row won't fill)
# This will error - let's use compatible size

arr = np.arange(12)  # [0-11]
arr_2d = arr.reshape(3, 4)

# Max of entire array
overall_max = arr_2d.max()  # 11

# Max per row
row_max = arr_2d.max(axis=1)  # [3, 7, 11]

# Max per column
col_max = arr_2d.max(axis=0)  # [8, 9, 10, 11]

print(f"Overall max: {overall_max}")
print(f"Row max: {row_max}")
print(f"Column max: {col_max}")
```

### Finding Location of Max in Reshaped Array

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Reshape and find max
arr_2d = arr.reshape(2, 4)
print(arr_2d)
# [[3 1 4 1]
#  [5 9 2 6]]

# Find max value
max_val = arr_2d.max()  # 9

# Find its index in flattened array
flat_index = arr_2d.argmax()  # 5

# Convert to 2-D indices
row, col = np.unravel_index(flat_index, arr_2d.shape)
print(f"Max value {max_val} at position [{row}, {col}]")  # [1, 1]
```

---

## Practical Examples

### Example 1: Analyzing Student Scores

```python
import numpy as np

# Scores for 5 students in 4 subjects
scores = np.array([85, 90, 78, 92,
                   88, 95, 82, 89,
                   91, 87, 85, 93,
                   79, 81, 88, 86,
                   92, 89, 95, 91])

# Reshape to 5 students, 4 subjects
scores_2d = scores.reshape(5, 4)

print("Student Scores:")
print(scores_2d)

# Highest score overall
highest = scores_2d.max()
print(f"\nHighest score: {highest}")

# Lowest score overall
lowest = scores_2d.min()
print(f"Lowest score: {lowest}")

# Best score per student
best_per_student = scores_2d.max(axis=1)
print(f"\nBest score per student: {best_per_student}")

# Worst score per student
worst_per_student = scores_2d.min(axis=1)
print(f"Worst score per student: {worst_per_student}")

# Highest score per subject
highest_per_subject = scores_2d.max(axis=0)
print(f"\nHighest score per subject: {highest_per_subject}")
```

### Example 2: Image Data Processing

```python
import numpy as np

# Create simulated grayscale image (height=10, width=10)
image = np.random.randint(0, 256, (10, 10))

print("Image brightness range:")
print(f"Brightest pixel: {image.max()}")
print(f"Darkest pixel: {image.min()}")

# Brightness per row
row_brightness = image.max(axis=1)
print(f"\nBrightest pixel per row: {row_brightness}")

# Brightness per column
col_brightness = image.max(axis=0)
print(f"Brightest pixel per column: {col_brightness}")

# Reshape image to 1-D and find brightest pixel location
brightest_index = image.argmax()
brightest_row, brightest_col = np.unravel_index(brightest_index, image.shape)
print(f"\nBrightest pixel at position [{brightest_row}, {brightest_col}]")
```

### Example 3: Sales Data Analysis

```python
import numpy as np

# Monthly sales for 3 quarters (3 months per quarter)
# 4 products
sales_data = np.array([1000, 1200, 1100,  # Product 1
                       1500, 1400, 1600,  # Product 2
                       900, 1000, 950,    # Product 3
                       1800, 1900, 1700])  # Product 4

# Reshape to 4 products, 3 months
sales = sales_data.reshape(4, 3)

print("Sales by Product (3 months):")
print(sales)

# Best performing product (highest total)
product_totals = sales.sum(axis=1)
best_product = product_totals.argmax()
print(f"\nBest product: Product {best_product + 1} (${product_totals[best_product]})")

# Highest selling month
month_totals = sales.sum(axis=0)
best_month = month_totals.argmax()
print(f"Best month: Month {best_month + 1} (${month_totals[best_month]})")

# Product with highest single sale
max_sale = sales.max()
print(f"\nHighest sale: ${max_sale}")

# Product with lowest single sale
min_sale = sales.min()
print(f"Lowest sale: ${min_sale}")
```

---

## Performance Considerations

### Speed Comparison

```python
import numpy as np
import time

# Create large array
large_arr = np.random.randint(0, 1000, 1000000)

# Method 1: NumPy max (optimized C code)
start = time.time()
result1 = large_arr.max()
numpy_time = time.time() - start

# Method 2: Python built-in max (slower)
start = time.time()
result2 = max(large_arr)
python_time = time.time() - start

print(f"NumPy max: {numpy_time:.6f} seconds")
print(f"Python max: {python_time:.6f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster!")
```

### Memory Efficiency

```python
import numpy as np

# reshape() doesn't copy data (returns a view)
arr = np.arange(1000000)

# Very fast - no data copying
reshaped = arr.reshape(1000, 1000)

# Compare with copy
reshaped_copy = arr.reshape(1000, 1000).copy()  # Slower due to copy
```

---

## Common Errors and Solutions

### ❌ Error 1: Reshape Size Mismatch

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Error: Cannot reshape array of size 6 into shape (2, 4)
# reshaped = arr.reshape(2, 4)  # ValueError!

# Solution: Use compatible shape
reshaped = arr.reshape(2, 3)  # Correct: 2 * 3 = 6
```

### ❌ Error 2: Max/Min on Empty Array

```python
import numpy as np

empty_arr = np.array([])

# Error: zero-size array to reduction operation maximum
# max_val = empty_arr.max()  # ValueError!

# Solution: Check array size first
if empty_arr.size > 0:
    max_val = empty_arr.max()
else:
    print("Array is empty")
```

### ❌ Error 3: Axis Out of Range

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])  # 2-D array

# Error: axis 2 is out of bounds for array of dimension 2
# result = arr.max(axis=2)  # ValueError!

# Solution: Use valid axis (0 or 1 for 2-D)
result = arr.max(axis=0)  # Valid
```

### ❌ Error 4: Trying to Modify Reshaped Array

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
reshaped = arr.reshape(2, 2)

# Modifying reshaped affects original (it's a view)
reshaped[0, 0] = 99
print(arr)  # [99 2 3 4] - original changed!

# Solution: Use copy() if you need independence
reshaped_copy = arr.reshape(2, 2).copy()
reshaped_copy[0, 0] = 99
print(arr)  # [1 2 3 4] - original unchanged
```

---

## Summary Table

| Operation | Syntax | Purpose | Returns |
|-----------|--------|---------|---------|
| **max()** | `arr.max()` or `np.max(arr)` | Find maximum value | Scalar or array |
| **max(axis=0)** | `arr.max(axis=0)` | Max along columns | 1-D array |
| **max(axis=1)** | `arr.max(axis=1)` | Max along rows | 1-D array |
| **min()** | `arr.min()` or `np.min(arr)` | Find minimum value | Scalar or array |
| **argmax()** | `arr.argmax()` | Index of maximum | Integer or array |
| **argmin()** | `arr.argmin()` | Index of minimum | Integer or array |
| **reshape()** | `arr.reshape(shape)` | Change dimensions | Reshaped array (view) |

---

## Best Practices

1. **Use axis parameter** for multi-dimensional analysis
2. **Use -1 in reshape** to let NumPy calculate dimension
3. **Check array size** before using max/min on user input
4. **Use .copy()** if you need an independent reshaped array
5. **Combine operations** for efficient data processing
6. **Use argmax/argmin** when you need element location

---

## Next Steps
- Master **sorting** and **searching** with NumPy
- Learn **broadcasting** for efficient operations
- Explore **statistical functions** (mean, std, etc.)
- Apply to real-world data analysis tasks

---

**Happy Computing! 🚀**
