# Python `for...else` Statements

Python supports an `else` block on a `for` loop. The loop's `else` block runs when the loop finishes normally, meaning that no `break` statement was executed. This makes `for...else` especially useful for search and validation tasks.

## Learning Objectives

By the end of this lesson, you should be able to:

- Explain when the `else` block of a `for` loop runs.
- Use `break` to stop a search when a match is found.
- Use `for...else` to handle the no-match case once.
- Check whether a number is prime with a loop.
- Build an integer array with Python's `array` module.

## Prerequisites

You should be familiar with:

- Variables and basic data types
- Lists and sequences
- `for` loops and `range()`
- Conditional statements
- The `break` statement
- Python indentation

## Syntax

```python
for item in iterable:
    if condition:
        break
else:
    # Runs only when the loop completes without break.
```

The `else` block belongs to the loop, not to the `if` statement. It is aligned with `for`, not with the code inside the loop.

## How It Works

A `for...else` loop has two possible outcomes:

- If `break` executes, Python leaves the loop and skips the `else` block.
- If every item is processed without `break`, Python runs the `else` block.

### Match Found

```python
numbers = [12, 14, 18, 21, 25, 30]

afor number in numbers:
    if number % 5 == 0:
        print("Found:", number)
        break
else:
    print("No number divisible by 5 was found.")
```

Output:

```text
Found: 25
```

Because the loop finds a matching number and executes `break`, the `else` block does not run.

### No Match Found

```python
numbers = [7, 14, 18, 21, 23, 27]

for number in numbers:
    if number % 5 == 0:
        print("Found:", number)
        break
else:
    print("No number divisible by 5 was found.")
```

Output:

```text
No number divisible by 5 was found.
```

The loop checks every item, but no item matches. Since `break` never runs, the `else` block executes once.

## Why Not Put `else` Inside `if`?

Putting `else` inside the `if` prints a message for every item that does not match. That is usually not the desired behavior when searching.

```python
# Prints "Not found" repeatedly for a collection with no match.
for number in numbers:
    if number % 5 == 0:
        print("Found:", number)
        break
    else:
        print("Not found")
```

With `for...else`, the no-match message appears once, after the entire search has finished.

## Prime Number Check

A number greater than `1` is prime if it has no divisors other than `1` and itself. The loop searches for a divisor. If it finds one, `break` identifies the number as non-prime; otherwise, the loop's `else` block confirms that the number is prime.

```python
number = 13

if number < 2:
    print("Not a prime number")
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
```

Output:

```text
Prime number
```

The `number < 2` check is important because `0` and `1` are not prime numbers.

## Creating an Integer Array

The notebook also introduces Python's built-in `array` module. An array stores values of one declared type. The type code `'i'` represents signed integers.

```python
from array import array

numbers = array("i")

for _ in range(5):
    value = int(input("Enter an integer: "))
    numbers.append(value)

print(numbers)
```

`int()` converts the text returned by `input()` into an integer before it is added to the array. The loop repeats five times in this example.

## `for...else` Versus `if...else`

These constructs solve different problems:

| Construct | Purpose |
| --- | --- |
| `if...else` | Choose between conditions during one decision |
| `for...else` | Handle whether a loop completed without `break` |

The `else` block of a loop does not mean that every condition was false. It means that the loop completed normally.

## Common Mistakes

- Indenting the loop `else` under the `if` statement.
- Expecting the `else` block to run only when the `if` condition is false on the last iteration.
- Forgetting `break` when a match should stop the search.
- Printing a no-match message inside the loop and getting repeated output.
- Calling `range(2, number)` without handling values less than `2`.
- Appending strings to an integer array instead of converting input with `int()`.

## Best Practices

- Use `for...else` for searches, validation, and divisor checks.
- Keep the `break` condition easy to identify.
- Put success handling inside the matching branch and no-match handling in `else`.
- Use clear variable names such as `number`, `item`, and `divisor`.
- Test both paths: one case that triggers `break` and one case that reaches `else`.

## Practice Exercises

1. Search a list for a target value and print a message exactly once when it is not found.
2. Check whether a number is divisible by any value from `2` through its square root.
3. Find the first number in a list that is divisible by both `3` and `5`.
4. Use `for...else` to check whether a word contains a digit.
5. Create an integer array from five user inputs and print its contents.

## Summary

`for...else` is a clear way to distinguish between a loop that found a result and a loop that completed without finding one. The `else` block runs only when the `for` loop finishes without executing `break`.
