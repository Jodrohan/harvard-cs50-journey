# CS50P Week 1 — Conditionals & Control Flow

## 🔀 if / elif / else

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

* `if` → checked first
* `elif` → checked only if above failed
* `else` → catches everything else

### First True Wins

```python
if x > 0:
    ...
elif x > 10:
    ...
```

Python executes the first True condition and ignores the rest.

**Rule:** Put specific conditions before broad ones.

---

## 🚨 else Trap

❌

```python
else age < 18:
```

✅

```python
else:
```

Need another condition? Use `elif`.

---

## 🗂️ match / case

```python
match role:
    case "admin":
        ...
    case "user":
        ...
    case _:
        ...
```

* `|` = inline `or`

```python
case "admin" | "root":
```

* `_` = wildcard (same as `else`)

---

## 🛑 return (Early Exit)

```python
if intruder:
    return
```

`return`:

1. Stops the function immediately.
2. Optionally sends back a value.

```python
return n * n
```

Code below `return` never runs.

---

## ⚖️ Pythonic Booleans

❌

```python
if n % 2 == 0:
    return True
else:
    return False
```

✅

```python
return n % 2 == 0
```

Use directly:

```python
if is_even(n):
```

---

## 🔗 Boolean Operators

```python
and  # both true
or   # at least one true
not  # opposite
```

Examples:

```python
age >= 18 and has_id
name == "Harry" or name == "Hermione"
not logged_in
```

---

## ⚖️ Comparison Operators

```python
==  equal
!=  not equal
>   greater than
<   less than
>=  greater/equal
<=  less/equal
```

Common mistake:

```python
=   assignment
==  comparison
```

---

## 🎭 Truthy & Falsy

Falsy values:

```python
False
None
0
0.0
""
[]
{}
set()
```

Everything else is usually Truthy.

```python
if name:
```

Instead of:

```python
if name != "":
```

---

## ✂️ input() Type Trap

`input()` always returns a string.

```python
x = input("x: ")
y = input("y: ")
```

```python
"1" + "1" -> "11"
```

Convert before math:

```python
int(x) + int(y)
float(x) + float(y)
```

**Rule:**

```text
Strings = Text
Ints/Floats = Math
```

---

## 🧰 Essential String Methods

```python
.strip()  # remove whitespace
.lower()  # lowercase text
.split()  # split into pieces
```

Example:

```python
x, op, z = expression.split(" ")
```

---

## 🎯 Week 1 Checklist

* First True Wins?
* Need `elif` instead of `else`?
* Can I use `return` early?
* Can I directly return a boolean?
* Using `and/or/not` correctly?
* Still dealing with strings?
* Need `int()` or `float()`?
* Used `.strip()` / `.lower()`?

---

## 🏅 Mastery Topics

1. `if / elif / else`
2. First True Wins
3. `match / case`
4. `case _`
5. `return`
6. `and / or / not`
7. Comparison operators
8. Truthy vs Falsy
9. Direct boolean returns
10. String → Number conversion
11. `.strip()`
12. `.lower()`
13. `.split()`
