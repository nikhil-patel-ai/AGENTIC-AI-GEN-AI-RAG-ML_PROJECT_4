# Set Data Structure

## Overview

A **set** is an unordered, mutable collection of unique and hashable values. Sets are useful for removing duplicates, testing membership, and performing mathematical set operations.

```python
numbers = {1, 2, 3, 3}
print(numbers)  # {1, 2, 3}
```

The order of elements is not guaranteed, so do not use a set with indexing or slicing.

## Key Characteristics

| Feature | Set |
|---|---|
| Ordered | No guaranteed order |
| Mutable | Yes |
| Duplicate values | Not allowed |
| Indexing and slicing | Not supported |
| Elements | Must be hashable |
| Syntax | `{1, 2, 3}` |

## Creating Sets

```python
empty_set = set()       # Correct way to create an empty set
numbers = {1, 2, 3, 4}
values = {2, 3.4, True, 2 + 3j, "Python"}

not_a_set = {}          # This creates an empty dictionary
```

A set can be created from another iterable:

```python
unique_letters = set("banana")
print(unique_letters)    # {'b', 'a', 'n'}
```

Set elements must be immutable/hashable. Numbers, strings, tuples, and booleans can be elements, but lists and dictionaries cannot.

## Adding and Removing Elements

```python
items = {1, 2, 3}

items.add(4)             # Add one element
items.update([5, 6])     # Add multiple elements
items.remove(2)          # Remove 2; raises KeyError if absent
items.discard(10)        # Remove 10 if present; no error if absent
removed = items.pop()   # Remove and return an arbitrary element
items.clear()            # Remove every element
```

`copy()` creates a shallow copy:

```python
original = {1, 2, 3}
backup = original.copy()
```

## Membership Testing

```python
colors = {"red", "green", "blue"}

"green" in colors       # True
"yellow" not in colors  # True
```

Membership testing is generally very efficient because sets are hash-based.

## Set Operations

Given these sets:

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {8, 9, 10}
```

### Union
All unique elements from the sets:

```python
a.union(b)              # {1, 2, 3, 4, 5, 6, 7, 8}
a | b | c
```

### Intersection
Elements common to both sets:

```python
a.intersection(b)       # {4, 5}
a & b
```

### Difference
Elements in the first set but not in the second:

```python
a.difference(b)          # {1, 2, 3}
a - b
```

Difference is directional: `a - b` can produce a different result from `b - a`.

### Symmetric Difference
Elements that belong to either set, but not both:

```python
a.symmetric_difference(b)
a ^ b
```

## Updating Sets In Place

The following methods modify the set instead of returning a new set:

```python
items = {1, 2, 3}
items.intersection_update({2, 3, 4})
items.difference_update({3})
items.symmetric_difference_update({4, 5})
items.update({6, 7})
```

## Relationship Tests

```python
large = {1, 2, 3, 4, 5}
small = {2, 3}
other = {10, 20}

small.issubset(large)       # True
large.issuperset(small)     # True
large.isdisjoint(other)     # True
```

Equivalent operators are available:

```python
small <= large      # Subset
large >= small      # Superset
large.isdisjoint(other)
```

## Frozen Sets

A `frozenset` is an immutable version of a set. It cannot be changed after creation and can be used as a dictionary key or as an element of another set.

```python
fixed = frozenset({1, 2, 3})

# fixed.add(4)       # AttributeError
lookup = {fixed: "immutable set"}
```

## Common Mistakes

```python
{}                   # Empty dictionary, not an empty set
set()[0]             # TypeError: sets do not support indexing
set().pop(1)         # TypeError: pop() takes no index
```

Use `remove()` when a missing value should be reported as an error, and `discard()` when it should be ignored.

## Summary

Sets provide:

- Automatic removal of duplicate values
- Fast membership testing
- Mutable collection operations such as `add`, `remove`, and `update`
- Mathematical operations such as union, intersection, and difference
- Immutable storage through `frozenset`

The accompanying `SetDS.ipynb` notebook demonstrates these concepts interactively.
