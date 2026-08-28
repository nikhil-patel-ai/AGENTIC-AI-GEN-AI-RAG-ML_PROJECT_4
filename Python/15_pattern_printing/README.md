# Pattern Printing in Python

Pattern printing is a practical way to learn nested loops, iteration ranges, conditions, string operations, and output formatting. Each pattern is built one row at a time. The outer loop controls the rows, while one or more inner loops control the characters printed in each row.

This lesson progresses from simple rectangles and triangles to hollow shapes, number patterns, pyramids, diamonds, and butterfly patterns.

## Learning Objectives

By the end of this lesson, you should be able to:

- Design a pattern by calculating its rows, columns, spaces, and symbols.
- Use nested `for` loops to generate two-dimensional output.
- Control line breaks with `print()` and the `end` parameter.
- Use `range()` for increasing, decreasing, and calculated sequences.
- Create star, number, hollow, pyramid, diamond, and butterfly patterns.
- Use conditions to print borders while leaving the inside of a shape empty.
- Write readable and reusable pattern programs.

## Prerequisites

You should understand:

- Variables and assignment
- `for` loops and nested loops
- `range()` and its `start`, `stop`, and `step` arguments
- Conditional statements
- Strings and string multiplication
- The `print()` function

## The Pattern Model

Most patterns follow this structure:

```python
for row in range(number_of_rows):
    for column in range(number_of_columns):
        print(symbol, end=" ")
    print()
```

The outer loop runs once for each row. The inner loop runs once for each position in that row. The final `print()` moves the cursor to the next line after the row is complete.

For patterns whose width changes from row to row, calculate the inner-loop range from the current row:

```python
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

## Understanding `print()` and `end`

By default, `print()` adds a newline after every call:

```python
print("A")
print("B")
```

Output:

```text
A
B
```

Use `end` to keep output on the same line:

```python
print("A", end=" ")
print("B")
```

Output:

```text
A B
```

In pattern programs, use `end=" "` or `end=""` inside the inner loop, then call `print()` once after the inner loop has finished.

## Understanding `range()`

`range(start, stop, step)` generates a sequence of integers. The `stop` value is excluded.

```python
range(1, 6)       # 1, 2, 3, 4, 5
range(5, 0, -1)   # 5, 4, 3, 2, 1
range(0, 5)       # 0, 1, 2, 3, 4
```

Use an increasing range for a growing pattern and a negative step for a shrinking pattern.

## Basic Patterns

### 1. Solid Rectangle

A rectangle has a fixed number of rows and columns.

```python
rows = 4
columns = 5

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()
```

### 2. Left-Aligned Star Triangle

The number of symbols increases with the row number.

```python
size = 5

for row in range(1, size + 1):
    print("* " * row)
```

### 3. Inverted Star Triangle

Start with the largest row and decrease the width by one each time.

```python
size = 5

for row in range(size, 0, -1):
    print("* " * row)
```

### 4. Number Triangle

Convert each number to text when joining values into one line.

```python
size = 5

for row in range(1, size + 1):
    print(" ".join(str(number) for number in range(1, row + 1)))
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

## Alignment and Spaces

Right-aligned patterns need leading spaces before the symbols. For a pattern with `size` rows, row `row` usually needs `size - row` groups of spaces.

```python
size = 5

for row in range(1, size + 1):
    print("  " * (size - row) + "* " * row)
```

Keeping the space width consistent is important. When each symbol has a trailing space, use two spaces for each leading indentation unit so the shape remains visually aligned.

## Pyramid Patterns

A centered pyramid combines leading spaces with an odd number of symbols. The symbol count for row `row` is `2 * row - 1`.

```python
size = 5

for row in range(1, size + 1):
    spaces = "  " * (size - row)
    stars = "* " * (2 * row - 1)
    print(spaces + stars)
```

### Inverted Pyramid

Reverse the row range to reduce the number of symbols on each line.

```python
size = 5

for row in range(size, 0, -1):
    spaces = "  " * (size - row)
    stars = "* " * (2 * row - 1)
    print(spaces + stars)
```

### Diamond

A diamond combines a growing pyramid with a shrinking inverted pyramid. The widest row must not be repeated.

```python
size = 5

for row in range(1, size + 1):
    print("  " * (size - row) + "* " * (2 * row - 1))

for row in range(size - 1, 0, -1):
    print("  " * (size - row) + "* " * (2 * row - 1))
```

## Hollow Patterns

A hollow pattern prints a symbol only on its border. For a square, a position is on the border when it is in the first or last row, or the first or last column.

### Hollow Square

```python
size = 5

for row in range(size):
    for column in range(size):
        is_border = row in (0, size - 1) or column in (0, size - 1)
        print("*" if is_border else " ", end=" ")
    print()
```

The same border idea can be adapted to triangles and pyramids. In a hollow triangle, print the symbol at the left edge, right edge, or on the final row.

### Hollow Right Triangle

```python
size = 5

for row in range(1, size + 1):
    for column in range(1, row + 1):
        is_border = column == 1 or column == row or row == size
        print("*" if is_border else " ", end=" ")
    print()
```

### Hollow Pyramid

```python
size = 5

for row in range(1, size + 1):
    print("  " * (size - row), end="")
    for position in range(1, 2 * row):
        is_border = position == 1 or position == 2 * row - 1 or row == size
        print("*" if is_border else " ", end=" ")
    print()
```

## Number Patterns

The same loop structures can print numbers instead of stars.

### Floyd's Triangle

Floyd's triangle uses one counter that continues across all rows.

```python
size = 5
number = 1

for row in range(1, size + 1):
    for column in range(row):
        print(number, end=" ")
        number += 1
    print()
```

### Hollow Number Pyramid

Print the row number on the two edges and across the last row.

```python
size = 5

for row in range(1, size + 1):
    print("  " * (size - row), end="")
    for position in range(1, 2 * row):
        is_border = position == 1 or position == 2 * row - 1 or row == size
        print(row if is_border else " ", end=" ")
    print()
```

## Butterfly Pattern

A butterfly has two matching wings separated by a growing or shrinking space. The first half grows, and the second half shrinks.

```python
size = 5

for row in range(1, size + 1):
    wing = "* " * row
    gap = "  " * (2 * (size - row))
    print(wing + gap + wing)

for row in range(size, 0, -1):
    wing = "* " * row
    gap = "  " * (2 * (size - row))
    print(wing + gap + wing)
```

For the number version, replace each wing with a loop that prints values from `1` through `row`.

## Pattern Index in This Notebook

The notebook contains these exercises and variations:

1. Basic rectangle and repeated rows
2. Right-angle star triangle
3. Inverted right-angle triangle
4. Pyramid pattern
5. Inverted pyramid pattern
6. Diamond pattern
7. Hollow square pattern
8. Full square pattern
9. Right-angle number triangle
10. Inverted right-angle number triangle
11. Floyd's triangle
12. Hollow right-angle triangle
13. Hollow pyramid
14. Hollow diamond
15. Hollow diamond with numbers
16. Butterfly pattern with numbers
17. Butterfly pattern with stars
18. Hollow number pyramid
19. Full star pyramid and inverted full star pyramid
20. Left- and right-aligned star and number pyramids

## A Systematic Problem-Solving Method

When creating a new pattern, work through these steps:

1. Decide how many rows the pattern requires.
2. Determine how the width changes from one row to the next.
3. Calculate the number of spaces needed for alignment.
4. Choose whether the row contains symbols, numbers, or both.
5. Decide whether the pattern needs one loop or nested loops.
6. Add conditions for hollow borders or special positions.
7. Print a newline after each completed row.
8. Test the smallest size, a normal size, and an edge case such as `size = 1`.

## Common Mistakes

- Forgetting the final `print()` after an inner loop, which makes every row appear on one line.
- Using `range(size)` when the pattern needs `range(1, size + 1)`.
- Forgetting that the stop value in `range()` is excluded.
- Using inconsistent spaces, which causes centered patterns to look misaligned.
- Printing a symbol in every position when a hollow pattern requires a border condition.
- Reusing a counter incorrectly in patterns such as Floyd's triangle.
- Modifying the loop variable inside the loop instead of calculating the required range.
- Mixing tabs and spaces in indentation.

## Best Practices

- Use descriptive names such as `row`, `column`, `size`, `spaces`, and `position`.
- Store the pattern size in one variable so the program is easy to change.
- Prefer string multiplication for simple repeated rows.
- Use nested loops when each position needs a condition or a calculated value.
- Keep one responsibility per loop and format the output consistently.
- Remove exploratory comments before sharing finished code.
- Test both star and number variations when the structure supports both.

## Practice Exercises

1. Print a hollow rectangle whose rows and columns are entered by the user.
2. Print a centered number pyramid where each row contains the same number.
3. Print a Pascal-style triangle using calculated values.
4. Print a hollow inverted pyramid.
5. Print a diamond with alternating `*` and `#` symbols.
6. Print a number butterfly in which each wing counts from `1` to the row number.
7. Rewrite one nested-loop pattern using string operations only.
8. Add input validation so the pattern size must be a positive integer.

## Summary

Pattern printing is an exercise in translating a visual design into loop rules. The outer loop controls rows, inner loops control positions, `range()` controls repetition, `end` controls horizontal output, and conditions control borders or special values. Once these relationships are clear, many complex-looking patterns become small, predictable Python programs.
