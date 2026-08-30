# NumPy Array Indexing

## 📚 Overview
This section covers **Array Indexing** in NumPy, which is a fundamental concept for accessing and manipulating elements within NumPy arrays. Indexing allows you to retrieve specific elements from arrays using their position, supporting positive indexing (from the start) and negative indexing (from the end).

---

## 📖 Table of Contents
1. [Introduction](#introduction)
2. [1-D Array Indexing](#1-d-array-indexing)
3. [2-D Array Indexing](#2-d-array-indexing)
4. [3-D Array Indexing](#3-d-array-indexing)
5. [Negative Indexing](#negative-indexing)
6. [Key Concepts](#key-concepts)
7. [Practical Examples](#practical-examples)

---

## Introduction

Array indexing is the process of accessing individual elements within an array by referring to their position or index. In NumPy (and most programming languages), indexing is **0-based**, meaning:
- The **first element** has index **0**
- The **second element** has index **1**
- And so on...

### Why is Indexing Important?
- **Data Access**: Retrieve specific values from large datasets
- **Data Manipulation**: Modify individual or groups of elements
- **Computation**: Perform calculations on specific array elements
- **Data Analysis**: Extract relevant information for analysis

---

## 1-D Array Indexing

### What is a 1-D Array?
A 1-D (one-dimensional) array is essentially a list of elements arranged in a single line.

### Syntax
```python
array[index]
```

### Example
```python
import numpy as np

# Create a 1-D array
arr = np.array([1, 2, 3, 4])

# Access individual elements
print(arr[0])      # Output: 1 (first element)
print(arr[1])      # Output: 2 (second element)
print(arr[2])      # Output: 3 (third element)
print(arr[3])      # Output: 4 (fourth element)

# Perform operations using indexed elements
print(arr[2] + arr[3])  # Output: 7 (add 3rd and 4th elements)
```

### Array Structure
```
Array: [1, 2, 3, 4]
Index:  0  1  2  3
```

### Key Points
- Use **single integer** to access elements
- Index must be between **0** and **length-1**
- Out-of-range indices raise an `IndexError`

---

## 2-D Array Indexing

### What is a 2-D Array?
A 2-D (two-dimensional) array is like a **table or matrix** with rows and columns. It's useful for representing structured data like spreadsheets or images.

### Syntax
```python
array[row_index, column_index]
```

### Visual Representation
```
Array: [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]]

Row Index:    0             1
Column Index: 0 1 2 3 4     0 1 2 3 4
```

### Example
```python
import numpy as np

# Create a 2-D array
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

# Access elements using [row, column]
print('Element at row 0, column 1:', arr[0, 1])    # Output: 2
print('Element at row 1, column 4:', arr[1, 4])    # Output: 10

# Access entire row
print('First row:', arr[0])          # Output: [1 2 3 4 5]
print('Second row:', arr[1])         # Output: [6 7 8 9 10]

# Access entire column
print('First column:', arr[:, 0])    # Output: [1 6]
```

### Understanding the Indexing
- **First index** = Row number (0 for first row, 1 for second row, etc.)
- **Second index** = Column number (0 for first column, 1 for second column, etc.)

### Common Use Cases
- Accessing matrix elements
- Working with image data (images are 2-D arrays of pixels)
- Spreadsheet-like operations
- Data from tables or CSV files

---

## 3-D Array Indexing

### What is a 3-D Array?
A 3-D (three-dimensional) array extends 2-D arrays by adding **depth**. Think of it as a **cube** or a **stack of matrices**. It's useful for:
- RGB images (height × width × 3 channels)
- Time-series data with multiple variables
- 3-D volumetric data (medical imaging)

### Syntax
```python
array[dimension1_index, dimension2_index, dimension3_index]
```

### Visual Representation
```
Array: [[[1, 2, 3],         [[[Index: [0, 0, 0], [0, 0, 1], [0, 0, 2],
         [4, 5, 6]],                  [0, 1, 0], [0, 1, 1], [0, 1, 2]],
        
        [[7, 8, 9],                  [[1, 0, 0], [1, 0, 1], [1, 0, 2],
         [10, 11, 12]]]               [1, 1, 0], [1, 1, 1], [1, 1, 2]]]
```

### Example
```python
import numpy as np

# Create a 3-D array (2 matrices, each with 2 rows and 3 columns)
arr = np.array([[[1, 2, 3], 
                 [4, 5, 6]], 
                
                [[7, 8, 9], 
                 [10, 11, 12]]])

# Access elements using [depth, row, column]
print('Element at [0, 1, 2]:', arr[0, 1, 2])    # Output: 6
print('Element at [1, 0, 1]:', arr[1, 0, 1])    # Output: 8

# Access entire 2-D slice
print('First matrix:', arr[0])
print('Second matrix:', arr[1])
```

### Understanding the Indexing
- **First index** = Depth/Matrix number (which matrix in the stack)
- **Second index** = Row within that matrix
- **Third index** = Column within that row

---

## Negative Indexing

### What is Negative Indexing?
Negative indexing allows you to access array elements **from the end** without knowing the array length. It's very useful for accessing the last elements.

### How It Works
- Index **-1** = Last element
- Index **-2** = Second-to-last element
- Index **-3** = Third-to-last element
- And so on...

### Syntax
```python
array[negative_index]
```

### Example with 1-D Array
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print('Last element:', arr[-1])        # Output: 50
print('Second last:', arr[-2])         # Output: 40
print('Third last:', arr[-3])          # Output: 30
```

### Example with 2-D Array
```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

# Access last element of second row
print('Last element from row 1:', arr[1, -1])     # Output: 10

# Access first element of last row
print('First element from last row:', arr[-1, 0]) # Output: 6

# Access last element overall
print('Last element overall:', arr[-1, -1])       # Output: 10
```

### Visual Reference
```
Array: [1, 2, 3, 4, 5]

Positive Index:  0  1  2  3  4
Negative Index: -5 -4 -3 -2 -1
```

### Advantages of Negative Indexing
- Access elements from the end without calculating array length
- More readable code (arr[-1] is clearer than arr[len(arr)-1])
- Useful in loops and data processing
- Dynamic indexing for variable-sized arrays

---

## Key Concepts

### 1. **Zero-Based Indexing**
- First element is at index 0, not 1
- This is standard in most programming languages

### 2. **Index Range**
- Valid indices: 0 to (array_length - 1)
- Out-of-range indexing raises `IndexError`

### 3. **Dimension-Based Indexing**
- 1-D: Single index
- 2-D: Two indices (row, column)
- 3-D: Three indices (depth, row, column)
- N-D: N indices

### 4. **Positive vs. Negative Indexing**
- Positive: Count from the start (0, 1, 2, ...)
- Negative: Count from the end (-1, -2, -3, ...)

### 5. **Mixed Indexing**
- Can combine positive and negative indices
- Example: `arr[0, -1]` (first row, last column)

---

## Practical Examples

### Example 1: Accessing Student Scores
```python
import numpy as np

# 2-D array: rows = students, columns = subjects
scores = np.array([[85, 90, 88],    # Student 1: Math, English, Science
                   [92, 87, 91],    # Student 2
                   [78, 85, 80]])   # Student 3

# Get Math score of Student 2
math_score = scores[1, 0]           # Output: 92

# Get Science score of last student
science_score = scores[-1, -1]      # Output: 80

# Get all Math scores
all_math = scores[:, 0]             # Output: [85 92 78]
```

### Example 2: Working with RGB Image Data
```python
import numpy as np

# Create a simple 2x2 RGB image (height=2, width=2, channels=3)
image = np.array([[[255, 0, 0],     # Red pixel
                   [0, 255, 0]],    # Green pixel
                  [[0, 0, 255],     # Blue pixel
                   [255, 255, 0]]])  # Yellow pixel

# Get the red channel value of pixel at position [0, 0]
red_value = image[0, 0, 0]          # Output: 255

# Get all RGB values of pixel at [1, 1]
pixel_color = image[1, 1, :]        # Output: [255 255 0]
```

### Example 3: Time Series Data
```python
import numpy as np

# 3-D array: Time periods, Locations, Temperatures (daily highs, lows, avg)
temp_data = np.array([[[25, 15, 20],   # Day 1: Location 1
                       [28, 18, 23]],   # Day 1: Location 2
                      [[26, 16, 21],    # Day 2: Location 1
                       [27, 17, 22]]])  # Day 2: Location 2

# Get average temperature of Location 2 on Day 1
avg_temp = temp_data[0, 1, 2]       # Output: 23

# Get all data for Location 1
location_1 = temp_data[:, 0, :]     # Output: [[25 15 20] [26 16 21]]
```

---

## Summary

| Aspect | Details |
|--------|---------|
| **Indexing Type** | Zero-based (starts at 0) |
| **1-D Syntax** | `array[index]` |
| **2-D Syntax** | `array[row, column]` |
| **3-D Syntax** | `array[depth, row, column]` |
| **Negative Indexing** | `-1` for last, `-2` for second-last, etc. |
| **Error Handling** | Out-of-range indices raise `IndexError` |
| **Use Cases** | Data access, modification, computation, analysis |

---

## Next Steps
- Master **Slicing** to access multiple elements at once
- Learn **Boolean indexing** for conditional element access
- Explore **Fancy indexing** with arrays of indices
- Apply indexing in real-world data processing tasks

---

## 📝 Notes
- Always remember: **Python uses 0-based indexing**, not 1-based
- Use negative indexing for cleaner, more intuitive code when accessing from the end
- Combine indexing with other NumPy operations for powerful data manipulation

---

**Happy Learning! 🚀**
