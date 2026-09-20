# Python Loops

Loops let a Python program repeat a block of code while a condition is true or for each item in a sequence. They reduce repeated code and are useful for processing data, counting, and automating repetitive tasks.

This lesson introduces:

- `while` loops
- Nested loops
- Loop counters and updates
- The `print()` `end` parameter
- `break` and `continue`

## Learning Objectives

By the end of this lesson, you should be able to:

- Repeat code with a `while` loop.
- Initialize, test, and update a loop counter.
- Create nested loops for repeated groups of work.
- Stop or skip loop iterations with `break` and `continue`.
- Avoid infinite loops by updating the loop condition.

## Prerequisites

You should be familiar with:

- Variables and assignment
- Comparison operators
- Conditional statements
- Indentation in Python
- Running Python code in a notebook or terminal

## The `while` Loop

A `while` loop repeats its indented block as long as its condition is true.

```python
i = 1

while i <= 5:
    print("data science", i)
    i = i + 1
```

Output:

```text
data science 1
data science 2
data science 3
data science 4
data science 5
```

A reliable `while` loop has three parts:

1. Initialize the counter.
2. Check the condition.
3. Update the counter inside the loop.

If the counter is not updated, the condition may remain true and create an infinite loop.

## Counting Backward

The counter can decrease instead of increase.

```python
i = 5

while i >= 1:
    print("data science", i)
    i = i - 1
```

## Nested Loops

A nested loop is a loop inside another loop. The inner loop completes all of its iterations for every iteration of the outer loop.

```python
i = 1

while i <= 3:
    print("data science", end=" - ")

    j = 1
    while j <= 2:
        print("technology", end=" - ")
        j = j + 1

    print()
    i = i + 1
```

The `end` argument changes what `print()` writes after each value. By default, `print()` starts a new line; `end=" - "` keeps output on the same line with a separator.

## `break`

Use `break` to stop the loop immediately.

```python
for number in range(1, 11):
    if number == 5:
        break
    print(number)
```

Output:

```text
1
2
3
4
```

## `continue`

Use `continue` to skip the rest of the current iteration and begin the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

## `while` and `for`

Use a `while` loop when repetition depends on a condition that changes during execution. Use a `for` loop when iterating through a sequence or a known range of values.

```python
for number in range(1, 6):
    print(number)
```

The `for` loop is covered in more detail in the next lesson.

## Best Practices

- Use descriptive counter names such as `count` or `index`.
- Update the counter in every `while` loop.
- Keep the loop condition easy to understand.
- Use four spaces for indentation.
- Use `break` and `continue` only when they make the control flow clearer.
- Prefer a `for` loop when iterating over a known sequence or range.

## Practice Exercises

1. Print the numbers from 1 to 10 using a `while` loop.
2. Print the numbers from 10 down to 1.
3. Print the multiplication table for a number entered by the user.
4. Use a nested loop to print a rectangle of stars.
5. Print numbers from 1 to 20, skipping multiples of 3 with `continue`.
6. Search for a number in a sequence and stop when it is found with `break`.
