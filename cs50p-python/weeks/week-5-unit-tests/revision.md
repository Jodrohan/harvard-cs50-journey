# CS50P Week 5 — Personal Revision Notes

> These notes focus on **my actual mistakes and weak areas** during Week 5, not on the entire curriculum.

---

# Biggest Lesson

## Think First, Code Later

When a problem feels difficult:

❌ Don't start typing Python immediately.

✅ Write the logic in plain English first.

Example:

```text
Check length

Check first two letters

Loop through each character

If first number is 0:
    reject

If a letter appears after numbers:
    reject

Otherwise:
    accept
```

### Personal Rule

```text
English → Pseudocode → Python
```

---

# Weakness #1: Returning Too Early

This was my most common mistake.

### Wrong

```python
if condition:
    return True
else:
    return False
```

before checking all requirements.

### Correct

```python
if bad_condition:
    return False

if another_bad_condition:
    return False

return True
```

### Mental Model

> Reject first. Approve last.

---

# Weakness #2: Forgetting Parentheses

I repeatedly wrote:

### Wrong

```python
s.isalpha
s.isdigit
s.startswith
```

### Correct

```python
s.isalpha()
s.isdigit()
s.startswith()
```

### Remember

If it performs an action, it needs `()`.

Common offenders:

```python
.isalpha()
.isdigit()
.startswith()
.lower()
.upper()
.strip()
.replace()
```

---

# Weakness #3: Strings Are Immutable

I often expected strings to change themselves.

### Wrong

```python
greeting.lower()
```

### Correct

```python
greeting = greeting.lower()
```

Same idea:

### Wrong

```python
name.strip()
text.replace("a", "")
```

### Correct

```python
name = name.strip()
text = text.replace("a", "")
```

### Rule

> String methods return a new string.

Save the result.

---

# Weakness #4: Testing Output Instead of Return Values

### Wrong

```python
assert is_valid("AB") == "valid"
```

### Correct

```python
assert is_valid("AB") == True
```

### Remember

Pytest tests:

* Function returns
* Function behavior

Not terminal output.

---

# Weakness #5: Writing Tests Too Late

I tend to focus only on making the code work.

A better workflow:

```text
Write function

Think of edge cases

Write tests

Run pytest

Fix failures
```

---

# Pytest Checklist

Every function should be tested with:

* Normal input
* Edge cases
* Uppercase input
* Lowercase input
* Numbers
* Symbols
* Spaces
* Invalid values

Example:

```python
assert shorten("aeiou") == ""
assert shorten("CS50!") == "CS50!"
assert shorten("I am Iron Man") == " m rn Mn"
```

---

# Pytest Rules

Test file:

```text
test_*.py
```

Test function:

```python
def test_something():
```

Must begin with:

```text
test_
```

Otherwise pytest ignores it.

---

# Vanity Plates Strategy

## Step 1 — Length

```python
if len(s) < 2 or len(s) > 6:
    return False
```

---

## Step 2 — First Two Characters

```python
if not s[:2].isalpha():
    return False
```

---

## Step 3 — Track Numbers

Use a switch:

```python
number_started = False
```

---

## Step 4 — Loop Through Characters

```python
for char in s:
```

---

## Step 5 — Reject If

* First number is `0`
* Letter appears after numbers
* Punctuation exists
* Spaces exist

---

## Step 6 — Survival Hatch

```python
return True
```

Only after all checks pass.

---

# Week 5 Personal Debugging Checklist

Before asking for help:

### 1. Did I forget `()`?

```python
.isalpha()
.isdigit()
.startswith()
```

---

### 2. Did I save the result?

```python
text = text.lower()
```

---

### 3. Am I returning too early?

```python
return True
```

should usually be near the end.

---

### 4. Am I testing return values?

```python
True / False
```

not:

```python
"valid" / "invalid"
```

---

### 5. Did I write pseudocode first?

If not:

```text
Stop coding.

Write the algorithm in English.
```

---

# Week 5 Personal Focus Going Forward

## Continue Improving

* Algorithm design
* Pseudocode writing
* Edge-case thinking
* Unit testing

## Reduce

* Returning too early
* Missing parentheses
* Forgetting string reassignment
* Mixing printed output with return values

---

# One-Line Reminder

> If stuck: Stop writing Python. Explain the solution in English first.
