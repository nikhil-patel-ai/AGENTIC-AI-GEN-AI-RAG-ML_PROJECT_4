# OTP Generator

This notebook demonstrates how to generate a numeric one-time password (OTP) in Python using the `random` module.

## Features

- Generates an OTP with a configurable length.
- Produces numeric output as a string, so leading zeroes are preserved.
- Uses a reusable `generate_otp()` function.

## Requirements

- Python 3.x
- Jupyter Notebook or VS Code with the Jupyter extension

No external packages are required.

## Usage

Open [OTP-Generator.ipynb](OTP-Generator.ipynb) and run the Python cell:

```python
import random

def generate_otp(length=4):
    digits = '012345'
    return ''.join(random.choice(digits) for _ in range(length))

otp = generate_otp(4)
print(f"Your OTP is: {otp}")
```

Example output:

```text
Your OTP is: 3041
```

## Custom Length

Pass the desired length to `generate_otp()`:

```python
otp = generate_otp(6)
```

The current notebook generates OTPs from the digit set `012345`.

## Note

This is an educational example. Production authentication systems should use a cryptographically secure generator such as Python's `secrets` module and should apply expiry, retry limits, and secure delivery controls.
