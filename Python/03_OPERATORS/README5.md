# Number System & Bitwise Operators

## Table of Contents
1. [Number Systems](#number-systems)
2. [Bitwise Operators](#bitwise-operators)
3. [Practical Examples](#practical-examples)
4. [Key Takeaways](#key-takeaways)

---

## Number Systems

### Overview
A number system is a way of representing numbers using digits and symbols. Python supports four main number systems:
- **Binary** (Base 2): Uses digits 0 and 1
- **Octal** (Base 8): Uses digits 0-7
- **Decimal** (Base 10): Uses digits 0-9 (default number system)
- **Hexadecimal** (Base 16): Uses digits 0-9 and letters A-F (case-insensitive)

### 1. Binary Number System

**Definition:** Binary is a base-2 number system using only two digits: 0 and 1. It's the fundamental language of computers.

**Prefix in Python:** `0b` or `0B`

**Example:**
```python
0b11001  # Binary representation of 25
```

#### Decimal to Binary Conversion
Use the `bin()` function to convert decimal numbers to binary:
```python
bin(25)   # Returns '0b11001'
# 25 in binary is 11001
# Calculation: 1×2⁴ + 1×2³ + 0×2² + 0×2¹ + 1×2⁰ = 16 + 8 + 1 = 25
```

#### Binary to Decimal Conversion
Use the `int()` function with binary notation:
```python
int(0b11001)  # Returns 25
# Convert binary 11001 back to decimal
```

---

### 2. Octal Number System

**Definition:** Octal is a base-8 number system using digits 0-7. It was commonly used in computer systems.

**Prefix in Python:** `0o` or `0O`

**Example:**
```python
0o31  # Octal representation of 25
```

#### Decimal to Octal Conversion
Use the `oct()` function:
```python
oct(25)   # Returns '0o31'
# 25 in octal is 31
# Calculation: 3×8¹ + 1×8⁰ = 24 + 1 = 25
```

#### Octal to Decimal Conversion
Use the `int()` function with octal notation:
```python
int(0o31)  # Returns 25
# Convert octal 31 back to decimal
```

---

### 3. Decimal Number System

**Definition:** Decimal is a base-10 number system using digits 0-9. It's the most commonly used number system in everyday life and the default in Python.

**Prefix in Python:** No prefix needed

**Example:**
```python
25  # This is 25 in decimal
45  # Another decimal number
```

Decimal is the default representation, so when you type a regular number, it's automatically interpreted as decimal.

---

### 4. Hexadecimal Number System

**Definition:** Hexadecimal is a base-16 number system using digits 0-9 and letters A-F (where A=10, B=11, C=12, D=13, E=14, F=15). It's widely used in computing for memory addresses, color codes, and more.

**Prefix in Python:** `0x` or `0X`

**Example:**
```python
0x19  # Hexadecimal representation of 25
```

#### Decimal to Hexadecimal Conversion
Use the `hex()` function:
```python
hex(25)   # Returns '0x19'
# 25 in hexadecimal is 19
# Calculation: 1×16¹ + 9×16⁰ = 16 + 9 = 25

hex(10)   # Returns '0xa'  (10 in decimal = A in hexadecimal)
hex(15)   # Returns '0xf'  (15 in decimal = F in hexadecimal)
hex(255)  # Returns '0xff' (255 in decimal = FF in hexadecimal)
```

#### Hexadecimal to Decimal Conversion
Use the `int()` function with hexadecimal notation:
```python
int(0x19)  # Returns 25
int(0xa)   # Returns 10
int(0xff)  # Returns 255
```

---

### Number System Conversion Chart

#### From Binary
- **Binary to Decimal:** `int(0b11001)` → 25
- **Binary to Octal:** `oct(0b11001)` → '0o31'
- **Binary to Hexadecimal:** `hex(0b11001)` → '0x19'

#### From Octal
- **Octal to Binary:** `bin(0o31)` → '0b11001'
- **Octal to Decimal:** `int(0o31)` → 25
- **Octal to Hexadecimal:** `hex(0o31)` → '0x19'

#### From Decimal
- **Decimal to Binary:** `bin(25)` → '0b11001'
- **Decimal to Octal:** `oct(25)` → '0o31'
- **Decimal to Hexadecimal:** `hex(25)` → '0x19'

#### From Hexadecimal
- **Hexadecimal to Binary:** `bin(0x19)` → '0b11001'
- **Hexadecimal to Octal:** `oct(0x19)` → '0o31'
- **Hexadecimal to Decimal:** `int(0x19)` → 25

---

## Bitwise Operators

### Overview
Bitwise operators work directly on binary representations of integers. They perform operations on individual bits (0 or 1) of numbers. These operators are crucial for low-level programming, cryptography, graphics, and performance optimization.

### Understanding Binary Operations

Before exploring each operator, let's understand how numbers look in binary:
- **12 in binary:** `0b1100` (1×8 + 1×4 + 0×2 + 0×1)
- **13 in binary:** `0b1101` (1×8 + 1×4 + 0×2 + 1×1)

---

### 1. Bitwise Complement (~)

**Definition:** The bitwise NOT operator inverts all bits in a number. It changes 0s to 1s and 1s to 0s.

**Syntax:** `~x`

**How it works:**
- Python uses two's complement representation for negative numbers
- Formula: `~x = -(x + 1)`

**Examples:**
```python
~12   # Returns -13
# 12 in binary: 00001100
# ~12 flips all bits: 11110011 (which is -13 in two's complement)

~35   # Returns -36
# Calculation: -(35 + 1) = -36

~18   # Returns -19
# Calculation: -(18 + 1) = -19
```

**Use Cases:**
- Toggling all bits in a number
- Finding the negative of a number minus 1
- Low-level bit manipulation

---

### 2. Bitwise AND (&)

**Definition:** The AND operator returns 1 only when both bits are 1; otherwise, it returns 0.

**Syntax:** `x & y`

**Truth Table:**
| a | b | a & b |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

**Example:**
```python
12 & 13  # Returns 12
# 12 in binary: 1100
# 13 in binary: 1101
# AND result:   1100 (which is 12)
# Bit-by-bit:
#   1 & 1 = 1
#   1 & 1 = 1
#   0 & 0 = 0
#   0 & 1 = 0
```

**Use Cases:**
- Checking if a specific bit is set
- Clearing specific bits
- Masking operations
- Checking if a number is even: `n & 1 == 0`

---

### 3. Bitwise OR (|)

**Definition:** The OR operator returns 1 when at least one bit is 1; it returns 0 only when both bits are 0.

**Syntax:** `x | y`

**Truth Table:**
| a | b | a \| b |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

**Example:**
```python
12 | 13  # Returns 13
# 12 in binary: 1100
# 13 in binary: 1101
# OR result:    1101 (which is 13)
# Bit-by-bit:
#   1 | 1 = 1
#   1 | 1 = 1
#   0 | 0 = 0
#   0 | 1 = 1
```

**Use Cases:**
- Setting specific bits to 1
- Combining bit flags
- Creating masks
- Enabling features in bit-packed data

---

### 4. Bitwise XOR (^)

**Definition:** The XOR (exclusive OR) operator returns 1 when bits are different; it returns 0 when bits are the same.

**Syntax:** `x ^ y`

**Truth Table:**
| a | b | a ^ b |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

**Example:**
```python
12 ^ 13  # Returns 1
# 12 in binary: 1100
# 13 in binary: 1101
# XOR result:   0001 (which is 1)
# Bit-by-bit:
#   1 ^ 1 = 0
#   1 ^ 1 = 0
#   0 ^ 0 = 0
#   0 ^ 1 = 1
```

**Use Cases:**
- Toggling specific bits
- Finding differences between numbers
- Swapping variables without a temporary variable: `a = a ^ b; b = a ^ b; a = a ^ b`
- Encryption and cryptography
- Error detection

---

### 5. Left Shift (<<)

**Definition:** The left shift operator shifts all bits to the left by a specified number of positions. Empty positions on the right are filled with zeros.

**Syntax:** `x << n`

**Effect:** Multiplies the number by 2^n

**Examples:**
```python
12 << 1  # Returns 24
# 12 in binary:     1100
# Shift left by 1: 11000 (which is 24)
# Calculation: 12 × 2¹ = 24

12 << 2  # Returns 48
# 12 in binary:      1100
# Shift left by 2: 110000 (which is 48)
# Calculation: 12 × 2² = 48
```

**Use Cases:**
- Multiplying by powers of 2 (faster than * operator)
- Setting specific bits
- Creating bitmasks
- Encoding data

---

### 6. Right Shift (>>)

**Definition:** The right shift operator shifts all bits to the right by a specified number of positions. For positive numbers, empty positions on the left are filled with zeros.

**Syntax:** `x >> n`

**Effect:** Divides the number by 2^n (integer division)

**Examples:**
```python
12 >> 1  # Returns 6
# 12 in binary:      1100
# Shift right by 1:   110 (which is 6)
# Calculation: 12 ÷ 2¹ = 6

12 >> 2  # Returns 3
# 12 in binary:      1100
# Shift right by 2:    11 (which is 3)
# Calculation: 12 ÷ 2² = 3

12 >> 3  # Returns 1
# 12 in binary:      1100
# Shift right by 3:     1 (which is 1)
# Calculation: 12 ÷ 2³ = 1

12 >> 4  # Returns 0
# 12 in binary:      1100
# Shift right by 4:      (all bits shifted out, result is 0)
# Calculation: 12 ÷ 2⁴ = 0

12 >> 5  # Returns 0
# All bits have been shifted out, result remains 0
```

**Use Cases:**
- Dividing by powers of 2 (faster than / operator)
- Extracting specific bits
- Reducing bit width
- Parsing data structures

---

## Practical Examples

### Example 1: Checking if a Bit is Set
```python
# Check if the 3rd bit (from right, 0-indexed) is set in number 12
def is_bit_set(num, position):
    return (num & (1 << position)) != 0

result = is_bit_set(12, 2)  # Check if 3rd bit is set
# 12 = 1100 in binary, 3rd bit (position 2) is 1, so result is True
```

### Example 2: Setting a Specific Bit
```python
# Set the nth bit in a number
def set_bit(num, position):
    return num | (1 << position)

result = set_bit(8, 2)  # Set 3rd bit
# 8 = 1000, setting bit at position 2 gives 1100 = 12
```

### Example 3: Clearing a Specific Bit
```python
# Clear (set to 0) the nth bit in a number
def clear_bit(num, position):
    return num & ~(1 << position)

result = clear_bit(12, 2)  # Clear 3rd bit
# 12 = 1100, clearing bit at position 2 gives 1000 = 8
```

### Example 4: Toggling a Specific Bit
```python
# Toggle (flip) the nth bit in a number
def toggle_bit(num, position):
    return num ^ (1 << position)

result = toggle_bit(12, 0)  # Toggle 1st bit
# 12 = 1100, toggling bit at position 0 gives 1101 = 13
```

---

## Key Takeaways

### Number Systems
1. **Binary** is essential for understanding computer operations
2. **Hexadecimal** is convenient for representing large binary numbers
3. **Octal** is less common but still appears in some legacy systems
4. Python provides built-in functions to convert between number systems:
   - `bin()`, `oct()`, `hex()` for converting TO these systems
   - `int(x, base)` for converting FROM these systems

### Bitwise Operators
1. **Bitwise operators** work on the binary representation of numbers
2. They are extremely fast and are used for:
   - Low-level programming
   - Performance-critical code
   - Cryptography and security
   - Graphics and gaming
   - System programming

3. **Common patterns:**
   - `x & 1` → Check if odd (1) or even (0)
   - `x | y` → Combine flags
   - `x ^ y` → Find differences or toggle
   - `x << n` → Multiply by 2^n
   - `x >> n` → Divide by 2^n (integer division)

### Important Notes
- Python integers have unlimited precision, unlike some other languages
- Bitwise operations follow two's complement representation for negative numbers
- Right shift on negative numbers fills with 1s (arithmetic shift), not 0s
- Bitwise operators have higher precedence than comparison operators but lower than arithmetic operators

---

## Practice Problems

1. Convert the decimal number 100 to binary, octal, and hexadecimal
2. Using bitwise operations, find if a number is a power of 2
3. Create a function to count the number of set bits (1s) in a binary number
4. Use bitwise XOR to swap two variables without a temporary variable
5. Implement a function to extract specific bits from a number using right shift and AND operations

---

## References
- Python Official Documentation: https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integers
- Binary, Octal, Decimal, Hexadecimal: https://en.wikipedia.org/wiki/Radix
- Two's Complement: https://en.wikipedia.org/wiki/Two%27s_complement
