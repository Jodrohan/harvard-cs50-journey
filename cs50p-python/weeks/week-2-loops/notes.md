# 🔁 Week 2: Loops & Iteration (CS50P)

## 📌 Overview

Week 2 introduces loops, allowing code to repeat instead of running only from top to bottom. This helps follow the DRY (Don't Repeat Yourself) principle and makes programs more efficient.

---

## 🛑 1. While Loops & Loop Control

A `while` loop repeats as long as a condition remains true.

### Standard Pattern

1. Initialize a counter.
2. Check a condition.
3. Update the counter inside the loop.

```python
i = 0

while i < 3:
    print("meow")
    i += 1
```

### Infinite Loops

Forgetting to update the counter can cause the loop to run forever.

```python
while True:
    print("meow")
```

To stop a stuck program in the terminal:

```bash
Ctrl + C
```

### Input Validation

A common pattern is using `while True` until valid input is received.

```python
while True:
    n = int(input("Number: "))
    if n > 0:
        break
```

### Loop Control Keywords

#### `break`

Exits the loop immediately.

```python
if n > 0:
    break
```

#### `continue`

Skips the current iteration and returns to the top of the loop.

```python
if n < 0:
    continue
```

---

## 🔄 2. For Loops & Iteration

A `for` loop is used when iterating through a collection or repeating something a known number of times.

### Direct Iteration

```python
students = ["Harry", "Hermione", "Ron"]

for student in students:
    print(student)
```

### `range()`

`range(n)` generates numbers from `0` up to (but not including) `n`.

```python
for i in range(3):
    print("meow")
```

### Throwaway Variable (`_`)

Use `_` when the loop variable is not needed.

```python
for _ in range(3):
    print("meow")
```

---

## 🖨️ 3. Overriding `print()` Defaults

By default:

* `print()` adds a newline (`\n`) at the end.
* Multiple arguments are separated by a space.

### `end=""`

Keeps printing on the same line.

```python
for _ in range(3):
    print("?", end="")
```

### `sep=""`

Removes the default space between arguments.

```python
print("A", "B", "C", sep="")
```

---

## 🗂️ 4. Data Structures: Lists & Dictionaries

### Lists (`[]`)

Ordered collections of data.

```python
students = ["Harry", "Hermione", "Ron"]
```

Instead of:

```python
for i in range(len(students)):
```

Prefer:

```python
for student in students:
```

### Dictionaries (`{}`)

Store data as key-value pairs.

```python
student = {
    "name": "Harry",
    "house": "Gryffindor"
}
```

Iterating through a dictionary gives the keys:

```python
for key in student:
    print(key)
```

Access values using the key:

```python
print(student[key])
```

### `.items()`

Access both keys and values together.

```python
for key, value in student.items():
    print(key, value)
```

### `None`

Represents the absence of a value.

```python
x = None
```

---

## 🧱 5. Nested Loops & Abstraction

### Nested Loops

A nested loop is a loop inside another loop.

```python
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()
```

Useful for grids, tables, and simple patterns.

### Abstraction

Breaking code into smaller functions makes it easier to read and reuse.

```python
def print_row():
    print("#####")

def print_square():
    for _ in range(5):
        print_row()
```

Abstraction helps keep programs organized and maintainable.

---

## 📚 Week 2 Key Takeaways

* Use `while` when the number of repetitions is unknown.
* Use `for` when iterating over data or a known range.
* `break` exits a loop immediately.
* `continue` skips the current iteration.
* `range()` generates sequences of numbers.
* Use `_` for unused loop variables.
* `end=""` and `sep=""` modify `print()` behavior.
* Lists store ordered data.
* Dictionaries store key-value pairs.
* Nested loops help create grids and patterns.
* Abstraction means breaking complex tasks into smaller functions.
