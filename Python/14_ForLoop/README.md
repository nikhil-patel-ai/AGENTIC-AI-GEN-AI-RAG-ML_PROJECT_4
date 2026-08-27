# Python `for` and `while` Loops

Loops repeat a block of code. A `for` loop processes each item in an iterable, while a `while` loop repeats code as long as a condition remains true.

This lesson introduces:

- `for` loops with `range()`
- `while` loops with counters and conditions
- Start, stop, and step values
- Conditions inside loops
- `break`, `continue`, and `pass`
- Nested loops
- Printing simple patterns

## Learning Objectives

By the end of this lesson, you should be able to:

- Iterate through a sequence with a `for` loop.
- Repeat code with a `while` loop.
- Generate numeric sequences with `range()`.
- Filter values using conditions inside a loop.
- Control loop execution with `break`, `continue`, and `pass`.
- Build simple patterns with nested loops.
- Avoid infinite loops by updating a `while` loop's condition.

## Prerequisites

You should be familiar with:

- Variables and basic data types
- Lists and strings
- Conditional statements
- Python indentation
- Running Python code in a notebook or terminal

## Basic `for` Loop

A `for` loop assigns each value from an iterable to the loop variable and runs the indented block.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

`range(5)` starts at `0` and stops before `5`.

## Using `range()`

The form `range(start, stop, step)` gives control over the sequence:

```python
for number in range(1, 10, 3):
    print(number)
```

Output:

```text
1
4
7
```

The `stop` value is excluded. The step can be negative when counting backward:

```python
for number in range(10, 0, -2):
    print(number)
```

## Loop Through a Collection

A `for` loop can process each item in a list or each character in a string.

```python
names = ["Asha", "Nikhil", "Ravi"]

for name in names:
    print(name)
```

```python
for character in "Python":
    print(character)
```

## Conditions Inside a Loop

Use an `if` statement inside a loop to select specific values.

```python
for number in range(1, 51):
    if number % 5 == 0:
        print(number)
```

The `%` operator returns the remainder. A remainder of `0` means the number is divisible by `5`.

To skip multiples of `3` or `5`, combine conditions with `continue`:

```python
for number in range(1, 51):
    if number % 3 == 0 or number % 5 == 0:
        continue
    print(number)
```

## `break`

Use `break` to stop the loop immediately when a condition is met.

```python
for number in range(1, 11):
    if number == 6:
        break
    print(number)
```

Output:

```text
1
2
3
4
5
```

## `continue`

Use `continue` to skip the rest of the current iteration and move to the next item.

```python
for number in range(1, 11):
    if number == 7:
        continue
    print("hello:", number)
```

The value `7` is not printed, but the loop continues with the remaining values.

## `pass`

Use `pass` as a placeholder when a loop body is required but no action is ready yet.

```python
for number in range(1, 5):
    pass
```

Unlike `continue`, `pass` does not skip to the next iteration by itself; it simply performs no operation for that statement.

## Basic `while` Loop

A `while` loop runs its indented block as long as its condition is true. A counter-based loop should initialize the counter, test the condition, and update the counter.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

The counter update is essential. Without it, the condition may never become false and the loop can run forever.

## Counting Backward with `while`

The counter can decrease when a task needs a countdown:

```python
count = 5

while count >= 1:
    print(count)
    count -= 1
```

## `while` with User Input

Use a `while` loop when the number of repetitions depends on a condition that changes during execution.

```python
command = ""

while command != "quit":
    command = input("Enter a command: ")
    print("You entered:", command)
```

The loop stops when the user enters `quit`.

## Nested `for` Loops

A nested loop is a loop inside another loop. The inner loop completes for each iteration of the outer loop.

```python
for row in range(4):
    for column in range(row + 1):
        print("#", end=" ")
    print()
```

Output:

```text
#
# #
# # #
# # # #
```

The `end` argument keeps the symbols on the same line. The final `print()` starts a new line after each row.

A decreasing pattern can be created by changing the inner range:

```python
for row in range(4):
    for column in range(4 - row):
        print("#", end=" ")
    print()
```

## `for` and `while`

Use a `for` loop when iterating through an iterable or a known range. Use a `while` loop when repetition depends on a condition that changes during execution.

```python
for number in range(1, 6):
    print(number)
```

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Choose `for` when iterating over a sequence or known range. Choose `while` when repetition depends on a condition that changes during execution.

## Best Practices

- Use descriptive names such as `number`, `row`, and `column`.
- Remember that `range()` excludes its stop value.
- Keep the loop body focused on one task.
- Use four spaces for indentation.
- Use `break` and `continue` when they make the control flow clearer.
- Avoid changing the loop variable unnecessarily inside the loop.
- Prefer a single loop over nested loops when the task does not require multiple dimensions.
- Update the condition or counter in every `while` loop.

## Practice Exercises

1. Print the numbers from 1 to 20 using `range()`.
2. Print the odd numbers from 1 to 50.
3. Print every number from 1 to 100 that is divisible by both 3 and 5.
4. Use `continue` to skip all even numbers from 1 to 20.
5. Search a list for a target value and stop with `break` when it is found.
6. Print a right-aligned or inverted triangle using nested loops.
7. Print a countdown from 10 to 1 using a `while` loop.
8. Keep asking for input until the user enters `quit`.
