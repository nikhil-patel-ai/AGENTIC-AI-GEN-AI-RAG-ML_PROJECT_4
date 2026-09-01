# NumPy: linspace and identity

This notebook covers two important NumPy functions for array creation: **linspace** and **identity**.

---

## 1. linspace() - Linearly Spaced Arrays

### What is linspace?

`linspace()` creates an array of **evenly spaced numbers** over a specified interval. It's also called "linearly spaced" or "linearly separable" because it divides a range into equal intervals.

### Syntax

```python
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
```

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| **start** | Starting value of the interval | Required |
| **stop** | End value of the interval | Required |
| **num** | Number of samples to generate | 50 |
| **endpoint** | If True, stop is the last sample | True |
| **retstep** | If True, return (array, step) | False |
| **dtype** | Data type of output array | None |
| **axis** | Axis along which to place samples | 0 |

### How it Works

The function divides the interval `[start, stop]` into `num` equal parts and returns the endpoints of these divisions.

**Step Size Calculation:**
```
step = (stop - start) / (num - 1)
```

### Examples

#### Example 1: Basic linspace
```python
import numpy as np

# Create 10 evenly spaced points between -10 and 10
result = np.linspace(-10, 10, 10)
# Output: [-10. -7.77777778 -5.55555556 -3.33333333 -1.11111111 1.11111111 3.33333333 5.55555556 7.77777778 10.]
```

**Explanation:**
- Start: -10
- Stop: 10
- Number of points: 10
- Interval step: (10 - (-10)) / (10 - 1) = 20 / 9 ≈ 2.222

#### Example 2: Different interval
```python
# Create 6 evenly spaced points between -2 and 12
result = np.linspace(-2, 12, 6)
# Output: [-2. 2. 6. 10. 12.]
```

**Explanation:**
- The interval [−2, 12] is divided into 6 equal parts
- Step: (12 - (-2)) / (6 - 1) = 14 / 5 = 2.8
- Points: -2, 0, 2.8, 5.6, 8.4, 12

### Common Use Cases

1. **Creating x-axis for plotting**
   ```python
   x = np.linspace(0, 2*np.pi, 100)  # 100 points from 0 to 2π
   y = np.sin(x)  # Calculate sine values
   ```

2. **Generating test data**
   ```python
   test_points = np.linspace(0, 100, 50)  # 50 evenly spaced test values
   ```

3. **Creating sequences with specific number of points**
   ```python
   temperatures = np.linspace(0, 100, 11)  # 11 points from 0 to 100 (0, 10, 20, ..., 100)
   ```

### linspace vs arange

| Feature | linspace | arange |
|---------|----------|--------|
| Specifies | Number of points | Step size |
| Endpoint included | Yes (by default) | No (by default) |
| Floating-point safe | Yes | Can have precision issues |
| Use case | When you know how many points you need | When you know the step size |

---

## 2. identity() - Identity Matrix

### What is an Identity Matrix?

An **identity matrix** is a square matrix where:
- All **diagonal elements** (where row index = column index) are **1**
- All **non-diagonal elements** are **0**

It's denoted as **I** and is the matrix equivalent of the number 1 in multiplication.

### Mathematical Properties

For an identity matrix I:
- **I × A = A** (any matrix multiplied by I returns itself)
- **A × I = A** (left or right multiplication)
- The determinant of I is always 1
- I is invertible: **I⁻¹ = I**

### Syntax

```python
np.identity(n, dtype=None)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| **n** | Size of the n×n identity matrix |
| **dtype** | Data type of the array (default: float64) |

### Examples

#### Example 1: 3×3 Identity Matrix
```python
result = np.identity(3)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

#### Example 2: 6×6 Identity Matrix
```python
result = np.identity(6)
# Output:
# [[1. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 1.]]
```

#### Example 3: Identity Matrix with Different Data Type
```python
result = np.identity(3, dtype=int)
# Output:
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
```

### Common Use Cases

1. **Linear Algebra Operations**
   ```python
   A = np.array([[1, 2], [3, 4]])
   I = np.identity(2)
   result = A @ I  # Matrix multiplication (result equals A)
   ```

2. **Initializing matrices**
   ```python
   # Start with identity and modify
   transition_matrix = np.identity(5)
   transition_matrix[0, 1] = 0.3  # Add transition probability
   ```

3. **Testing matrix operations**
   ```python
   # Verify that a matrix times its inverse equals identity
   A = np.array([[2, 1], [1, 2]])
   A_inv = np.linalg.inv(A)
   result = A @ A_inv  # Should be approximately I
   ```

4. **Creating augmented matrices**
   ```python
   # For solving systems of linear equations
   augmented = np.hstack([A, np.identity(n)])
   ```

---

## Summary Table

### linspace
- **Purpose:** Create evenly spaced numbers in an interval
- **Input:** Start, stop, and number of points
- **Output:** 1D array of n values
- **Use when:** You know how many points you need
- **Example:** `np.linspace(0, 10, 5)` → [0., 2.5, 5., 7.5, 10.]

### identity
- **Purpose:** Create an identity (unit) matrix
- **Input:** Size n
- **Output:** n×n 2D array with 1s on diagonal, 0s elsewhere
- **Use when:** You need an identity matrix for linear algebra
- **Example:** `np.identity(2)` → [[1., 0.], [0., 1.]]

---

## Key Differences from Similar Functions

### linspace vs linspace with endpoint=False
```python
np.linspace(0, 10, 5)              # [0. 2.5 5. 7.5 10.]
np.linspace(0, 10, 5, endpoint=False)  # [0. 2. 4. 6. 8.]
```

### identity vs eye
```python
np.identity(3)  # Creates identity matrix
np.eye(3)       # Also creates identity matrix (similar function)

# Difference: eye() can have offset diagonals
np.eye(3, k=1)  # 1s on first upper diagonal
```

### identity vs zeros and ones
```python
np.zeros((3, 3))  # All zeros
np.ones((3, 3))   # All ones
np.identity(3)    # 1s on diagonal, 0s elsewhere (specific pattern)
```

---

## Practice Exercises

1. Create a linspace array with 20 points between 0 and 100
2. Create a 4×4 identity matrix
3. Use linspace to create 50 evenly spaced angles between 0 and 2π
4. Create an identity matrix and multiply it with another matrix to verify it returns the same matrix
5. Compare the output of linspace with different numbers of points for the same interval

---

## References

- [NumPy linspace Documentation](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [NumPy identity Documentation](https://numpy.org/doc/stable/reference/generated/numpy.identity.html)
- [Identity Matrix - Wikipedia](https://en.wikipedia.org/wiki/Identity_matrix)

---

## Author Notes

This notebook demonstrates:
- How to import NumPy
- Creating arrays with `linspace()` for specified intervals
- Creating identity matrices with `identity()`
- Practical examples of each function
- Applications in numerical computing and linear algebra

These functions are fundamental tools in NumPy for scientific computing and data analysis.
