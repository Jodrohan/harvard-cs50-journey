# 🧩 Mastering Python Regular Expressions (re)

Regular Expressions (Regex) are a specialized mini-language used to search, validate, and extract patterns from text.

💡 **The Mental Model:** Think of regex like a highly specific search warrant. Instead of asking a detective to just find "a car," you provide a warrant for "a red car, built between 1990 and 2000, with a license plate starting with XYZ." Instead of writing dozens of complex if/else statements, regex allows you to define these strict parameters mathematically.

## 📑 Table of Contents

1. [Positional Anchors (Where to look)](#-1-positional-anchors-where-to-look)
2. [Wildcards, Sets, & Classes (What to look for)](#-2-wildcards-sets--classes-what-to-look-for)
3. [Quantifiers (How many times?)](#-3-quantifiers-how-many-times)
4. [Grouping & Extraction (Capturing Data)](#-4-grouping--extraction-capturing-data)
5. [Core Module Functions](#-5-core-module-functions)
6. [Regex Flags](#-6-regex-flags)
7. [Advanced Concepts](#-7-advanced-concepts)
8. [Real-World Examples](#-8-real-world-examples)

---

## 🟢 1. Positional Anchors (Where to look)

Think of anchors as a tether; they do not match actual text, but instead tie your search strictly to the very beginning or end of a line.

| Symbol | Meaning | Example | Matches |
|---|---|---|---|
| `^` | Start of string | `^Hello` | "Hello world" (but not "Say Hello") |
| `$` | End of string | `world$` | "Hello world" (but not "world peace") |
| `\b` | Word boundary | `\bcat\b` | "cat" (but not "category" or "tomcat") |

---

## 🟡 2. Wildcards, Sets, & Classes (What to look for)

Think of sets like a strict bouncer with a VIP list—they define the exact pool of acceptable characters allowed through a single door.

| Syntax | Meaning | Example | Matches |
|---|---|---|---|
| `.` | The Wildcard: Matches ANY character (except newline) | `c.t` | cat, cbt, c3t, c!t |
| `[abc]` | The VIP List: Matches exactly one 'a', 'b', or 'c' | `c[ao]t` | cat, cot (but not cut) |
| `[^abc]` | The Banned List: Matches anything EXCEPT 'a', 'b', 'c' | `c[^a]t` | cot, cut (but not cat) |
| `[a-z]` | The Range: Matches any lowercase letter | `[a-zA-Z]` | Any alphabet letter |

### Built-in Shortcuts

| Shortcut | Equivalent To | Meaning |
|---|---|---|
| `\d` | `[0-9]` | Any number (digit) |
| `\D` | `[^0-9]` | Anything NOT a number |
| `\w` | `[a-zA-Z0-9_]` | Word character (letters, numbers, underscore) |
| `\W` | `[^a-zA-Z0-9_]` | Non-word character (spaces, punctuation) |
| `\s` | `[ \t\n\r\f\v]` | Whitespace (space, tab, newline) |
| `\S` | `[^ \t\n\r\f\v]` | Non-whitespace character |

---

## 🟠 3. Quantifiers (How many times?)

Think of quantifiers like a multiplier dial on a machine—they sit immediately after a character or set and dictate exactly how many times it is allowed to repeat.

| Symbol | Meaning | Example | Matches |
|---|---|---|---|
| `*` | 0 or more times (optional, can repeat) | `ca*t` | ct, cat, caaat |
| `+` | 1 or more times (required, can repeat) | `ca+t` | cat, caaat (but not ct) |
| `?` | 0 or 1 time (optional, cannot repeat) | `ca?t` | ct, cat (but not caaat) |
| `{n}` | Exactly n times | `a{3}` | aaa |
| `{m,n}` | Between m and n times | `a{1,3}` | a, aa, aaa |

---

## 🔴 4. Grouping & Extraction (Capturing Data)

Think of parentheses `()` as boxes. They box off sections of your pattern to isolate parts for extraction, or to apply quantifiers to whole words at once.

| Syntax | Name | Purpose | Example |
|---|---|---|---|
| `(abc)` | Capturing Group | Saves matched data into memory, accessible via `.group(1)` | `^My name is (\w+)$` |
| `(?:abc)` | Non-Capturing Group | Groups logic without saving data (saves memory/processing) | `^(?:https)?://` |
| `a\|b` | Alternation (OR) | Matches the left OR the right | `(cat\|dog)` |

---

## 🧠 5. Core Module Functions

Now that you understand what regex patterns look like visually, here is how Python actually executes them. You must `import re` to use these tools.

- **`re.search(pattern, string, flags=0)`**: Scans through a string looking for the first location where the regex pattern produces a match. Returns a Match object if found, or `None` if not.
- **`re.match(pattern, string, flags=0)`**: Checks for a match only at the absolute beginning of the string. (Note: `re.search` with a `^` is generally preferred).
- **`re.fullmatch(pattern, string, flags=0)`**: Requires the entire string to match the pattern exactly.
- **`re.sub(pattern, repl, string, count=0, flags=0)`**: Finds occurrences of the pattern and replaces them with the `repl` string.
- **`re.findall(pattern, string, flags=0)`**: Returns all non-overlapping matches of the pattern in the string as a list.
- **`re.split(pattern, string, maxsplit=0, flags=0)`**: Splits the string by the occurrences of the pattern.

---

## 🚩 6. Regex Flags

Flags modify how the regex engine interprets the pattern. They are passed as the third argument in functions like `re.search()`.

- **`re.IGNORECASE`** (or `re.I`): Makes the pattern case-insensitive (e.g., `A` matches `a`).
- **`re.MULTILINE`** (or `re.M`): Allows `^` and `$` to match the start and end of each line within a multi-line string.
- **`re.DOTALL`** (or `re.S`): Configures the `.` (dot) character to match any character at all, including the newline character (`\n`).

---

## 🚀 7. Advanced Concepts

### The Walrus Operator (`:=`)

Introduced in Python 3.8, the assignment expression (`:=`) assigns a value to a variable and evaluates it within a single line. It is highly idiomatic when used with `re.search` to combine the search and the `if` logic.

```python
# Standard way
matches = re.search(r"^https://twitter\.com/(.+)$", url)
if matches:
    print(matches.group(1))

# Walrus Operator way
if matches := re.search(r"^https://twitter\.com/(.+)$", url):
    print(matches.group(1))
```

### Modern Security Updates (Python 3.11+)

Normal quantifiers (`*`, `+`) are "greedy". If a match fails later in the string, the engine will "backtrack" (re-evaluate previous characters). On massive files or malicious inputs, this backtracking can cause catastrophic performance slowdowns known as **ReDoS** (Regular Expression Denial of Service).

To solve this, Python 3.11 introduced:

- **Possessive Quantifiers** (`*+`, `++`, `?+`)
- **Atomic Grouping** (`(?>...)`)

These force the engine to grab characters and NEVER give them back to retry a match. If the match fails, it fails instantly without backtracking.

---

## 💻 8. Real-World Examples

### 1. Data Reformatting (`format.py`)

Reformatting a user's input from "Last, First" to "First Last".

```python
import re

name = input("What's your name? ").strip()

# Capture the last name in group 1, and the first name in group 2
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
```

### 2. Validation (`validate.py`)

Ensuring a user provides a properly formatted `.com` email address.

```python
import re

email = input("What's your email? ").strip()

# Validate standard email structure, permitting one optional subdomain
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```

### 3. Data Extraction (`twitter.py`)

Isolating a username from a provided Twitter URL.

```python
import re

url = input("URL: ").strip()

# Extract the alphanumeric username from a strict URL, ignoring case and optional www
if matches := re.search(r"^https://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
```