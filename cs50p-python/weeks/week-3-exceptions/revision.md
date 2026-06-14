# Week 3: Performance & Debugging Revision Notes

> **Core Philosophy Learned:** Never trust user input. Assume users will try to break the program. Use loops to trap invalid input until valid data is provided, and use `try/except` as a blast shield to prevent crashes.

---

## 💡 1. Logic Breakthroughs (The "Aha!" Moments)

### The Containment Strategy

I cannot simply check if input is bad and let the program continue running. If a user enters garbage data, the code needs to be trapped inside a `try` block so it immediately resets the loop before it can crash the rest of the program.

### Data Mapping is Powerful

Instead of writing long chains of `if/else` statements for months, storing month names in a list and using their `.index()` position is much cleaner and easier to maintain.

### The "Gatekeeper" Break

The `break` statement inside a `while True` loop is dangerous. It must be the **last line executed inside the `try` block**, protected by validation logic that confirms the data is 100% valid.

---

## 🛑 2. Specific Traps & How I Beat Them

### 💀 Trap 1: The `NameError` Ambush (Variable Scope)

**What I did:**

```python
month = int(month)
```

I tried to run this outside of my `try` block. If the `try` block failed early due to bad input, the variable `month` was never created, causing the program to crash anyway.

**How I Fixed It:**

I moved the entire conversion, validation, and output process inside the `try` block. If the data is bad, execution jumps safely to `except` and skips the dangerous code.

---

### 💀 Trap 2: The "Ghost" String Replacement

**What I did:**

```python
date.replace(",", "")
```

Python strings are immutable. This created a modified string but immediately discarded it.

**How I Fixed It:**

Always assign string modifications back to a variable:

```python
date = date.replace(",", "")
```

---

### 💀 Trap 3: The Premature Break

**What I did:**

I placed `break` after the `except` block, causing the loop to terminate even when the user entered invalid data.

**How I Fixed It:**

The `break` acts as the ultimate Gatekeeper. It only executes after all validation checks pass.

```python
if 1 <= month <= 12:
    break
```

---

### 💀 Trap 4: Method vs. List Lookup Syntax

**What I did:**

```python
months.index[month]
```

I used square brackets on a method.

**How I Fixed It:**

Methods are functions and require parentheses:

```python
months.index(month)
```

Square brackets are only used to access list positions:

```python
months[0]
```

---

## 🛠️ 3. Tool Mastery (Code Snippets I Nailed)

### Dictionary Frequencies (`grocery.py`)

I learned how to count occurrences dynamically without knowing what the user will enter beforehand.

```python
# Count occurrences cleanly
grocery_list[item] = grocery_list.get(item, 0) + 1

# Print alphabetically by key
for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item}")
```

---

### Number Translation via Lists (`outdated.py`)

I learned to convert a month name into a numerical value using its position inside a list.

```python
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Add 1 because list indexing starts at 0
month_number = months.index("September") + 1
```

---

### F-String Zero Padding

I learned how to enforce a fixed-width number format when printing dates.

```python
# :02d adds a leading zero to single-digit numbers
print(f"{year}-{month:02d}-{day:02d}")
```

---

## 🎯 Week 3 Takeaway

The biggest lesson from this week was learning that **robust programs are not built around ideal user behavior—they are built around handling bad input safely.** Loops, validation checks, and `try/except` blocks work together to prevent crashes and ensure the program only continues when the data is valid.
