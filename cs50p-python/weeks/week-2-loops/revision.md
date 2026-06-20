# CS50P Week 2 — Loops (Revision Sheet)

## Loop Types

### `while`

Runs while condition is `True`.

```python
while condition:
    ...
```

### `for`

Runs a fixed number of times.

```python
for _ in range(n):
    ...
```

`range(n)` → `0` to `n-1`

---

## Loop Control

```python
break
```

Exit loop immediately.

```python
continue
```

Skip current iteration.

---

## Input Validation Pattern

```python
while True:
    n = int(input("Number: "))
    if n > 0:
        break
```

Or:

```python
while True:
    n = int(input("Number: "))
    if n > 0:
        return n
```

---

## Lists

```python
students = ["Harry", "Ron", "Hermione"]
```

Access:

```python
students[0]
```

Length:

```python
len(students)
```

Loop:

```python
for student in students:
    print(student)
```

---

## Dictionaries

```python
student = {
    "name": "Harry",
    "house": "Gryffindor"
}
```

Access:

```python
student["name"]
```

Loop:

```python
for key in student:
    print(key, student[key])
```

---

## List of Dictionaries

```python
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]
```

```python
for student in students:
    print(student["name"])
```

---

## Nested Loops

Outer = Rows

Inner = Columns

```python
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()
```

---

## Useful Tricks

### String Repetition

```python
print("#" * 5)
```

### No Newline

```python
print("#", end="")
```

### Iterate String

```python
for c in "Harry":
    print(c)
```

---

## Common Errors

### Infinite Loop

```python
i = 0
while i < 3:
    print(i)
```

Forgot:

```python
i += 1
```

### Off-by-One

```python
range(3)
```

Produces:

```text
0, 1, 2
```

NOT:

```text
0, 1, 2, 3
```

---

## Week 2 Exam Checklist

✅ `while`

✅ `for`

✅ `range()`

✅ `break`

✅ `continue`

✅ Input Validation

✅ Lists

✅ Dictionaries

✅ Lists of Dictionaries

✅ Nested Loops

✅ `len()`

✅ `end=""`

✅ String Multiplication (`"*" * n`)

---

## Golden Rule

**If you're copying and pasting code, use a loop.**
