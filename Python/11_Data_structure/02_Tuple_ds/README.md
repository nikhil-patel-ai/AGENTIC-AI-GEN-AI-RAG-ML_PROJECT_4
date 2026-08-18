# Tuple Data Structure (TupleDS)

## Overview
This notebook provides a comprehensive guide to **Tuples** in Python, one of the fundamental data structures. Tuples are immutable, ordered collections of elements that can contain different data types.

## Table of Contents
1. [What is a Tuple?](#what-is-a-tuple)
2. [Tuple Creation](#tuple-creation)
3. [Tuple Indexing](#tuple-indexing)
4. [Tuple Slicing](#tuple-slicing)
5. [Tuple Methods](#tuple-methods)
6. [Tuple Membership](#tuple-membership)
7. [Sorting Tuples](#sorting-tuples)
8. [Key Characteristics](#key-characteristics)

## What is a Tuple?

A **tuple** is an immutable, ordered collection of elements in Python. Once created, tuples cannot be modified (no adding, removing, or changing elements).

### Basic Tuple Creation
```python
t = ()              # Empty tuple
t1 = (10, True, 3.4, 1+3j, 'welcome')  # Tuple with mixed data types
```

### Key Point
- Tuples are **immutable** - you cannot use methods like `.append()` to modify them
- They are **ordered** - elements have a defined sequence
- They are **heterogeneous** - can contain different data types

---

## Tuple Creation

There are several ways to create tuples:

### Empty Tuple
```python
tup = ()    # Empty tuple
```

### Tuple of Integers
```python
tup1 = (10, 20, 30, 40, 50)
```

### Tuple of Floats
```python
tup2 = (3.4, 2.5, 5.3, 10.6)
```

### Tuple of Strings
```python
tup3 = ('one', 'two', 'three', 'four')
```

### Nested Tuples
```python
tup4 = ('Nikhil', 39, (50, 100), (60, 75))  # Contains other tuples
```

---

## Tuple Indexing

Access individual elements using their position (0-indexed):

### Positive Indexing
```python
tup1[0]      # Returns 10 (first element)
tup3[0]      # Returns 'one'
```

### Negative Indexing
```python
tup3[-1]     # Returns 'four' (last element)
tup3[-2]     # Returns 'three' (second-to-last element)
```

### Nested Indexing
```python
tup3[0][0]   # Returns 'o' (first character of 'one')
tup4[2][0]   # Returns 50 (first element of nested tuple)
```

---

## Tuple Slicing

Extract portions of a tuple using slice notation `tuple[start:end:step]`:

### Basic Slicing
```python
tup4 = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

tup4[:3]     # ('one', 'two', 'three') - first 3 elements
tup4[2:5]    # ('three', 'four', 'five') - elements from index 2 to 4
```

### Using Negative Indices
```python
tup4[-3:]    # ('seven', 'eight', 'nine') - last 3 elements
tup4[-2:]    # ('eight', 'nine') - last 2 elements
tup4[-1:]    # ('nine',) - last element as a tuple
```

### Full Slice
```python
tup4[:]      # Returns a copy of the entire tuple
```

---

## Tuple Methods

Tuples have limited methods since they are immutable. The two main methods are:

### count() Function
Returns the number of times a value appears in the tuple:
```python
tup4 = ('one', 'two', 'three', 'one', 'one')
tup4.count('one')    # Returns 3
```

### index() Function
Returns the index of the first occurrence of a value:
```python
tup4.index('one')    # Returns 0 (first position)
tup4.index('four')   # Returns 3
```

---

## Tuple Membership

Check if an element exists in a tuple using the `in` operator:

```python
tup4 = ('one', 'two', 'three', 'four', 'five', 'six')

'three' in tup4      # Returns True
'six' in tup4        # Returns True
'ten' in tup4        # Returns False
```

---

## Sorting Tuples

Sort tuple elements using the `sorted()` function (returns a list):

### Ascending Order (Default)
```python
tpl1 = (43, 33, 56, 87, 27, 99, 79)
sorted(tpl1)         # Returns [27, 33, 43, 56, 79, 87, 99]
sorted(tpl1, reverse=False)  # Same as above
```

### Descending Order
```python
sorted(tpl1, reverse=True)   # Returns [99, 87, 79, 56, 43, 33, 27]
```

### Important Note
- `sorted()` returns a **list**, not a tuple
- To convert back to a tuple: `tuple(sorted(tpl1))`

---

## Key Characteristics

| Feature | Tuple | List |
|---------|-------|------|
| **Mutability** | Immutable ❌ | Mutable ✅ |
| **Ordered** | Yes ✅ | Yes ✅ |
| **Syntax** | `(1, 2, 3)` | `[1, 2, 3]` |
| **Performance** | Faster 🚀 | Slower |
| **Use Case** | Fixed data, dict keys | Dynamic data |

### Why Use Tuples?
1. **Immutability** - Guarantees data won't change
2. **Performance** - Tuples are faster than lists
3. **Dictionary Keys** - Can use tuples as dictionary keys (lists cannot)
4. **Safety** - Prevents accidental modifications
5. **Memory** - Uses less memory than lists

---

## Exercises to Try

1. Create a tuple with mixed data types (int, float, string, boolean)
2. Access elements using both positive and negative indices
3. Use slicing to extract the first and last 3 elements
4. Count occurrences of an element in a tuple
5. Find the index of specific values
6. Check membership of elements
7. Sort a tuple of numbers in both ascending and descending order
8. Create nested tuples and access inner elements

---

## Summary

Tuples are fundamental Python data structures that provide:
- ✅ Immutable storage of multiple elements
- ✅ Fast access to elements by index
- ✅ Protection against accidental modifications
- ✅ Ability to use as dictionary keys

Master tuples to write safer, more efficient Python code!
