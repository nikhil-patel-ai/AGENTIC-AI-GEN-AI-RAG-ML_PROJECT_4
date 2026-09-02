# NumPy Array Operations

This notebook is a comprehensive guide to various operations you can perform on NumPy arrays. It covers everything from basic arithmetic to advanced array manipulation techniques.

---

## Table of Contents

1. [Scalar Operations](#scalar-operations)
2. [Relational Operators](#relational-operators)
3. [Vector Operations](#vector-operations)
4. [Array Functions](#array-functions)
5. [Statistical Functions](#statistical-functions)
6. [Trigonometric Functions](#trigonometric-functions)
7. [Dot Product](#dot-product)
8. [Logarithmic and Exponential Functions](#logarithmic-and-exponential-functions)
9. [Rounding Functions](#rounding-functions)
10. [Iteration](#iteration)
11. [Reshaping](#reshaping)
12. [Stacking](#stacking)
13. [Splitting](#splitting)

---

## Setup

```python
import numpy as np

# Example arrays used throughout
z1 = np.arange(12).reshape(3,4)  # [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
z2 = np.arange(12,24).reshape(3,4)  # [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]
```

---

## Scalar Operations

Scalar operations perform arithmetic operations on each element of an array with a single scalar value.

### Addition
```python
z1 + 2
# [[2, 3, 4, 5],
#  [6, 7, 8, 9],
#  [10, 11, 12, 13]]
```

### Subtraction
```python
z1 - 2
# [[-2, -1, 0, 1],
#  [2, 3, 4, 5],
#  [6, 7, 8, 9]]
```

### Multiplication
```python
z1 * 2
# [[0, 2, 4, 6],
#  [8, 10, 12, 14],
#  [16, 18, 20, 22]]
```

### Exponentiation (Power)
```python
z1 ** 2
# [[0, 1, 4, 9],
#  [16, 25, 36, 49],
#  [64, 81, 100, 121]]
```

### Modulo (Remainder)
```python
z1 % 2
# [[0, 1, 0, 1],
#  [0, 1, 0, 1],
#  [0, 1, 0, 1]]
```

### Division
```python
z1 / 2
# [[0., 0.5, 1., 1.5],
#  [2., 2.5, 3., 3.5],
#  [4., 4.5, 5., 5.5]]
```

### Floor Division
```python
z1 // 2
# [[0, 0, 1, 1],
#  [2, 2, 3, 3],
#  [4, 4, 5, 5]]
```

**Key Point:** These operations are applied element-wise to every element in the array simultaneously.

---

## Relational Operators

Relational operators (comparison operators) compare array elements and return boolean arrays (True/False).

### Greater Than (>)
```python
z2 > 2
# Returns boolean array where each True indicates element > 2
# [[True, True, True, True],
#  [True, True, True, True],
#  [True, True, True, True]]

z2 > 20
# [[False, False, False, False],
#  [False, False, False, False],
#  [True, True, True, True]]
```

### Other Comparison Operators
```python
z2 < 15      # Less than
z2 <= 15     # Less than or equal
z2 >= 15     # Greater than or equal
z2 == 15     # Equal to
z2 != 15     # Not equal to
```

### Usage with Filtering
```python
# Filter array elements
filtered = z2[z2 > 18]  # Get all elements greater than 18
# Output: [19, 20, 21, 22, 23]

# Count elements meeting condition
count = np.sum(z2 > 18)  # Returns 5
```

**Key Point:** Relational operators return boolean arrays useful for conditional operations and filtering.

---

## Vector Operations

Vector operations perform element-wise arithmetic between two arrays of the same shape.

### Prerequisites
- Both arrays must have the same shape
- Operations are performed element-by-element

### Addition
```python
z1 + z2
# [[12, 14, 16, 18],
#  [20, 22, 24, 26],
#  [28, 30, 32, 34]]
```

### Subtraction
```python
z1 - z2
# [[-12, -12, -12, -12],
#  [-12, -12, -12, -12],
#  [-12, -12, -12, -12]]
```

### Multiplication (Element-wise)
```python
z1 * z2
# [[0, 13, 28, 45],
#  [64, 85, 108, 133],
#  [160, 189, 220, 253]]
```

### Division (Element-wise)
```python
z1 / z2
# [[0., 0.076923..., 0.142857..., 0.2],
#  [0.25, 0.294117..., 0.333333..., 0.368421...],
#  [0.4, 0.428571..., 0.454545..., 0.478260...]]
```

**Important Note:** Element-wise multiplication is NOT matrix multiplication. Use `np.dot()` for matrix multiplication.

### Broadcasting
Arrays with different shapes can be operated under certain broadcasting rules:

```python
# Broadcasting example
a = np.array([[1, 2, 3]])      # Shape: (1, 3)
b = np.array([[1], [2], [3]])  # Shape: (3, 1)
result = a + b  # Broadcasting adds the scalar to all elements
# Result shape: (3, 3)
```

---

## Array Functions

### Max and Min

```python
k1 = np.round(np.random.random((3,3)) * 100)

# Overall maximum
np.max(k1)  # Returns maximum value in entire array

# Maximum of each row (axis=1)
np.max(k1, axis=1)
# Output example: [100., 98., 99.]

# Maximum of each column (axis=0)
np.max(k1, axis=0)
# Output example: [100., 99., 100.]

# Minimum operations (same syntax)
np.min(k1)
np.min(k1, axis=0)
np.min(k1, axis=1)
```

### Sum

```python
# Sum of all elements
np.sum(k1)

# Sum of each row
np.sum(k1, axis=1)

# Sum of each column
np.sum(k1, axis=0)
```

### Product

```python
# Product (multiplication) of all elements
np.prod(k1)

# Product of each row
np.prod(k1, axis=1)

# Product of each column
np.prod(k1, axis=0)
```

### Understanding `axis` Parameter

For a 2D array (3 rows × 4 columns):
- **axis=0**: Operations along rows (vertically, result has length = number of columns)
- **axis=1**: Operations along columns (horizontally, result has length = number of rows)
- **No axis**: Operation on all elements

```
Array shape: (3, 4)
             [col0, col1, col2, col3]  row0
             [col0, col1, col2, col3]  row1
             [col0, col1, col2, col3]  row2

axis=1: operates horizontally (left-right) → 3 values
axis=0: operates vertically (top-bottom) → 4 values
```

---

## Statistical Functions

### Mean (Average)

```python
# Mean of all elements
np.mean(k1)

# Mean of each column
k1.mean(axis=0)

# Mean of each row
k1.mean(axis=1)
```

### Median (Middle Value)

```python
# Median of all elements
np.median(k1)

# Median of each row
np.median(k1, axis=1)

# Median of each column
np.median(k1, axis=0)

# Example:
# Array: [1, 2, 3, 4, 5] → Median = 3
# Array: [1, 2, 3, 4] → Median = 2.5 (average of middle two)
```

### Standard Deviation

Standard deviation measures how spread out data is from the mean.

```python
# Std dev of all elements
np.std(k1)

# Std dev of each column
np.std(k1, axis=0)

# Std dev of each row
np.std(k1, axis=1)

# Lower std dev = data points cluster near mean
# Higher std dev = data points spread out
```

### Variance

Variance is the square of standard deviation.

```python
# Variance of all elements
np.var(k1)

# Variance of each column
np.var(k1, axis=0)

# Variance of each row
np.var(k1, axis=1)

# Relationship: variance = (std dev)²
```

### Summary of Statistical Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `mean()` | Average value | np.mean([1,2,3,4,5]) = 3 |
| `median()` | Middle value | np.median([1,2,3,4,5]) = 3 |
| `std()` | Spread from mean | np.std([1,5]) = 2.0 |
| `var()` | Squared spread | np.var([1,5]) = 4.0 |
| `min()` | Smallest value | np.min([1,2,3]) = 1 |
| `max()` | Largest value | np.max([1,2,3]) = 3 |
| `sum()` | Total | np.sum([1,2,3]) = 6 |

---

## Trigonometric Functions

### Sine
```python
np.sin(k1)
# Returns sine of each element (in radians)

# Example:
np.sin(0)      # 0
np.sin(np.pi/2)  # 1
np.sin(np.pi)  # 6.123233995736766e-17 (≈ 0)
```

### Cosine
```python
np.cos(k1)
# Returns cosine of each element

# Example:
np.cos(0)      # 1
np.cos(np.pi/2)  # 6.123233995736766e-17 (≈ 0)
np.cos(np.pi)  # -1
```

### Tangent
```python
np.tan(k1)
# Returns tangent of each element

# Example:
np.tan(0)      # 0
np.tan(np.pi/4)  # 1
```

### Inverse Trigonometric Functions
```python
np.arcsin(0.5)  # Inverse sine
np.arccos(0.5)  # Inverse cosine
np.arctan(1)    # Inverse tangent
```

**Note:** Angles must be in radians. Convert from degrees:
```python
degrees = 90
radians = np.deg2rad(degrees)  # or degrees * np.pi / 180
result = np.sin(radians)
```

---

## Dot Product

The dot product is used for matrix multiplication.

### Definition
For matrices with compatible dimensions:
- Matrix A: (m × n)
- Matrix B: (n × p)
- Result: (m × p)

Each element in result is the dot product of corresponding row and column.

### Example

```python
s2 = np.arange(12).reshape(3, 4)   # Shape: (3, 4)
s3 = np.arange(12, 24).reshape(4, 3)  # Shape: (4, 3)

result = np.dot(s2, s3)  # Shape: (3, 3)
# or
result = s2 @ s3  # @ operator also computes dot product (Python 3.5+)
```

### When to Use

```python
# For matrix multiplication (rows × columns)
np.dot(matrix_a, matrix_b)

# NOT for element-wise multiplication
# matrix_a * matrix_b  # This is element-wise, not matrix multiplication
```

### Practical Example

```python
# In linear algebra/ML:
# y = X · w (predictions = features · weights)
X = np.array([[1, 2], [3, 4], [5, 6]])  # 3 samples, 2 features
w = np.array([0.5, 0.3])                # 2 weights
y = np.dot(X, w)                        # 3 predictions
```

---

## Logarithmic and Exponential Functions

### Exponential (e^x)
```python
np.exp(s2)
# Returns e raised to power of each element
# e ≈ 2.71828

# Example:
np.exp(0)  # 1
np.exp(1)  # 2.718281828...
np.exp(2)  # 7.389056099...
```

### Natural Logarithm (ln)
```python
np.log(array)
# Returns natural log of each element
# Inverse of np.exp()

# Example:
np.log(1)    # 0
np.log(2.718281828)  # ≈ 1
```

### Base-10 Logarithm
```python
np.log10(array)
# Returns log base 10

# Example:
np.log10(1)    # 0
np.log10(10)   # 1
np.log10(100)  # 2
```

### Base-2 Logarithm
```python
np.log2(array)
# Returns log base 2

# Example:
np.log2(1)    # 0
np.log2(2)    # 1
np.log2(4)    # 2
np.log2(8)    # 3
```

### Square Root
```python
np.sqrt(array)
# Returns square root of each element

# Example:
np.sqrt(4)   # 2
np.sqrt(9)   # 3
np.sqrt(16)  # 4
```

---

## Rounding Functions

### Round

```python
arr = np.array([1.2, 2.7, 3.5, 4.9])
np.round(arr)  # [1., 3., 4., 5.]

# Round to specific decimals
arr = np.array([1.234, 2.567, 3.891])
np.round(arr, decimals=2)  # [1.23, 2.57, 3.89]

# Round to nearest even (banker's rounding)
np.round(2.5)  # 2
np.round(3.5)  # 4
```

**Rounding Rules:**
- 0.5 rounds to nearest even number
- 1.5 → 2 (even)
- 2.5 → 2 (even)
- 3.5 → 4 (even)

### Floor

Rounds down to the nearest integer (largest integer ≤ value).

```python
arr = np.array([1.2, 2.7, 3.5, 4.9])
np.floor(arr)  # [1., 2., 3., 4.]

# Floor with random numbers
np.floor(np.random.random((2, 3)) * 100)
```

### Ceil

Rounds up to the nearest integer (smallest integer ≥ value).

```python
arr = np.array([1.2, 2.7, 3.5, 4.9])
np.ceil(arr)  # [2., 3., 4., 5.]

# Ceil with random numbers
np.ceil(np.random.random((2, 3)) * 100)
```

### Comparison Table

| Value | round() | floor() | ceil() |
|-------|---------|---------|--------|
| 1.2 | 1 | 1 | 2 |
| 1.5 | 2 | 1 | 2 |
| 1.7 | 2 | 1 | 2 |
| 2.5 | 2 | 2 | 3 |
| 3.5 | 4 | 3 | 4 |

---

## Iteration

Iterating through NumPy arrays efficiently.

### 1D Array Iteration

```python
p1 = np.arange(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in p1:
    print(i)  # Prints: 0, 1, 2, ..., 9
```

### 2D Array Iteration

```python
p2 = np.arange(12).reshape(3, 4)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11]]

for i in p2:
    print(i)  # Prints entire rows: [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]
```

### 3D Array Iteration

```python
p3 = np.arange(8).reshape(2, 2, 2)
# [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]

for i in p3:
    print(i)  # Prints 2D arrays
# Output:
# [[0 1]
#  [2 3]]
# [[4 5]
#  [6 7]]
```

### Iterating Over All Elements (nditer)

To access every individual element regardless of array dimensions:

```python
p3 = np.arange(8).reshape(2, 2, 2)

for i in np.nditer(p3):
    print(i)  # Prints: 0, 1, 2, 3, 4, 5, 6, 7

# This converts multidimensional arrays to 1D internally
```

### Using enumerate()

```python
for index, value in enumerate(p1):
    print(f"Index {index}: Value {value}")
```

### Nested Loops (2D)

```python
p2 = np.arange(12).reshape(3, 4)

for i in range(p2.shape[0]):  # Iterate rows
    for j in range(p2.shape[1]):  # Iterate columns
        print(p2[i, j])
```

---

## Reshaping

Reshaping changes the dimensions of an array without changing data.

### Transpose

Swap rows and columns (for 2D arrays) or reverse axes (for nD arrays).

```python
p2 = np.arange(12).reshape(3, 4)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11]]

# Method 1: np.transpose()
np.transpose(p2)

# Method 2: .T attribute
p2.T
# Output shape: (4, 3)
# [[0, 4, 8],
#  [1, 5, 9],
#  [2, 6, 10],
#  [3, 7, 11]]

# For 3D arrays
p3 = np.arange(8).reshape(2, 2, 2)
p3.T  # Reverses all axes: (2, 2, 2) → (2, 2, 2)
```

### Ravel

Converts any dimensional array to 1D (flattens).

```python
p2 = np.arange(12).reshape(3, 4)
p2.ravel()  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

p3 = np.arange(8).reshape(2, 2, 2)
p3.ravel()  # [0, 1, 2, 3, 4, 5, 6, 7]
```

### Flatten

Similar to ravel(), but returns a copy instead of view:

```python
p2.flatten()  # Returns new 1D array (copy)
p2.ravel()    # Returns view (more memory efficient)
```

### Reshape

Changes dimensions while maintaining total elements:

```python
arr = np.arange(12)
arr.reshape(3, 4)   # (12,) → (3, 4)
arr.reshape(2, 6)   # (12,) → (2, 6)
arr.reshape(2, 2, 3)  # (12,) → (2, 2, 3)
```

**Rules:**
- Product of new dimensions must equal total elements
- `12 = 3 × 4 = 2 × 6 = 2 × 2 × 3`
- Cannot reshape 12 elements into (3, 5) because 3 × 5 = 15 ≠ 12

---

## Stacking

Combining multiple arrays into one.

### Horizontal Stack (hstack)

Concatenate arrays side-by-side (along columns).

```python
w1 = np.arange(12).reshape(3, 4)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11]]

w2 = np.arange(12, 24).reshape(3, 4)
# [[12, 13, 14, 15],
#  [16, 17, 18, 19],
#  [20, 21, 22, 23]]

result = np.hstack((w1, w2))  # Note: use tuple of arrays
# Output shape: (3, 8)
# [[0, 1, 2, 3, 12, 13, 14, 15],
#  [4, 5, 6, 7, 16, 17, 18, 19],
#  [8, 9, 10, 11, 20, 21, 22, 23]]
```

### Vertical Stack (vstack)

Concatenate arrays top-to-bottom (along rows).

```python
result = np.vstack((w1, w2))  # Note: use tuple of arrays
# Output shape: (6, 4)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11],
#  [12, 13, 14, 15],
#  [16, 17, 18, 19],
#  [20, 21, 22, 23]]
```

### Depth Stack (dstack)

Concatenate arrays along depth (third dimension).

```python
result = np.dstack((w1, w2))
# Output shape: (3, 4, 2)
```

### Concatenate

General purpose concatenation along specified axis.

```python
# Concatenate along axis=0 (rows)
np.concatenate((w1, w2), axis=0)  # Same as vstack

# Concatenate along axis=1 (columns)
np.concatenate((w1, w2), axis=1)  # Same as hstack
```

### Visualization

```
hstack (axis=1):           vstack (axis=0):
┌─────────┬─────────┐     ┌─────────┐
│   w1    │   w2    │     │   w1    │
├─────────┼─────────┤     ├─────────┤
                          │   w2    │
                          └─────────┘
```

---

## Splitting

Opposite of stacking. Dividing arrays into smaller arrays.

### Horizontal Split (hsplit)

Split array along columns (left-right).

```python
w1 = np.arange(12).reshape(3, 4)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11]]

# Split into 2 equal parts
result = np.hsplit(w1, 2)
# Returns 2 arrays of shape (3, 2) each:
# [array([[0, 1], [4, 5], [8, 9]]),
#  array([[2, 3], [6, 7], [10, 11]])]

# Split into 4 equal parts
result = np.hsplit(w1, 4)
# Returns 4 arrays of shape (3, 1) each:
# [array([[0], [4], [8]]),
#  array([[1], [5], [9]]),
#  array([[2], [6], [10]]),
#  array([[3], [7], [11]])]

# Split at specific column indices
result = np.hsplit(w1, [1, 3])  # Split after columns 1 and 3
# Returns 3 arrays: columns [0], [1-2], [3]
```

### Vertical Split (vsplit)

Split array along rows (top-bottom).

```python
w2 = np.arange(12, 24).reshape(3, 4)

# Split into 3 equal parts (1 row each)
result = np.vsplit(w2, 3)
# Returns 3 arrays of shape (1, 4) each

# Split at specific row indices
result = np.vsplit(w2, [1, 2])  # Split after rows 1 and 2
# Returns 3 arrays: rows [0], [1], [2]
```

### Depth Split (dsplit)

Split array along depth dimension.

```python
arr = np.arange(24).reshape(2, 3, 4)
result = np.dsplit(arr, 2)  # Split into 2 parts along depth
```

### Visualization

```
Original (3, 4):              hsplit(w1, 2):           vsplit(w2, 3):
┌─────────────────┐           ┌───────┬───────┐        ┌─────────┐
│                 │           │ Part1 │ Part2 │        │  Row 0  │
│                 │   →        │       │       │   →   ├─────────┤
│                 │           │       │       │        │  Row 1  │
└─────────────────┘           └───────┴───────┘        ├─────────┤
                                                        │  Row 2  │
                                                        └─────────┘
```

---

## Practical Examples

### Example 1: Data Analysis

```python
# Student grades
grades = np.array([
    [85, 90, 78, 92],  # Student 1
    [88, 92, 85, 95],  # Student 2
    [75, 80, 82, 78],  # Student 3
])

# Analysis
overall_avg = np.mean(grades)  # 86.04
subject_avg = np.mean(grades, axis=0)  # Average per subject
student_avg = np.mean(grades, axis=1)  # Average per student

best_student = np.argmax(student_avg)  # Index of best student
highest_score = np.max(grades)  # Highest score overall
```

### Example 2: Image Processing

```python
# Simulate image array (100×100 RGB)
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Brightness adjustment
brightened = np.clip(image * 1.2, 0, 255).astype(np.uint8)

# Extract channel
red_channel = image[:, :, 0]

# Convert to grayscale
gray = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
```

### Example 3: Matrix Operations

```python
# System of linear equations: Ax = b
A = np.array([[2, 1], [1, 3]])
b = np.array([8, 13])

# Solve: x = A^(-1) · b
x = np.linalg.solve(A, b)
# or
x = np.dot(np.linalg.inv(A), b)
```

---

## Quick Reference Table

| Operation | Function | Example |
|-----------|----------|---------|
| Add scalar | `arr + 2` | Element-wise addition |
| Compare | `arr > 5` | Boolean array |
| Sum | `np.sum(arr)` | Total of elements |
| Average | `np.mean(arr)` | Mean value |
| Transpose | `arr.T` | Swap axes |
| Flatten | `arr.ravel()` | Convert to 1D |
| Stack | `np.hstack()` | Combine arrays |
| Split | `np.hsplit()` | Divide arrays |
| Dot product | `np.dot(a, b)` | Matrix multiply |
| Round | `np.round(arr)` | Round to integer |
| Iterate | `for i in arr` | Loop through |

---

## Summary

This notebook covers:
- **Scalar operations**: Math on single values
- **Vector operations**: Math between arrays
- **Aggregation**: Sum, min, max across arrays
- **Statistics**: Mean, median, std, variance
- **Transformations**: Transpose, reshape, flatten
- **Manipulation**: Stack, split, concatenate
- **Mathematical**: Trig, log, exp, dot product

Master these operations to unlock NumPy's power for scientific computing, data analysis, and machine learning.

---

## Practice Exercises

1. Create two 3×3 arrays and perform scalar and vector operations
2. Calculate statistics (mean, std, median) on a random array
3. Use dot product to solve a simple linear system
4. Flatten a 3D array and iterate through elements
5. Stack and split arrays in different ways
6. Filter array elements using relational operators
7. Create a simple gradient using exponential functions
8. Perform trigonometric operations on array of angles
9. Reshape an array multiple ways maintaining element count
10. Combine rounding functions (round, floor, ceil) on random data

---

## References

- [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
- [NumPy Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [NumPy Array Manipulation](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)
- [NumPy Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)
