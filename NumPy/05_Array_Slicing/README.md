# NumPy Array Slicing

## 📚 Overview
This section covers **Array Slicing** in NumPy, which is the process of extracting a portion or subset of elements from an array using a range of indices. Slicing is different from indexing (which accesses single elements) and allows you to work with multiple elements efficiently.

---

## 📖 Table of Contents
1. [Introduction](#introduction)
2. [Basic Slicing Concepts](#basic-slicing-concepts)
3. [1-D Array Slicing](#1-d-array-slicing)
4. [Negative Slicing](#negative-slicing)
5. [Step in Slicing](#step-in-slicing)
6. [2-D Array Slicing](#2-d-array-slicing)
7. [Key Concepts](#key-concepts)
8. [Practical Examples](#practical-examples)
9. [Slicing vs. Indexing](#slicing-vs-indexing)

---

## Introduction

**Array slicing** is a technique to extract a contiguous subset of elements from an array. Instead of accessing individual elements (indexing), slicing allows you to:
- Extract a **range of elements** at once
- Get multiple consecutive or evenly-spaced elements
- Work with subarrays without creating copies
- Perform batch operations on array segments

### Why is Slicing Important?
- **Efficiency**: Access multiple elements without a loop
- **Readability**: Clean, concise syntax for extracting data ranges
- **Data Processing**: Extract specific portions of datasets for analysis
- **Memory**: Slices are often views (not copies), saving memory

### Core Concept
Slicing uses the colon operator `:` to specify a range: `[start:end:step]`

---

## Basic Slicing Concepts

### The Slicing Syntax
```python
array[start:end:step]
```

### Parameters Explained

| Parameter | Meaning | Default | Example |
|-----------|---------|---------|---------|
| **start** | Index where slice begins (inclusive) | 0 | arr[2:] starts at index 2 |
| **end** | Index where slice ends (exclusive) | Array length | arr[:5] ends before index 5 |
| **step** | Increment between selected elements | 1 | arr[::2] takes every 2nd element |

### Important Rules
1. **Start is inclusive** – The element at the start index IS included
2. **End is exclusive** – The element at the end index is NOT included
3. **Missing values have defaults**:
   - No start → starts from 0
   - No end → goes to array length
   - No step → step is 1

### Visual Example
```
Array:     [1, 2, 3, 4, 5, 6, 7]
Index:      0  1  2  3  4  5  6
Slice [1:4]: includes indices 1, 2, 3 (NOT 4)
Result:   [2, 3, 4]
```

---

## 1-D Array Slicing

### Basic Slicing
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice from index 1 to 5 (5 not included)
print(arr[1:5])  # Output: [2 3 4 5]

# Access indices: 1, 2, 3, 4
```

### Slicing from Start
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice from beginning to index 4 (4 not included)
print(arr[:4])   # Output: [1 2 3 4]

# Same as arr[0:4]
```

### Slicing to End
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice from index 4 to the end
print(arr[4:])   # Output: [5 6 7]

# Same as arr[4:7] for this array
```

### Slice Entire Array
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Get the entire array
print(arr[:])    # Output: [1 2 3 4 5 6 7]

# Same as arr[0:7]
```

### Visual Reference
```
Array:        [1, 2, 3, 4, 5, 6, 7]
Index:         0  1  2  3  4  5  6

arr[1:5]  →  [2, 3, 4, 5]      (indices 1,2,3,4)
arr[:4]   →  [1, 2, 3, 4]      (indices 0,1,2,3)
arr[4:]   →  [5, 6, 7]         (indices 4,5,6)
arr[:]    →  [1, 2, 3, 4, 5, 6, 7]  (all elements)
```

---

## Negative Slicing

### Concept
Negative indices count from the **end** of the array. Use them to slice elements from the end without knowing the array length.

### How Negative Indexing Works
```
Array:              [1, 2, 3, 4, 5, 6, 7]
Positive Index:      0  1  2  3  4  5  6
Negative Index:     -7 -6 -5 -4 -3 -2 -1

-1 = last element
-2 = second-to-last
-3 = third-to-last, etc.
```

### Example: Negative Slicing
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice from index -3 to -1 (last 3 elements, excluding the very last)
print(arr[-3:-1])  # Output: [5 6]

# From 3rd-to-last to 2nd-to-last (not including -1)
```

### More Examples
```python
arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Last 3 elements
print(arr[-3:])     # Output: [50 60 70]

# Everything except the last 2 elements
print(arr[:-2])     # Output: [10 20 30 40 50]

# From index -5 to -2
print(arr[-5:-2])   # Output: [30 40 50]
```

### Advantages
- No need to calculate array length
- More intuitive for accessing end portions
- Dynamic indexing for variable-length arrays

---

## Step in Slicing

### Concept
The **step** parameter determines how many elements to skip. A step of:
- **2** = take every 2nd element
- **3** = take every 3rd element
- **-1** = reverse the array
- **-2** = reverse and take every 2nd element

### Syntax
```python
array[start:end:step]
```

### Example: Every 2nd Element
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# From index 1 to 5, take every 2nd element
print(arr[1:5:2])  # Output: [2 4]

# Indices: 1, 3 (step by 2)
```

### Example: Every nth Element
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Take every 2nd element from entire array
print(arr[::2])    # Output: [1 3 5 7]

# Indices: 0, 2, 4, 6 (start=0, end=7, step=2)
```

### Example: Every 3rd Element
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Take every 3rd element
print(arr[::3])    # Output: [1 4 7]

# Indices: 0, 3, 6
```

### Reversing with Negative Step
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Reverse the array
print(arr[::-1])   # Output: [7 6 5 4 3 2 1]

# Step = -1, goes backwards

# Reverse every 2nd element
print(arr[::-2])   # Output: [7 5 3 1]
```

### Visual Reference
```
Array:          [1, 2, 3, 4, 5, 6, 7]
Index:           0  1  2  3  4  5  6

arr[1:5:2]  →  [2, 4]           (1→3, step 2)
arr[::2]    →  [1, 3, 5, 7]     (every 2nd)
arr[::3]    →  [1, 4, 7]        (every 3rd)
arr[::-1]   →  [7, 6, 5, 4, 3, 2, 1]  (reversed)
arr[::-2]   →  [7, 5, 3, 1]     (reversed, every 2nd)
```

---

## 2-D Array Slicing

### Concept
2-D arrays (matrices) require slicing on two dimensions: **rows** and **columns**.

### Syntax
```python
array[row_slice, column_slice]
```

### Visual Structure
```
Array: [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10]]

Rows:     0                    1
Cols:     0  1  2  3  4        0  1  2  3  4
```

### Example 1: Slice Row and Column
```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

# From 2nd row (index 1), slice columns 1 to 4 (4 not included)
print(arr[1, 1:4])  # Output: [7 8 9]

# Row 1, columns 1,2,3
```

### Example 2: Slice Rows and Columns
```python
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

# From both rows, slice columns 1 to 4
print(arr[0:2, 1:4])

# Output:
# [[2 3 4]
#  [7 8 9]]

# All rows, columns 1,2,3
```

### Example 3: Get Single Column
```python
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

# From all rows, get column 2
print(arr[0:2, 2])  # Output: [3 9]

# Or simply: arr[:, 2]
```

### Example 4: Get Multiple Columns
```python
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

# Get all rows, columns 1 to 3
print(arr[:, 1:3])

# Output:
# [[2 3]
#  [7 8]]
```

### Slicing Rules for 2-D
- **First parameter** = Row slicing
- **Second parameter** = Column slicing
- Use `:` alone to select all in that dimension
- Combine with `start:end:step` for both

### Common 2-D Slicing Patterns
```python
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

arr[0]        # First row: [1 2 3 4 5]
arr[1]        # Second row: [6 7 8 9 10]
arr[:, 0]     # First column: [1 6]
arr[:, -1]    # Last column: [5 10]
arr[0, :]     # First row (explicit): [1 2 3 4 5]
arr[:, 1:4]   # All rows, columns 1-3: [[2 3 4] [7 8 9]]
arr[::2, ::2] # Every 2nd row/column
```

---

## Key Concepts

### 1. **Inclusive Start, Exclusive End**
- Start index is included
- End index is excluded
- `arr[1:4]` includes indices 1, 2, 3 (NOT 4)

### 2. **Default Values**
- Omitted start → 0
- Omitted end → array length
- Omitted step → 1

### 3. **Step Control**
- Positive step: moves forward
- Negative step: moves backward (reverses)
- Step size determines element spacing

### 4. **Negative Indices**
- `-1` = last element
- `-2` = second-to-last, etc.
- Works in both start and end positions

### 5. **2-D Slicing**
- First index = rows
- Second index = columns
- Each can be a simple index or a slice

### 6. **Memory Efficiency**
- Slices are typically **views**, not copies
- Modifying a slice might affect the original array
- Use `.copy()` if you need a separate array

---

## Practical Examples

### Example 1: Extract Test Scores
```python
import numpy as np

# Student scores: rows=students, cols=subjects
scores = np.array([[85, 90, 88, 92],    # Student 1
                   [92, 87, 91, 89],    # Student 2
                   [78, 85, 80, 83]])   # Student 3

# Get scores for Student 2
student2_scores = scores[1, :]          # [92 87 91 89]

# Get Math and Science scores for all students
math_science = scores[:, [0, 2]]        # First and 3rd columns

# Get last 2 students' all scores
last_two = scores[1:3, :]               # Last 2 rows
```

### Example 2: Work with Time Series Data
```python
import numpy as np

# Daily temperature readings for 7 days
temperatures = np.array([22, 24, 23, 25, 26, 24, 22])

# First 3 days
first_3_days = temperatures[:3]         # [22 24 23]

# Every other day
alternate_days = temperatures[::2]      # [22 23 26 22]

# Last 3 days
last_3_days = temperatures[-3:]         # [24 22]

# Exclude first and last day
middle_days = temperatures[1:-1]        # [24 23 25 26 24]
```

### Example 3: Image Data Processing
```python
import numpy as np

# Image: 10x10 pixels, each with RGB values
# Shape: (10, 10, 3)
# Assume 'image' is already loaded

# Get top-left 5x5 region
region = image[:5, :5, :]

# Get red channel only
red_channel = image[:, :, 0]

# Get specific row (horizontal line)
row = image[5, :, :]

# Every 2nd row and column (downsampling)
downsampled = image[::2, ::2, :]
```

### Example 4: Extract Even and Odd Positioned Elements
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Even positioned (indices 0, 2, 4, ...)
even_pos = arr[::2]     # [1 3 5 7 9]

# Odd positioned (indices 1, 3, 5, ...)
odd_pos = arr[1::2]     # [2 4 6 8 10]

# Reverse order
reversed_arr = arr[::-1] # [10 9 8 7 6 5 4 3 2 1]

# Last 5 elements
last_5 = arr[-5:]       # [6 7 8 9 10]
```

---

## Slicing vs. Indexing

### Quick Comparison

| Aspect | Indexing | Slicing |
|--------|----------|---------|
| **Elements Returned** | Single element | Multiple elements (subarray) |
| **Syntax** | `array[index]` | `array[start:end:step]` |
| **Return Type** | Scalar or single value | Array |
| **Speed** | Slightly faster | Slightly slower (multiple elements) |
| **Use Case** | Access one element | Extract a range of elements |
| **Example** | `arr[2]` → `3` | `arr[1:4]` → `[2 3 4]` |

### Code Example
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# INDEXING - Get single element
single = arr[2]         # 30 (type: numpy.int64)

# SLICING - Get range of elements
subset = arr[1:4]       # [20 30 40] (type: numpy.ndarray)

# INDEXING - 2-D single element
matrix = np.array([[1, 2, 3], [4, 5, 6]])
element = matrix[1, 2]  # 6

# SLICING - 2-D range
submatrix = matrix[0:2, 1:3]  # [[2 3] [5 6]]
```

---

## Common Mistakes and Solutions

### ❌ Mistake 1: Forgetting End is Exclusive
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr[0:3])  # [1 2 3] - includes 0,1,2 but NOT 3
```

### ❌ Mistake 2: Confusing Rows and Columns
```python
matrix = np.array([[1, 2], [3, 4]])
print(matrix[0, 1])  # 2 - row 0, column 1 (correct)
print(matrix[1, 0])  # 3 - row 1, column 0 (different!)
```

### ❌ Mistake 3: Wrong Step Direction
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr[4:1])     # [] - empty! Goes forward but start > end
print(arr[4:1:-1])  # [5 4 3] - correct way to reverse slice
```

---

## Summary

| Concept | Syntax | Example | Output |
|---------|--------|---------|--------|
| Basic Slice | `[start:end]` | `arr[1:4]` | Elements at indices 1,2,3 |
| From Start | `[:end]` | `arr[:3]` | First 3 elements |
| To End | `[start:]` | `arr[2:]` | From index 2 onwards |
| With Step | `[start:end:step]` | `arr[::2]` | Every 2nd element |
| Negative Index | `[-n]` | `arr[-1]` | Last element |
| Negative Slice | `[start:end]` | `arr[-3:-1]` | 3rd and 2nd from last |
| Reverse | `[::-1]` | `arr[::-1]` | Reversed array |
| 2-D Slice | `[rows, cols]` | `arr[0:2, 1:3]` | Submatrix |

---

## Next Steps
- Master **Advanced Indexing** (Boolean, Fancy indexing)
- Learn **Array Reshaping** and Flattening
- Explore **Broadcasting** for element-wise operations
- Apply slicing in real-world data cleaning tasks

---

## 📝 Tips for Effective Slicing
1. **Remember**: Start is inclusive, end is exclusive
2. **Use negative indices** for cleaner "from the end" operations
3. **Use step** for sampling and filtering operations
4. **Combine indexing and slicing** for powerful data access
5. **Test with small arrays** to verify slice results before applying to large data

---

**Happy Slicing! 🚀**
