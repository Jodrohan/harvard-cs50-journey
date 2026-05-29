# CS50P Week 0 — Functions, Variables

## What I Learned

- Programming is input → process → output
- Python executes code from top to bottom
- Variables store data
- Functions perform reusable actions
- `input()` gets user input
- `print()` displays output
- Strings are text inside quotes
- `int()` converts text into integers
- `float()` converts text into decimal numbers
- `.lower()` converts text to lowercase
- `return` sends values back from functions
- `.replace()` replaces matching text inside a string

---

## First Python Program

```python
print("hello, world")
```

---

## Assignment Completed

### indoor.py

Convert user input into lowercase text using `.lower()`.

```python
a = input("Enter a string: ")
print(a.lower())
```

---

## More String Methods

- `.capitalize()` makes only the first letter capital

```python
print("rohan".capitalize())
```

- `.title()` makes the first letter of every word capital

```python
print("rohan somriya".title())
```

- `.split()` breaks a single string into multiple parts

```python
name = "Rohan Somriya"
first, last = name.split(" ")
```

This can separate first name and last name.

---

## Integers

- Integers are whole numbers
- They do not contain decimal points
- They can be positive, negative, or zero

### Using int()

```python
x = int(input("What's x? "))
```

`int()` converts normal string input into a mathematical integer.

### Addition Calculator

```python
a = int(input("What's a? "))
b = int(input("What's b? "))

print(a + b)
```

---

## Floats

- Floats are decimal numbers

### Using float()

```python
x = float(input("What's x? "))
```

This allows decimal mathematics in Python.

---

## round()

`round()` is used to round decimal values.

```python
z = round(3.14159)
```

---

## Number Formatting

### Adding Commas

```python
a = float(input("What's a? "))
b = float(input("What's b? "))

z = a + b

print(f"{z:,}")
```

Output:

```text
1,000
```

### Limiting Decimal Places

```python
print(f"{z:.2f}")
```

This prints only 2 decimal places.

---

## Functions with def

- Functions allow reusable code
- Instead of rewriting the same logic repeatedly, we can create a function and call it whenever needed
- Functions help keep large programs cleaner and more organized

---

## Parameters & Arguments

### Parameter

A variable inside the function definition.

```python
def hello(name):
```

`name` is a parameter.

### Argument

The actual value passed into the function.

```python
hello("Rohan")
```

`"Rohan"` is an argument.

---

## Function Example

```python
def hello(name):
    print("hello", name)

hello("Rohan")
hello("David")
```

---

## Focused Functions

- It is better for one function to do one specific task
- Smaller functions make programs easier to:
  - understand
  - debug
  - maintain

---

## Default Parameters

```python
def hello(to="world"):
    print("hello", to)
```

If no argument is given, `"world"` becomes the default value.

---

## Using main()

`main()` is commonly used to control program flow.

```python
def main():
    name = input("Enter name: ")
    hello(name)

def hello(to="world"):
    print("hello", to)

main()
```

---

## return

`return` sends a value back from a function.

```python
def square(n):
    return n * n
```

---

## Square Calculator Program

```python
def main():
    x = int(input("Enter number: "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()
```

### Program Flow

1. User enters a number
2. `square(x)` is called
3. `pow(n, 2)` calculates the square
4. `return` sends the result back
5. `print()` displays the output

---

## Important Concepts

### input() always returns a string

```python
x = input("What's x? ")
```

Even if user types:

```text
5
```

Python still stores it as:

```python
"5"
```

That is why `int()` or `float()` is needed for mathematics.

---

### Difference Between print() and return()

- `print()` displays output
- `return` sends a value back from a function

```python
def square(n):
    return n * n
```

---

### Function Flow

```text
main() → calls another function → function returns value → output is printed
```