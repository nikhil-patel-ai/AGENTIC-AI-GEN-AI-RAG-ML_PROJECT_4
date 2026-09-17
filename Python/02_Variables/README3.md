# Swap Variable in Python - Complete Guide

## Overview
This notebook demonstrates different techniques to swap the values of two variables in Python. The goal is to exchange values between two variables, converting `(a, b = 12, 15)` to `(a, b = 15, 12)`.

---

## Table of Contents
1. [Method 1: Naive Swapping (Incorrect Approach)](#method-1-naive-swapping-incorrect-approach)
2. [Method 2: Using a Temporary Variable](#method-2-using-a-temporary-variable)
3. [Method 3: Arithmetic Operations (Addition/Subtraction)](#method-3-arithmetic-operations)
4. [Method 4: Bitwise XOR Operations](#method-4-bitwise-xor-operations)
5. [Method 5: Tuple Unpacking (Pythonic Way - Recommended)](#method-5-tuple-unpacking-recommended)
6. [Comparison Summary](#comparison-summary)

---

## Method 1: Naive Swapping (Incorrect Approach)

### Code
```python
a = 12
b = 15
print(a, b)  # Output: 12 15

a = b        # a now becomes 15
b = a        # b also becomes 15 (we lost the original value of a)
print(a, b)  # Output: 15 15
```

### Explanation
- **Line 1-2**: Initialize two variables `a = 12` and `b = 15`
- **Line 5**: Assign `b` (15) to `a`, so now `a = 15`
- **Line 6**: Assign `a` (which is now 15) to `b`, so `b = 15`
- **Problem**: The original value of `a` (12) is lost during the process, resulting in both variables having the same value

### Key Takeaway
❌ **This method does NOT work** because we overwrite the first variable's value before we can use it to update the second variable.

---

## Method 2: Using a Temporary Variable

### Code
```python
a1 = 4
b1 = 9
print(a1, b1)  # Output: 4 9

# Step 1: Store the original value of a1
temp = a1      # temp = 4

# Step 2: Assign b1 to a1
a1 = b1        # a1 = 9

# Step 3: Assign the stored value (temp) to b1
b1 = temp      # b1 = 4

print(a1)      # Output: 9
print(b1)      # Output: 4
```

### Explanation
- **Line 1-2**: Initialize `a1 = 4` and `b1 = 9`
- **Line 5**: Create a temporary variable `temp` to preserve the original value of `a1`, so `temp = 4`
- **Line 6**: Now safely assign `b1` to `a1`, resulting in `a1 = 9`
- **Line 7**: Assign the saved value from `temp` to `b1`, resulting in `b1 = 4`
- **Result**: Variables are successfully swapped: `a1 = 9` and `b1 = 4`

### Advantages
✅ Simple and easy to understand  
✅ Works with all data types  
✅ No risk of losing data

### Disadvantages
⚠️ Uses extra memory for the temporary variable  
⚠️ Requires 3 lines of code

---

## Method 3: Arithmetic Operations

### Code
```python
a2 = 12
b2 = 11
print(a2, b2)  # Output: 12 11

# Step 1: Store sum of both numbers in a2
a2 = a2 + b2   # a2 = 12 + 11 = 23

# Step 2: Subtract b2 from the new a2 to get original a2 value
b2 = a2 - b2   # b2 = 23 - 11 = 12

# Step 3: Subtract b2 from the current a2 to get original b2 value
a2 = a2 - b2   # a2 = 23 - 12 = 11

print(a2)      # Output: 11
print(b2)      # Output: 12
```

### Explanation
- **Line 5**: Add both values and store in `a2`: `a2 = 23` (sum of 12 + 11)
- **Line 6**: Subtract the new `b2` from `a2` to recover the original `a2` value: `b2 = 12`
- **Line 7**: Subtract the updated `b2` from `a2` to recover the original `b2` value: `a2 = 11`
- **Result**: Variables are successfully swapped without using extra variables

### Memory Consideration
```python
print(0b101)   # Binary: 101 = 5
print(0b110)   # Binary: 110 = 6
print(bin(11)) # Binary: 1011 = 4 bits (extra bit required!)
print(0b1011)  # This is 11 in binary
```

### Key Insight
⚠️ **Memory Issue**: When adding two numbers, the result may require more bits to store. For example:
- `101` (5) + `110` (6) = `1011` (11)
- The result requires 4 bits instead of 3, wasting 1 extra bit of memory

### Advantages
✅ No temporary variable needed  
✅ Works well for small numbers

### Disadvantages
⚠️ May cause integer overflow with very large numbers  
⚠️ Wastes extra memory for intermediate results  
⚠️ Not intuitive

---

## Method 4: Bitwise XOR Operations

### Code
```python
a2 = 12
b2 = 11

# Step 1: XOR a2 and b2, store result in a2
a2 = a2 ^ b2   # XOR operation

# Step 2: XOR new a2 with b2, store result in b2
b2 = a2 ^ b2   # This recovers original a2

# Step 3: XOR new a2 with updated b2, store result in a2
a2 = a2 ^ b2   # This recovers original b2

print(a2)      # Output: 11
print(b2)      # Output: 12
```

### How XOR Works
The XOR (Exclusive OR) operator has a unique property:
- `a ^ b ^ b = a` (XORing a number with itself twice returns the original number)

### Binary Example
```
a2 = 12 = 1100 (binary)
b2 = 11 = 1011 (binary)

Step 1: a2 = a2 ^ b2 = 1100 ^ 1011 = 0111 (7 in decimal)
Step 2: b2 = a2 ^ b2 = 0111 ^ 1011 = 1100 (12 in decimal) ← recovers original a2
Step 3: a2 = a2 ^ b2 = 0111 ^ 1100 = 1011 (11 in decimal) ← recovers original b2
```

### Advantages
✅ No temporary variable needed  
✅ No extra memory waste (XOR always produces result same size as operands)  
✅ Efficient bit-level operation

### Disadvantages
⚠️ Complex and hard to understand  
⚠️ Not commonly used in modern Python  
⚠️ Only works with integers

---

## Method 5: Tuple Unpacking (Recommended) ⭐

### Code
```python
a2 = 12
b2 = 11

# Python's built-in swapping mechanism
a2, b2 = b2, a2   # Both variables swap in one line!

print(a2)  # Output: 11
print(b2)  # Output: 12
```

### Explanation
- **Line 1-2**: Initialize `a2 = 12` and `b2 = 11`
- **Line 5**: Python creates a temporary tuple `(b2, a2)` on the right side, then unpacks it to `a2, b2` on the left side
- This is handled entirely by Python's interpreter, which is optimized for this operation
- **Result**: Clean and efficient swap in a single line

### Why This is the Best Method

#### Pythonic
This is the recommended way to swap variables in Python, embracing the language's elegance and readability.

#### Efficient
Python's interpreter handles tuple packing/unpacking efficiently without creating actual intermediate tuples.

#### Works with All Data Types
```python
# Strings
x, y = "hello", "world"
x, y = y, x  # x = "world", y = "hello"

# Lists
list1, list2 = [1, 2, 3], [4, 5, 6]
list1, list2 = list2, list1

# Different types
a, b = 42, "string"
a, b = b, a  # a = "string", b = 42
```

#### Readable and Concise
One line of code that clearly expresses intent.

### Advantages
✅ Most Pythonic approach  
✅ Works with any data type  
✅ Highly readable and concise  
✅ No extra variables needed  
✅ Optimized by Python interpreter  
✅ Best performance

### Disadvantages
❌ None! This is the recommended method.

---

## Comparison Summary

| Method | Code Lines | Memory Used | Easy to Understand | Performance | Works with All Types |
|--------|-----------|------------|-------------------|-------------|----------------------|
| **Method 1: Naive** | 2 | Low | ✅ High | ⚡ Fast | ✅ Yes | ❌ **No** |
| **Method 2: Temporary** | 3 | Medium | ✅ High | ⚡ Fast | ✅ Yes |
| **Method 3: Arithmetic** | 3 | Medium | ❌ Low | ⚡ Fast | ❌ Numbers only |
| **Method 4: XOR** | 3 | Low | ❌ Very Low | ⚡ Fast | ❌ Integers only |
| **Method 5: Tuple** | 1 | Low | ✅ Very High | ⚡⚡ Fastest | ✅ Yes |

---

## Conclusion

### Best Practice Recommendation
**Always use Method 5 (Tuple Unpacking)** in Python:

```python
a, b = b, a
```

This method is:
- ✅ Pythonic and idiomatic
- ✅ Most efficient and readable
- ✅ Universally compatible with any data type
- ✅ The professional standard in Python development

---

## Practice Exercises

1. **Swap two numbers using tuple unpacking**
2. **Swap three variables: a, b, c = b, c, a**
3. **Swap variables inside a list or function**
4. **Compare execution time of all methods**

---

## Additional Resources

- Python Official Documentation on Tuple Unpacking
- Memory efficiency in Python variable operations
- Bitwise operations and XOR operators
- Python best practices for variable manipulation

---

**Created for Python Learning Journey** | Notebook: SwapVariable.ipynb
