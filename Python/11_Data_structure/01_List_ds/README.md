# List Data Structure

## Overview
A **list** in Python is an ordered, mutable collection that can store multiple items of different data types. Lists are one of the most commonly used data structures in Python.

## Key Characteristics
- **Ordered**: Elements maintain their position in the list
- **Mutable**: Lists can be modified after creation (items can be added, removed, or changed)
- **Heterogeneous**: Can contain items of different data types (integers, floats, strings, complex numbers, booleans, nested lists, etc.)
- **Indexed**: Elements are accessed using zero-based indexing
- **Allows Duplicates**: The same value can appear multiple times in a list

## Creating Lists

### Empty List
```python
l = []  # Create an empty list
type(l)  # Returns: <class 'list'>
len(l)   # Returns: 0
```

### List with Values
```python
l1 = [10, 3.5, True, 1+3j, 'hello']  # Heterogeneous list
l2 = [1, 2, 3, 4, 5]                 # Homogeneous list
```

## Adding Elements

### append()
Adds a single element to the end of the list.
```python
l = []
l.append(10)    # l = [10]
l.append(20)    # l = [10, 20]
l.append(30)    # l = [10, 20, 30]
```

**Note**: `append()` only accepts one argument. For multiple items, call it multiple times or use `extend()`.

### extend()
Adds multiple elements from an iterable to the end of the list.
```python
l1 = [10, 20, 30]
l2 = [40, 50, 60]
l1.extend(l2)   # l1 = [10, 20, 30, 40, 50, 60]
```

## Accessing Elements

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
