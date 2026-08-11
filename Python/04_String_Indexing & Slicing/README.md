# String Indexing & Slicing

This folder contains a Jupyter Notebook that demonstrates Python string creation, indexing, slicing, and common string operations with runnable examples and notes.

## Files
- [String_indexing_&_Slicing.ipynb](String_indexing_&_Slicing.ipynb) — Notebook with explanations and runnable examples.
- README.md — This expanded summary and examples.

## Overview
The notebook and this README cover:
- String creation using single, double and triple quotes
- Multiline strings and quoting rules
- Immutability of strings
- Indexing (forward and backward)
- Slicing (start:stop:step) including positive and negative steps
- Common operations: concatenation, replication, length

## Examples (copied from the notebook)

### 1. String creation
```python
s1 = 'abcd'                # single quotes
s2 = "nit-lab-practice"  # double quotes
s3 = '''nit-lab-practice triple quotes'''  # triple quotes
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
```

### 2. Multiline strings
```python
s6 = ''' Welcome to the Naresh IT FSDS With Gen-AI & Agentic-AI
This is test for single quotes in 
multiple line '''
print(s6)
```

### 3. Concatenation and replication
```python
mystr = ('Happy '
         'Monday '
         'Everyone')
print(mystr)

mystr2 = 'Woohoo '
mystr2 = mystr2 * 5
print(mystr2)
print(len(mystr2))
```

### 4. Indexing (forward & backward)
```python
str2 = 'Naresh IT'
print(str2)      # full string
print(str2[0])   # first character
print(str2[1])
print(str2[-1])  # last character
print(str2[len(str2)-1])
```

### 5. Slicing
```python
str2 = 'Naresh IT'
print(str2[:])       # copy entire string
print(str2[0:9])     # characters from index 0 up to 8
print(str2[6:12])    # characters starting at 6 up to 11 (may truncate)
print(str2[-4:])     # last four characters

# Positive step (forward)
print(str2[3:9])
print(str2[:4])

# Negative step (backward)
print(str2[::-1])    # reverse string
print(str2[0:7:2])   # start=0, stop=7, step=2
```

## Key Notes
- Creation: use single/double quotes or triple quotes for multiline strings.
- Immutability: strings are immutable; operations return new strings.
- Indexing: zero-based; negative indices count from the end (-1 is last char).
- Slicing: `s[start:stop:step]` — `start` inclusive, `stop` exclusive; out-of-range slice bounds are handled gracefully.

## How to run
1. Install Python 3.8+ and Jupyter (or use VS Code's Jupyter extension).

Using pip:

```bash
python -m pip install --upgrade pip
pip install jupyter
```

2. Open the notebook in Jupyter or VS Code and run the cells interactively.

## Exercises
- Create strings that embed quotes without escapes by switching outer quotes.
- Extract characters with positive and negative indices.
- Slice strings with different `start`, `stop`, and `step` values; try out-of-range bounds.

## License
This material is provided as-is for learning and practice. Feel free to reuse or adapt for teaching and exercises.
