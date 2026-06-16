# Week 4: Libraries — Revision Notes

## Core Theme

Week 4 is about using other people's code (libraries/APIs) while maintaining control over:

* Input validation
* Program flow
* Exceptions
* Functions
* Command-line arguments
* Data from external sources

**Rule:** Let libraries solve specialized problems. Your job is orchestration and validation.

---

# 1. Third-Party Libraries

Install:

```bash
pip install emoji
pip install pyfiglet
pip install inflect
pip install requests
```

Examples:

```python
emoji.emojize(text, language="alias")
```

```python
p = inflect.engine()
p.join(names)
```

```python
figlet = Figlet()
figlet.getFonts()
figlet.setFont(font="slant")
```

### Lessons

* Don't reinvent existing library functionality.
* Read documentation carefully.
* Parameters often contain the real power of a function.
* Never shadow imported modules:

```python
import emoji
emoji = input()   # BAD
```

---

# 2. Command-Line Arguments (`sys.argv`)

```bash
python bitcoin.py 2
```

Creates:

```python
["bitcoin.py", "2"]
```

Rules:

```python
sys.argv[0]  # filename
sys.argv[1]  # first argument
```

Validate early:

```python
if len(sys.argv) != 2:
    sys.exit("Missing argument")
```

**Fail Fast:** Validate before running program logic.

---

# 3. Input Validation

`input()` always returns a string.

```python
n = int(input())
price = float(input())
```

Every conversion can fail:

```python
try:
    n = int(input())
except ValueError:
    pass
```

---

# 4. Exception Handling

Structure:

```python
try:
    ...
except ValueError:
    ...
else:
    ...
```

* `try` → risky code
* `except` → error path
* `else` → success path

### EOFError

`Ctrl + D` raises:

```python
EOFError
```

Useful for ending infinite input loops.

---

# 5. Loop Control

### break

Exits current loop only.

```python
break
```

### continue

Restarts current iteration.

```python
if guess <= 0:
    continue
```

### for...else

```python
for _ in range(3):
    if correct:
        break
else:
    print("Out of attempts")
```

`else` runs only if no `break` occurs.

### Design Principle

Avoid unnecessary nested loops. Separate program phases when possible.

---

# 6. Function Design

### Single Responsibility

Functions should do one job.

```python
def generate_integer(level):
    return number
```

### Trust Parameters

Bad:

```python
def generate_integer(level):
    level = get_level()
```

Use the value passed into the function.

### main() Controls Flow

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

---

# 7. Variables & Scope

Prefer local variables:

```python
def main():
    names = []
```

over globals:

```python
names = []
```

### Save Important Values

Bad:

```python
print(f"{x + y}")
```

Good:

```python
answer = x + y
```

Compute once, reuse many times.

---

# 8. Common Logic Traps

### Boolean Trap

Bad:

```python
if n != 1 or n != 2 or n != 3:
```

Good:

```python
if n not in [1, 2, 3]:
```

### UnboundLocalError

Don't return variables that may never have been created.

### Off-By-One

```python
range(1, 10)
```

Produces:

```text
1 2 3 4 5 6 7 8 9
```

Upper bound excluded.

### Expression Trap

```python
guess == answer
```

Produces a value but performs no action.

---

# 9. APIs & JSON

Download data:

```python
response = requests.get(URL)
data = response.json()
```

JSON often contains nested dictionaries:

```python
data["bpi"]["USD"]["rate_float"]
```

Access one layer at a time.

---

# 10. Output Formatting

Currency formatting:

```python
f"${amount:,.4f}"
```

* `,` → thousands separators
* `.4f` → 4 decimal places

Example:

```text
$68,240.9000
```

### check50 Rule

Output must match exactly:

* spacing
* capitalization
* punctuation
* formatting

Remove all debug prints before submission.

---

# Week 4 Assignment Takeaways

### Emojize

* Use `emoji.emojize()`
* `language="alias"` enables common emoji aliases

### Figlet

* `sys.argv` validation
* `sys.exit()` for invalid flags
* `Figlet()` object, `getFonts()`, `setFont()`

### Adieu, Adieu

* `inflect.engine()`
* `p.join()` for Oxford-comma lists
* `EOFError` as loop termination

### Guessing Game

* Input validation
* `continue`
* `try/except/else`
* Loop architecture

### Little Professor

* Function responsibility
* `for...else`
* Algorithmic thinking (`10 ** level`)
* Retry-loop design

### Bitcoin Price Index

* `sys.argv`
* `requests`
* JSON navigation
* Numeric formatting
* Exact output requirements
