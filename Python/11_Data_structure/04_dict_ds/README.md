# Dictionary Data Structure

## Overview

A **dictionary** is a mutable collection of key-value pairs. Each key must be unique and hashable, while values can be any Python object. Dictionaries are useful when data should be looked up by a meaningful key instead of a numeric index.

```python
student = {
    "name": "Nikhil",
    "id": 12345,
    "course": "Python"
}
```

## Key Characteristics

| Feature | Dictionary |
|---|---|
| Ordered | Yes, insertion order is preserved |
| Mutable | Yes |
| Duplicate keys | Not allowed |
| Keys | Must be hashable |
| Values | Can be any data type |
| Syntax | `{key: value}` |

## Creating Dictionaries

```python
empty = {}
also_empty = dict()

numbers = {1: "one", 2: "two", 3: "three"}
mixed = {1: "one", "A": ["two", "three"]}
```

Create a dictionary from a sequence of keys with `fromkeys()`:

```python
keys = {"a", "b", "c"}
scores = dict.fromkeys(keys, 0)
```

Be careful when using a mutable default value. All keys will reference the same object:

```python
shared = dict.fromkeys(keys, [])
shared["a"].append(10)
print(shared)  # Every key now shows [10]
```

## Accessing Items

Use a key with square brackets or use `get()`:

```python
student = {"name": "Nikhil", "id": 12345}

student["name"]          # Raises KeyError if the key is missing
student.get("id")        # Returns None if the key is missing
student.get("age", 0)    # Returns 0 if the key is missing
```

The main dictionary views are:

```python
student.keys()    # Keys
student.values()  # Values
student.items()   # Key-value pairs
```

Nested dictionaries and collections are supported:

```python
profile = {
    "name": "Nikhil",
    "skills": ["Python", "SQL"],
    "contact": {"city": "Delhi"}
}

profile["contact"]["city"]  # "Delhi"
```

## Adding, Changing, and Removing Items

```python
student["course"] = "Python"       # Add a new item
student["id"] = 54321               # Change an existing item
student.update({"level": "beginner"})

student.pop("level")                # Remove and return a value
student.pop("missing", None)        # Avoid KeyError for a missing key
student.popitem()                   # Remove and return the last pair
del student["course"]               # Remove a specific item
student.clear()                      # Remove all items
```

## Copying Dictionaries

Assignment creates another reference to the same dictionary. Use `copy()` for a shallow copy:

```python
original = {"name": "Nikhil", "id": 12345}

alias = original
copied = original.copy()

original["id"] = 54321
print(alias["id"])   # 54321
print(copied["id"])  # 12345
```

For nested data, use `copy.deepcopy()` when independent nested objects are required.

## Looping Through a Dictionary

```python
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)
```

## Dictionary Membership

The `in` operator checks keys by default:

```python
student = {"name": "Nikhil", "id": 12345}

"name" in student          # True
"Nikhil" in student         # False: this checks keys, not values
"Nikhil" in student.values()  # True
```

## Common Mistakes

```python
student["age"]              # KeyError when "age" does not exist
student.get("age")          # Safer lookup when a key may be missing
del student["id"]           # Correct deletion syntax
```

Keys should be immutable/hashable values such as strings, numbers, tuples, or booleans. Lists and dictionaries cannot be used as keys.

## Summary

Dictionaries provide:

- Fast lookup using unique keys
- Mutable key-value storage
- Support for nested and mixed data
- Useful views through `keys()`, `values()`, and `items()`
- Convenient methods for updating, copying, and removing data

The accompanying `dictionary.ipynb` notebook demonstrates these concepts interactively.