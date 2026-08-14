# Modules, Framework & Input Functions in Python - Complete Guide

## Overview
This notebook covers two essential Python concepts:
1. **Modules & Frameworks** - How to import and use the `math` module with various functions
2. **User Input Functions** - How to accept and process user input in Python programs

---

## Table of Contents
1. [Part 1: Math Module](#part-1-math-module)
   - [Importing the Math Module](#importing-the-math-module)
   - [Math Functions](#math-functions)
   - [Math Constants](#math-constants)
   - [Different Import Methods](#different-import-methods)
2. [Part 2: User Input Functions](#part-2-user-input-functions)
   - [input() Function Basics](#input-function-basics)
   - [Type Conversion with input()](#type-conversion-with-input)
   - [String Indexing with input()](#string-indexing-with-input)
   - [eval() Function](#eval-function)

---

# Part 1: Math Module

## Importing the Math Module

### What is a Module?
A **module** is a Python file containing reusable code (functions, variables, classes) that you can import and use in your programs. The `math` module provides mathematical functions and constants.

### Basic Import

#### Code
```python
import math    # math is a module
```

#### Explanation
- **`import`**: Keyword that loads a module into your program
- **`math`**: Name of the built-in Python module containing mathematical functions
- **Purpose**: This single line gives you access to all functions and constants in the math module
- **Usage**: You must prefix functions with `math.` (e.g., `math.sqrt()`)

---

## Math Functions

### 1. Square Root - `math.sqrt()`

#### Code
```python
x = math.sqrt(25)
x
```

#### Explanation
- **`math.sqrt(25)`**: Returns the square root of 25
- **Line 1**: Calculates √25 and stores the result (5.0) in variable `x`
- **Line 2**: Displays the value of `x`
- **Output**: `5.0` (floating-point number)

#### Example
```python
sq = math.sqrt(56)
# sq = 7.483314773547883
```

---

### 2. Floor Function - `math.floor()`

#### Code
```python
print(math.floor(2.9))     # floor - minimum or least value
```

#### Explanation
- **`math.floor(2.9)`**: Rounds DOWN to the nearest integer
- **Function Purpose**: Returns the largest integer less than or equal to the given number
- **2.9 → 2**: The decimal part (0.9) is removed, keeping only the integer part
- **Output**: `2`

#### Examples
```python
math.floor(3.5)    # Output: 3
math.floor(4.9)    # Output: 4
math.floor(2.1)    # Output: 2
```

---

### 3. Ceiling Function - `math.ceil()`

#### Code
```python
print(math.ceil(2.9))    # ceil - maximum or highest value
```

#### Explanation
- **`math.ceil(2.9)`**: Rounds UP to the nearest integer
- **Function Purpose**: Returns the smallest integer greater than or equal to the given number
- **2.9 → 3**: Since 2.9 is between 2 and 3, it rounds up to the next integer (3)
- **Output**: `3`

#### Examples
```python
math.ceil(3.5)    # Output: 4
math.ceil(4.9)    # Output: 5
math.ceil(2.1)    # Output: 3
```

#### Difference: floor vs ceil
| Number | floor() | ceil() |
|--------|---------|--------|
| 2.1 | 2 | 3 |
| 3.5 | 3 | 4 |
| 4.9 | 4 | 5 |

---

### 4. Power Function - `math.pow()`

#### Code
```python
print(math.pow(38, 2))
```

#### Explanation
- **`math.pow(base, exponent)`**: Raises a number to a power
- **`math.pow(38, 2)`**: Calculates 38² (38 raised to the power of 2)
- **Calculation**: 38 × 38 = 1444
- **Output**: `1444.0` (returns float)

#### Examples
```python
math.pow(2, 3)     # 2³ = 2 × 2 × 2 = 8.0
math.pow(5, 2)     # 5² = 5 × 5 = 25.0
math.pow(10, 0)    # 10⁰ = 1.0
```

---

## Math Constants

### 1. Pi - `math.pi`

#### Code
```python
print(math.pi)    # these are constants
```

#### Explanation
- **`math.pi`**: Built-in constant representing the mathematical value π (pi)
- **Value**: 3.141592653589793
- **Usage**: Used in calculations involving circles, spheres, and trigonometry
- **Output**: `3.141592653589793`

#### Example Application
```python
radius = 5
area = math.pi * radius ** 2
# area = 3.141592653589793 * 25 = 78.53981633974483
```

---

### 2. Euler's Number - `math.e`

#### Code
```python
print(math.e)    # these are constants
```

#### Explanation
- **`math.e`**: Built-in constant representing Euler's number
- **Value**: 2.718281828459045
- **Usage**: Used in exponential growth/decay calculations, natural logarithms
- **Output**: `2.718281828459045`

#### Example Application
```python
# Exponential growth: N(t) = N₀ * e^(kt)
initial = 100
rate = 0.05
time = 10
result = initial * (math.e ** (rate * time))
```

---

## Different Import Methods

### Method 1: Direct Import
```python
import math
math.sqrt(25)      # Use: module.function()
```

### Method 2: Import with Alias
```python
import math as m
m.floor(3.4)       # Use: alias.function()
```

#### Code Explanation
```python
import math as m      # Import math module with nickname 'm'
m.floor(3.4)          # Use 'm' instead of 'math'
# Output: 3
```

- **`as m`**: Creates a shorter alias (nickname) for the module
- **Benefit**: Reduces typing when using frequently
- **Usage**: Call functions with the alias: `m.sqrt()`, `m.floor()`, etc.

#### Examples
```python
print(m.floor(34))      # Output: 34
print(m.pow(8, 4))      # Output: 4096.0
print(m.sqrt(4))        # Output: 2.0
```

---

### Method 3: Import Specific Functions

#### Code
```python
from math import sqrt, pow    # Import specific functions
pow(2, 3)                      # Call without 'math.' prefix
# Output: 8.0
```

#### Explanation
- **`from math import sqrt, pow`**: Imports only the specified functions from the math module
- **No prefix needed**: You can call `pow()` directly instead of `math.pow()`
- **Benefit**: Less typing, cleaner code
- **Trade-off**: Only imported functions are available; others require full path

#### Example
```python
from math import pow, floor, ceil, sqrt
# Now you can use directly:
sqrt(16)           # Output: 4.0
floor(3.9)         # Output: 3
ceil(3.1)          # Output: 4
pow(2, 8)          # Output: 256.0
```

---

### Method 4: Import All Functions (Wildcard)

#### Code
```python
from math import *    # Import ALL functions from math module
```

#### Explanation
- **`from math import *`**: Imports all available functions and constants from the math module
- **Asterisk (*)**:  Wildcard meaning "everything"
- **Benefit**: Access all math functions without prefix
- **Warning**: ⚠️ Can cause naming conflicts if you have variables with same names as math functions

#### Example
```python
from math import *
# Now available: sqrt(), floor(), ceil(), pow(), pi, e, sin(), cos(), etc.
pi           # 3.141592653589793
sqrt(100)    # 10.0
factorial(5) # 120
```

---

### Getting Help with Modules

#### Code
```python
help()
```

#### Explanation
- **`help()`**: Launches an interactive help system in Python
- **Purpose**: Get documentation about modules, functions, and classes
- **Usage**: Type `help()` to enter help mode, then type the object name (e.g., `math`, `math.sqrt`)
- **Exit**: Type `quit()` to exit help mode

#### How to Use
```python
help()
# Then type: math
# Or directly: help(math.sqrt)
```

---

# Part 2: User Input Functions

## input() Function Basics

### What is input()?
The **`input()`** function allows users to enter data from the keyboard/console while the program is running.

### Basic Usage

#### Code
```python
x = input()
x
```

#### Explanation
- **`input()`**: Waits for user to type something and press Enter
- **Returns**: The text entered by the user as a **string**
- **Storage**: The input is stored in variable `x`
- **Display**: The second line displays the value stored in `x`
- **Important**: The console will pause and wait for user input

#### Example
```
Input: hello
x = "hello"
```

---

### Multiple Inputs

#### Code
```python
x = input()
y = input()
z = x + y
print(z)
```

#### Explanation
- **Line 1**: Waits for first input and stores in `x`
- **Line 2**: Waits for second input and stores in `y`
- **Line 3**: Concatenates (joins) `x` and `y` as strings
- **Line 4**: Prints the combined result
- **Important**: The `+` operator joins strings, NOT adds numbers

#### Example
```
Input 1: 5
Input 2: 10
Output: 510  ← Strings are concatenated, not added arithmetically!
```

#### Verify Type
```python
print(type(x))    # Output: <class 'str'>
```

---

## Type Conversion with input()

### Understanding the Problem

#### Code
```python
x = input()
y = input()
z = x + y
print(z)
```

#### The Issue
- **Problem**: `input()` ALWAYS returns a STRING, even if you enter numbers
- **`"5" + "10" = "510"`**: String concatenation, not mathematical addition
- **Solution**: Convert strings to integers using `int()`

---

### Solution 1: Convert After Input

#### Code
```python
x = int(input())
y = int(input())
z = x + y
print(z)
```

#### Explanation
- **`int(input())`**: First gets the input as a string, then converts it to an integer
- **Line 1**: Gets first number input and converts to integer, stores in `x`
- **Line 2**: Gets second number input and converts to integer, stores in `y`
- **Line 3**: Adds the two integers arithmetically: `x + y`
- **Line 4**: Prints the sum
- **Output**: Arithmetic result, not string concatenation

#### Example
```
Input 1: 5
Input 2: 10
Output: 15  ← Correct mathematical addition!
```

---

### Adding a Prompt Message

#### Code
```python
x1 = input('Enter the 1st number')    # Prompt message appears
y1 = input('Enter the 2nd number')    # Always returns a string
z1 = x1 + y1
print(z1)
```

#### Explanation
- **`input('message')`**: The string argument is a prompt displayed to the user
- **'Enter the 1st number'**: This message is shown before the user inputs
- **Still returns string**: Even with a prompt, `input()` returns a string
- **Concatenation**: `x1 + y1` joins strings, not adds numbers

#### Console Display
```
Enter the 1st number5
Enter the 2nd number10
510
```

#### Verify Type
```python
print(type(x1))    # Output: <class 'str'>
print(type(y1))    # Output: <class 'str'>
```

---

### Solution 2: Convert with Explicit Steps

#### Code
```python
x1 = input('Enter the 1st number')    # Get input as string
a1 = int(x1)                          # Convert to integer
y1 = input('Enter the 2nd number')    # Get input as string
b1 = int(y1)                          # Convert to integer
z1 = a1 + b1                          # Add integers
print(z1)
```

#### Explanation
- **Line 1**: Stores user input as STRING in `x1`
- **Line 2**: Converts string `x1` to integer `a1`
- **Line 3**: Stores second input as STRING in `y1`
- **Line 4**: Converts string `y1` to integer `b1`
- **Line 5**: Adds the two integers
- **Line 6**: Prints the result

#### Drawback
⚠️ **Memory Inefficient**: Uses extra variables and lines of code unnecessarily

---

### Solution 3: Convert During Input (Recommended)

#### Code
```python
x2 = int(input('Enter the 1st number'))
y2 = int(input('Enter the 2nd number'))
z2 = x2 + y2
z2
```

#### Explanation
- **`int(input('...'))`**: Combines input and type conversion in one operation
- **Line 1**: Gets input and immediately converts to integer, stores in `x2`
- **Line 2**: Gets input and immediately converts to integer, stores in `y2`
- **Line 3**: Adds the two integers arithmetically
- **Line 4**: Displays the result
- **Benefit**: Cleaner, more concise, and memory-efficient

#### Console Display
```
Enter the 1st number5
Enter the 2nd number10
15
```

#### Key Advantages
✅ Single line per input  
✅ No extra variables  
✅ Type-safe  
✅ Pythonic approach

---

## String Indexing with input()

### Simulating Character Input

#### Note
Python doesn't have a dedicated `char` data type. Single characters are stored as strings of length 1.

#### Code
```python
ch = input('enter a char')
print(ch)
```

#### Explanation
- **`input('enter a char')`**: Accepts text input from user
- **`print(ch)`**: Displays the entire input
- **Note**: If user enters multiple characters, all are stored in `ch`

#### Example
```
User enters: Hello
Output: Hello
```

---

### Accessing Individual Characters by Index

#### Accessing First Character
```python
print(ch[0])
```

- **`ch[0]`**: First character of the string (index starts at 0)
- **Example**: If `ch = "Hello"`, then `ch[0] = "H"`

#### Accessing Second Character
```python
print(ch[1])
```

- **`ch[1]`**: Second character of the string
- **Example**: If `ch = "Hello"`, then `ch[1] = "e"`

#### Accessing Last Character
```python
print(ch[-1])
```

- **`ch[-1]`**: Last character of the string (negative indexing)
- **Example**: If `ch = "Hello"`, then `ch[-1] = "o"`

#### Complete Example
```python
ch = input('enter a char')    # User enters: "Hello"
print(ch[0])                  # Output: H
print(ch[1])                  # Output: e
print(ch[-1])                 # Output: o
```

---

### Single Character Extraction

#### Getting Only First Character During Input

#### Code
```python
ch = input('enter a char')[0]
print(ch)
```

#### Explanation
- **`input('enter a char')[0]`**: Gets input and immediately extracts first character
- **`[0]`**: Index operator applied directly to the input result
- **Result**: Even if user enters multiple characters, only the first is stored

#### Example
```
User enters: Python
Output: P  ← Only first character
```

---

### String Slicing with Input

#### Code
```python
ch = input('enter a char')[1:4]
print(ch)
```

#### Explanation
- **`input('enter a char')[1:4]`**: Gets input and extracts characters at indices 1 to 3 (4 is exclusive)
- **`[1:4]`**: Slice notation meaning "start at index 1, stop before index 4"
- **Result**: Characters at positions 1, 2, and 3

#### Example
```
User enters: Programming
Output: rog  ← Characters at indices 1, 2, 3
         P r o g r a m m i n g
         0 1 2 3 4 5 6 7 8 9 10
```

---

### Important: input() as String

#### Code
```python
ch = input('enter a char')
print(ch)     # If you enter "2 + 6 - 1", output is "2 + 6 - 1"
```

#### Explanation
- **No evaluation**: `input()` treats everything as text/string
- **Mathematical expressions are NOT calculated**: "2 + 6 - 1" is stored as a string, not evaluated
- **Output**: Exactly what was typed, nothing more
- **No operator interpretation**: The `+` and `-` are just characters in a string

#### Example
```
User enters: 2 + 6 - 1
Output: 2 + 6 - 1  ← Printed as-is, not calculated as 7
```

---

## eval() Function

### What is eval()?
**`eval()`** evaluates a string containing a Python expression and returns the result.

### Code
```python
result = eval(input('enter an expr'))
print(result)
```

### Explanation
- **`input('enter an expr')`**: Gets user input as a string
- **`eval(...)`**: Evaluates the string as a Python expression
- **Expression**: The input string is treated as Python code and executed
- **Result**: The calculation result is returned and stored in `result`
- **`print(result)`**: Displays the calculated result

### Example
```
User enters: 2 + 6 - 1
eval() processes: 2 + 6 - 1
Output: 7  ← Correctly calculated!
```

### More Examples
```python
result = eval(input('enter an expr'))

# User enters: 10 * 5
# Output: 50

# User enters: 100 / 2 + 5
# Output: 55.0

# User enters: 2 ** 8
# Output: 256
```

### Supported Operations
```python
eval("5 + 3")        # 8
eval("10 - 4")       # 6
eval("7 * 6")        # 42
eval("20 / 4")       # 5.0
eval("2 ** 3")       # 8 (exponentiation)
eval("10 % 3")       # 1 (modulo)
eval("(5 + 3) * 2")  # 16
```

### ⚠️ Important Security Warning

**`eval()` is dangerous** and should NOT be used with untrusted user input!

#### Why?
- **Arbitrary code execution**: Users could enter malicious code
- **Security risk**: Can access/modify variables and execute dangerous operations

#### Example of Risk
```python
# User enters: __import__('os').system('rm -rf /')
result = eval(input())  # EXTREMELY DANGEROUS!
```

#### Safe Alternatives
```python
# Use ast.literal_eval() for safe evaluation of literals
import ast
result = ast.literal_eval(input())  # Only evaluates literals

# Or use specific conversion
x = int(input())       # Only accept integers
y = float(input())     # Only accept floats
```

---

## Comparison Summary

| Function | Purpose | Input Type | Output Type | Example |
|----------|---------|-----------|------------|---------|
| `input()` | Get user input | String | String | `input() → "5"` |
| `int(input())` | Get number input | String | Integer | `int(input()) → 5` |
| `float(input())` | Get decimal input | String | Float | `float(input()) → 5.5` |
| `eval(input())` | Evaluate expression | String expression | Result | `eval(input()) → 7` |

---

## Complete Working Examples

### Example 1: Calculator
```python
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print(f'Sum: {x + y}')
print(f'Difference: {x - y}')
print(f'Product: {x * y}')
print(f'Division: {x / y}')
```

### Example 2: Name and Age
```python
name = input('Enter your name: ')
age = int(input('Enter your age: '))
print(f'Hello {name}, you are {age} years old')
```

### Example 3: Mathematical Calculation
```python
radius = float(input('Enter radius: '))
import math
area = math.pi * radius ** 2
print(f'Area of circle: {area}')
```

### Example 4: Using eval() for Expressions
```python
expression = input('Enter a mathematical expression: ')
result = eval(expression)
print(f'Result: {result}')
```

---

## Key Takeaways

### Math Module
- ✅ Use `import math` to access mathematical functions
- ✅ Common functions: `sqrt()`, `floor()`, `ceil()`, `pow()`
- ✅ Common constants: `pi`, `e`
- ✅ Use aliases with `import math as m` for shorter code
- ✅ Import specific functions with `from math import function_name`

### User Input
- ✅ `input()` ALWAYS returns a string
- ✅ Use `int(input())` for integer input
- ✅ Use `float(input())` for decimal input
- ✅ Add a prompt message: `input('Enter value: ')`
- ⚠️ Avoid `eval()` with untrusted user input (security risk)
- ✅ Use `int()`, `float()` for safe type conversion

---

## Practice Exercises

1. **Math Module**
   - Calculate the area of a circle with radius 7
   - Find the square root of 144
   - Use `floor()` and `ceil()` on 3.7

2. **User Input**
   - Create a simple calculator that adds two numbers
   - Get user's name and age, display in a sentence
   - Create a program that takes a radius and calculates circle area

3. **Combined**
   - Get two numbers from user, calculate their square roots
   - Get an expression from user and use `eval()` to calculate
   - Get a string, extract and display individual characters

---

**Created for Python Learning Journey** | Notebook: Module_Framwork_Input-fun..ipynb
