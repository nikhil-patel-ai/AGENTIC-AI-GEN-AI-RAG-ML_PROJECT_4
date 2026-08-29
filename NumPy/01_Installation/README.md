# NumPy Installation

This section is focused on installing and verifying the NumPy library in Python.

## What is NumPy?

NumPy is a powerful Python library used for numerical computing. It helps in working with arrays, matrices, and mathematical operations efficiently.

It is widely used in:

- Data Science
- Machine Learning
- Artificial Intelligence
- Scientific Computing
- Image Processing
- Signal Processing

---

## Why Use NumPy?

NumPy provides:

- Faster numerical operations than Python lists
- Support for multi-dimensional arrays
- Mathematical and statistical functions
- Easy handling of large datasets
- Compatibility with many data science libraries

---

## Prerequisites

Before installing NumPy, make sure Python is installed on your system.

Check Python version:

```bash
python --version
```

If Python is not installed, install it first from the official Python website.

---

## Install NumPy

Use the following command:

```bash
pip install numpy
```

If you are using Python 3 specifically, you can also use:

```bash
python -m pip install numpy
```

For Windows users, this also works:

```bash
py -m pip install numpy
```

---

## Verify the Installation

After installation, verify it with:

```bash
python -c "import numpy as np; print(np.__version__)"
```

You should see a version number such as:

```text
2.0.0
```

---

## Quick Example

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr * 2)
```

Expected output:

```text
[1 2 3 4 5]
[ 2  4  6  8 10]
```

---

## Common Installation Issues

### 1. pip not recognized
Use:

```bash
python -m pip install numpy
```

### 2. Wrong Python version
Check which Python interpreter is active:

```bash
python -c "import sys; print(sys.executable)"
```

### 3. Virtual environment not activated
If you are using a virtual environment, activate it first and then run:

```bash
pip install numpy
```

---

## Notes

This folder contains the NumPy installation notebook and related learning materials. The main goal is to help learners understand how to install NumPy and confirm that it works correctly before starting array operations.

---

## Next Topics in NumPy

After installation, you can continue with:

- Creating arrays
- Array indexing
- Array slicing
- Reshaping arrays
- Mathematical operations

---

## Reference

NumPy official website: https://numpy.org
