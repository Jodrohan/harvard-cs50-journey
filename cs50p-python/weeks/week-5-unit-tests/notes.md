# CS50P Week 5: Unit Testing

## Introduction

As programs become larger and more complex, manually testing them becomes inefficient. Instead of repeatedly running a program and entering inputs ourselves, we can write code that automatically tests our functions.

Unit testing is the process of testing individual functions (units) of code to ensure they behave as expected.

---

# Writing Testable Code

To test a function automatically, the function must return a value.

### Not Testable

```python
def square(n):
    print(n * n)
```

This only displays output to the screen and returns `None`.

### Testable

```python
def square(n):
    return n * n
```

Now other code can examine the returned value and verify its correctness.

---

# Manual Testing

A simple approach is to create another file and manually check outputs.

```python
from calculator import square

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
```

This works, but quickly becomes repetitive and difficult to maintain.

---

# The assert Keyword

Python provides the `assert` keyword to simplify testing.

```python
from calculator import square

def test_square():
    assert square(2) == 4
```

An assertion states that a condition must be true.

If the condition is false, Python raises:

```text
AssertionError
```

Multiple assertions can be written:

```python
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0
```

The drawback is that execution stops when the first failing assertion is encountered.

---

# Using pytest

`pytest` is a third-party library that automates testing.

Install:

```bash
pip install pytest
```

Run:

```bash
pytest
```

or

```bash
pytest test_calculator.py
```

Pytest automatically:

* Finds tests
* Runs tests
* Reports failures
* Provides useful error messages

---

# Pytest Discovery Rules

Pytest looks for specific naming conventions.

### Test Files

```text
test_calculator.py
```

or

```text
calculator_test.py
```

### Test Functions

```python
def test_square():
```

Functions must begin with `test_`.

---

# Organizing Tests

Rather than placing all assertions inside one function, tests should be grouped logically.

```python
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4

def test_zero():
    assert square(0) == 0
```

Benefits:

* Easier debugging
* Clearer failure reports
* Better organization

---

# Testing Strings

Testing strings follows the same process.

Function:

```python
def hello(name="world"):
    return f"hello, {name}"
```

Tests:

```python
def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"
```

Unit testing is not limited to numbers.

---

# Testing for Exceptions

Some inputs should cause errors.

Example:

```python
square("cat")
```

A proper implementation should raise a `TypeError`.

Pytest allows testing for exceptions using `pytest.raises()`.

```python
import pytest
from calculator import square

def test_str():
    with pytest.raises(TypeError):
        square("cat")
```

The test passes only if the expected exception occurs.

---

# Edge Cases

Good tests examine more than normal inputs.

Examples:

```python
square(2)      # normal input
square(0)      # boundary case
square(-2)     # negative value
square("cat")  # invalid input
```

A strong test suite considers all reasonable categories of input.

---

# The main() Pattern

Programs are often structured as:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

This ensures that `main()` runs only when the file is executed directly.

When another file imports the module:

```python
from calculator import square
```

the program's main logic will not execute automatically.

This is important for testing.

---

# Packages

As projects grow, multiple files may be organized into folders.

Example:

```text
project/
│
├── calculator.py
├── test_calculator.py
│
└── helpers/
    ├── __init__.py
    └── math_utils.py
```

The file:

```text
__init__.py
```

tells Python to treat the folder as a package.

This allows modules inside the folder to be imported and used more easily.

---

# Key Concepts

* Unit testing verifies individual functions.
* Functions should return values instead of only printing them.
* `assert` checks whether a condition is true.
* `pytest` automates testing.
* Test files and test functions follow specific naming conventions.
* Tests should be separated into logical categories.
* `pytest.raises()` tests expected exceptions.
* Edge cases should always be tested.
* `if __name__ == "__main__"` prevents code from running during imports.
* `__init__.py` identifies a package.
