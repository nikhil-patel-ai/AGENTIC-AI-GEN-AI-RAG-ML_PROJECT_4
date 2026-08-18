# List Data Structure - Complete Guide

## 📚 Table of Contents
1. [Overview](#overview)
2. [Key Characteristics](#key-characteristics)
3. [Creating Lists](#creating-lists)
4. [Accessing Elements](#accessing-elements)
5. [List Methods](#list-methods)
6. [List Operations](#list-operations)
7. [Advanced Concepts](#advanced-concepts)

---

## Overview

A **List** in Python is an ordered, mutable collection that can store multiple items of different data types. Lists are one of the most versatile and commonly used data structures in Python programming. They are represented by square brackets `[]` and elements are separated by commas.

### Why Use Lists?
- **Flexible**: Store any type of data
- **Dynamic**: Easily add or remove elements
- **Ordered**: Maintain insertion order
- **Efficient**: Fast access to elements by index
- **Powerful**: Rich set of built-in methods

---

## Key Characteristics

| Characteristic | Description |
|---|---|
| **Ordered** | Elements maintain their position/index in the list |
| **Mutable** | Lists can be modified after creation (add, remove, change elements) |
| **Heterogeneous** | Can contain items of different data types (int, float, str, complex, bool, nested lists, etc.) |
| **Indexed** | Elements are accessed using zero-based indexing (0, 1, 2, ...) |
| **Allows Duplicates** | The same value can appear multiple times in a list |
| **Dynamic Size** | Size can be changed at runtime |

---

## Creating Lists

### 1. Empty List
```python
l = []              # Create an empty list
type(l)             # Returns: <class 'list'>
len(l)              # Returns: 0
```

### 2. List with Integer Values
```python
list2 = [10, 30, 60]
# Represents a list of integers
```

### 3. List with Float Values
```python
list3 = [10.77, 30.66, 60.89]
# Represents a list of floating-point numbers
```

### 4. List with String Values
```python
list4 = ['one', 'two', 'three']
# Represents a list of strings
```

### 5. List with Mixed Data Types
```python
list6 = [100, 'Nikhil', 17.765]  # Mixed types
# Integers, strings, and floats in one list
```

### 6. List with Nested Lists
```python
list5 = ['Nikhil', 21, [50, 100], [150, 90]]
# Lists can contain other lists (nested lists)
```

### 7. List with Multiple Data Types (Including Collections)
```python
list7 = ['Nikhil', 21, [70, 700], [50, 900], {'Nikhil', 'Kumar'}]
# Can contain lists, sets, and other data types
```

### 8. List with Various Data Types
```python
l1 = [10, 3.5, True, 1+3j, 'hello']
# Integers, floats, booleans, complex numbers, and strings
```

---

## Accessing Elements

### Forward Indexing
Access elements from the beginning of the list using positive indices (0, 1, 2, ...).

```python
lst1 = [10, 20, 40, 80, 'Hello']

lst1[0]      # Returns: 10 (first element)
lst1[1]      # Returns: 20 (second element)
lst1[4]      # Returns: 'Hello' (last element)
```

### Backward Indexing
Access elements from the end of the list using negative indices (-1, -2, -3, ...).

```python
lst1 = [10, 20, 40, 80, 'Hello']

lst1[-1]     # Returns: 'Hello' (last element)
lst1[-2]     # Returns: 80 (second-to-last element)
lst1[-5]     # Returns: 10 (first element)
```

### Nested Indexing
Access elements within nested lists using multiple indices.

```python
l1 = [10, 3.5, True, 1+3j, 'hello', [1, 2, 3, 4]]

l1[5]        # Returns: [1, 2, 3, 4]
l1[5][0]     # Returns: 1 (first element of nested list)
l1[5][2]     # Returns: 3 (third element of nested list)
```

### Slicing
Extract a portion of the list using the slice syntax `list[start:end:step]`.

#### Basic Slicing
```python
l1 = [10, 3.5, True, 1+3j, 'hello', [1, 2, 3, 4]]

l1[:]        # Returns entire list
l1[:3]       # Returns: [10, 3.5, True] (from index 0 to 2)
l1[3:]       # Returns: [1+3j, 'hello', [1, 2, 3, 4]] (from index 3 to end)
```

#### Slicing with Step
```python
l1 = [10, 3.5, True, 1+3j, 'hello', [1, 2, 3, 4]]

l1[0:5:2]    # Returns: [10, True, 'hello'] (every 2nd element)
l1[::2]      # Returns: [10, True, 'hello', [1, 2, 3, 4]] (every 2nd element)
```

#### Backward Slicing
```python
l1 = [10, 3.5, True, 1+3j, 'hello', [1, 2, 3, 4]]

l1[-3:]      # Returns: ['hello', [1, 2, 3, 4]] (last 3 elements)
l1[-3]       # Returns: 1+3j (3rd element from end)
l1[::-1]     # Returns: [[1,2,3,4], 'hello', 1+3j, True, 3.5, 10] (reversed)
l1[::-2]     # Returns: [[1,2,3,4], 1+3j, 3.5] (reversed, every 2nd)
```

---

## List Methods

### 1. `append(element)`
Adds a **single element** to the end of the list.

```python
l = []
l.append(10)     # l = [10]
l.append(20)     # l = [10, 20]
l.append(30)     # l = [10, 20, 30]
len(l)           # Returns: 3
```

**Important**: `append()` accepts only ONE argument at a time.

```python
l.append(20, 30, 40)  # ❌ Error! Only one argument allowed
```

### 2. `extend(iterable)`
Adds **multiple elements** from an iterable (list, tuple, etc.) to the end of the list.

```python
l = [10, 20, 30]
l2 = [40, 50, 60]
l.extend(l2)     # l = [10, 20, 30, 40, 50, 60]

a1 = [1, 2, 3]
b1 = [4, 5, 6]
a1.extend(b1)    # a1 = [1, 2, 3, 4, 5, 6]
```

### 3. `insert(index, element)`
Inserts an element at a **specific index** in the list.

```python
l2 = [100, 20, 30]
l2.insert(2, 25)      # l2 = [100, 20, 25, 30]
l2.insert(2, [1, 2, 3])  # Can insert lists: [100, 20, [1,2,3], 25, 30]
```

**Note**: `insert()` accepts only one element at a time.

### 4. `pop([index])`
Removes and **returns** an element at the specified index. If no index is provided, removes the **last element**.

```python
l2 = [100, 20, 25, 30, 40, [1, 2, 3]]

l2.pop()         # Returns: [1, 2, 3], l2 = [100, 20, 25, 30, 40]
l2.pop()         # Returns: 40, l2 = [100, 20, 25, 30]
l2.pop(2)        # Returns: 25, l2 = [100, 20, 30]
```

### 5. `remove(value)`
Removes the **first occurrence** of a value from the list (by value, not index).

```python
l = [10, 20, 30, 40, 50, 10, 10, 3.5, True, (1+3j), 'hello', [1, 2, 3, 4]]

l.remove(10)     # Removes first 10: [20, 30, 40, 50, 10, 10, 3.5, True, ...]
# Only the first occurrence is removed
```

### 6. `index(value)`
Returns the **index** of the first occurrence of a value.

```python
l = [10, 20, 30, 10, 40]

l.index(20)      # Returns: 1
l.index(10)      # Returns: 0 (first occurrence)
l1.index('hello')  # Returns the index of 'hello'
```

### 7. `count(value)`
Returns the **number of times** a value appears in the list.

```python
l = [10, 10, 10, 20, 30, 40, 50, 10, 10]

l.count(10)      # Returns: 5
l.count(30)      # Returns: 1
l.count(100)     # Returns: 0 (not in list)
```

### 8. `sort([reverse=False])`
Sorts the list **in-place** in ascending order. Use `reverse=True` for descending order.

```python
lstn = [9, 5, 2, 99, 12, 88, 34]
lstn.sort()           # [2, 5, 9, 12, 34, 88, 99]

l = ['30', '10', '20', '40', '50']
l.sort()              # ['10', '20', '30', '40', '50']

lstn.sort(reverse=True)  # [99, 88, 34, 12, 9, 5, 2]
```

**Note**: `sort()` modifies the original list.

### 9. `sorted(list)`
Returns a **new sorted list** without modifying the original.

```python
lst3 = [88, 65, 33, 21, 11, 98]
sorted_list = sorted(lst3)  # [11, 21, 33, 65, 88, 98]
print(lst3)  # Original unchanged: [88, 65, 33, 21, 11, 98]
```

### 10. `reverse()`
Reverses the list **in-place**.

```python
l3 = ['a', 'b', 'c', 'd']
l3.reverse()     # ['d', 'c', 'b', 'a']
```

**Alternative**: Use slicing `l1[::-1]` to reverse without modifying original.

### 11. `copy()`
Creates a **shallow copy** of the list.

```python
l = [10, 20, 30, 40, 50]
l3 = l.copy()    # l3 = [10, 20, 30, 40, 50]

l == l3          # True (same values)
id(l) == id(l3)  # False (different objects)
```

### 12. `clear()`
Removes **all elements** from the list.

```python
l3 = [10, 20, 30]
l3.clear()       # l3 = []
len(l3)          # Returns: 0
```

---

## List Operations

### 1. Update/Modify Elements
Change the value at a specific index.

```python
l2 = [10, 20, 30]
l2[0] = 100      # l2 = [100, 20, 30]

l1 = [10, 3.5, True, 1+3j, 'hello', [1,2,3,4]]
l1[0] = 100      # l1 = [100, 3.5, True, 1+3j, 'hello', [1,2,3,4]]
```

### 2. Join/Concatenate Lists
Combine two or more lists using the `+` operator or `extend()`.

```python
list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six', 'seven', 'eight']

# Method 1: Using + operator
list3 = list1 + list2  # Creates new list
# list3 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

# Method 2: Using extend()
list1.extend(list2)    # Modifies list1
# list1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
```

### 3. Check Membership (in/not in)
Check if an element exists in the list.

```python
l = [10, 10, 10, 20, 30, 40, 50]

10 in l          # Returns: True
40 in l          # Returns: True
100 in l         # Returns: False
100 not in l     # Returns: True
```

### 4. Delete Elements
Remove elements using `del` keyword or `pop()`/`remove()` methods.

```python
l3 = [10, 20, 30]
del l3           # Deletes the entire list

l3 = [10, 20, 30]
del l3[0]        # Deletes element at index 0
# l3 = [20, 30]
```

---

## Advanced Concepts

### 1. Iterating Through Lists

#### Using `for` loop
```python
l = [10, 10, 10, 20, 30, 40, 50]

for i in l:
    print(i)
# Output:
# 10
# 10
# 10
# 20
# 30
# 40
# 50
```

#### Using `enumerate()`
Get both index and value while iterating.

```python
l = [10, 10, 10, 20, 30, 40, 50]

for i in enumerate(l):
    print(i)
# Output:
# (0, 10)
# (1, 10)
# (2, 10)
# (3, 20)
# (4, 30)
# (5, 40)
# (6, 50)
```

### 2. List Comprehension
Create lists concisely using list comprehensions.

```python
# Basic list comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_numbers = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### 3. Nested Lists
Lists containing other lists.

```python
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

nested[0]        # [1, 2, 3]
nested[0][1]     # 2
nested[1][2]     # 6
```

---

## Common List Operations Summary

| Operation | Example | Result |
|---|---|---|
| Create | `l = [1, 2, 3]` | Creates list |
| Access | `l[0]` | Returns first element |
| Slice | `l[1:3]` | Returns subset |
| Add element | `l.append(4)` | Adds to end |
| Insert | `l.insert(1, 10)` | Inserts at index |
| Remove | `l.remove(2)` | Removes by value |
| Pop | `l.pop()` | Removes and returns last |
| Sort | `l.sort()` | Sorts in place |
| Reverse | `l.reverse()` | Reverses in place |
| Find | `l.index(2)` | Returns index |
| Count | `l.count(2)` | Returns occurrences |
| Copy | `l.copy()` | Creates shallow copy |
| Clear | `l.clear()` | Removes all elements |
| Join | `l1 + l2` or `l1.extend(l2)` | Combines lists |
| Check | `2 in l` | Returns boolean |

---

## Tips & Best Practices

1. **Use `append()`** for adding single elements
2. **Use `extend()`** for adding multiple elements from another iterable
3. **Use `insert()`** when you need to add at a specific position
4. **Use `pop()`** when you need the removed value
5. **Use `remove()`** when you know the value but not the index
6. **Lists are mutable** - they can be changed after creation
7. **Indexing is zero-based** - first element is at index 0
8. **Use negative indices** to access from the end
9. **Slicing creates new lists** - doesn't modify the original (with `[:]`)
10. **Be careful with nested lists** - modifying inner lists affects all references

---

## Conclusion

Lists are fundamental to Python programming. Master these methods and operations to efficiently manipulate data in your Python projects!

### Indexing
Access individual elements by position (zero-based indexing).
```python
l1 = [10, 3.5, True, 1+3j, 'hello', [1, 2, 3, 4]]
l1[0]    # Returns: 10
l1[2]    # Returns: True
l1[-3]   # Returns: 1+3j (third from the end)
```

### Slicing
Extract a range of elements.
```python
l1[:3]       # [10, 3.5, True]
l1[3:]       # [1+3j, 'hello', [1, 2, 3, 4]]
l1[0:5:2]    # [10, True, 'hello']
l1[::-1]     # Reverse the list
l1[::-2]     # Reverse with step 2
```

### Nested List Access
Access elements within nested lists.
```python
l1[4]          # Returns: 'hello'
l1[5]          # Returns: [1, 2, 3, 4]
l1[5][0]       # Returns: 1
l1[5][3]       # Returns: 4
```

## Modifying Elements

### Assignment
Change an element's value by index.
```python
l1 = [10, 3.5, True, 1+3j, 'hello', [1, 2, 3, 4]]
l1[0] = 100    # l1 = [100, 3.5, True, 1+3j, 'hello', [1, 2, 3, 4]]
```

## List Methods

### count()
Returns the number of times a value appears in the list.
```python
l = [10, 20, 30, 40, 50, 10]
l.count(10)    # Returns: 2
l.count(30)    # Returns: 1
```

### index()
Returns the index of the first occurrence of a value.
```python
l = [10, 20, 30, 40, 50]
l.index(20)    # Returns: 1
l.index(40)    # Returns: 3
```

### copy()
Creates a shallow copy of the list.
```python
l = [10, 20, 30, 40, 50]
l3 = l.copy()
# l and l3 have the same values but different identities
l == l3        # True (equal values)
id(l) == id(l3)  # False (different objects)
```

### clear()
Removes all elements from the list.
```python
l3 = [1, 2, 3]
l3.clear()     # l3 = []
```

## Deleting Elements

### del statement
Deletes a variable or element.
```python
l = [10, 20, 30]
del l          # Deletes the entire list
l              # NameError: name 'l' is not defined
```

## Comparison and Identity

### Equality (==)
Compares values.
```python
l = [10, 20, 30]
l3 = l.copy()
l == l3        # True (same values)
```

### Identity (id() and ==)
Compares object identity.
```python
id(l)          # Returns: memory address of l
id(l3)         # Returns: different memory address
id(l) == id(l3)    # False (different objects)
id(l) != id(l3)    # True
```

## Best Practices

1. **Use descriptive variable names** for lists
2. **Check list length** before accessing elements to avoid IndexError
3. **Use slicing** instead of creating new lists when possible
4. **Understand mutability**: Changes to a list affect the original object
5. **Use copy()** when you need an independent copy of a list
6. **Remember zero-based indexing** in Python
7. **Use negative indexing** to access elements from the end

## Common Errors

```python
# IndexError: list index out of range
l = [1, 2, 3]
l[5]  # Error! Only indices 0-2 exist

# TypeError: append() takes exactly one argument
l.append(20, 30, 40)  # Error! Use extend() instead

# NameError: name not defined
del l3
l3  # Error! Variable no longer exists
```

## Summary Table

| Method | Purpose | Example |
|--------|---------|---------|
| `append()` | Add single item | `l.append(10)` |
| `extend()` | Add multiple items | `l.extend([20, 30])` |
| `count()` | Count occurrences | `l.count(10)` |
| `index()` | Find first position | `l.index(20)` |
| `copy()` | Create shallow copy | `l2 = l.copy()` |
| `clear()` | Remove all items | `l.clear()` |
| Slicing `[:]` | Extract range | `l[1:3]` |
| Indexing `[]` | Access by position | `l[0]` |

## References
- [Python Official Documentation - Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
