# CS50P Week 4 — Libraries

## Overview

This week introduced one of Python's greatest strengths: **libraries**. Instead of writing everything from scratch, Python allows us to reuse code written by others through built-in modules, third-party packages, APIs, and even our own custom libraries.

---

## Modules

A **module** is a Python file containing reusable code.

### Importing Modules

Import an entire module:

```python
import random
```

Import a specific function:

```python
from random import choice
```

Example:

```python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```

Compared to:

```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```

Using `from ... import ...` allows access to a specific function without repeatedly typing the module name.

---

## The `random` Module

### `choice()`

Returns a random item from a sequence.

```python
from random import choice

coin = choice(["heads", "tails"])
```

### `randint()`

Returns a random integer within a specified range.

```python
import random

number = random.randint(1, 10)
print(number)
```

### `shuffle()`

Randomly rearranges a list.

```python
import random

cards = ["jack", "king", "queen"]

random.shuffle(cards)

for card in cards:
    print(card)
```

**Important:** `shuffle()` modifies the original list and does not return a new one.

---

## The `statistics` Module

The `statistics` module provides pre-built statistical functions.

Example:

```python
import statistics

mean = statistics.mean([100, 90])
print(mean)
```

Useful functions include:

* `mean()`
* `median()`
* `mode()`

**Practice File:** `experiments/average.py`

---

## Command-Line Arguments (`sys.argv`)

The `sys` module allows programs to receive input directly from the terminal.

Example:

```bash
python name.py David
```

Here:

```python
sys.argv[0]
```

contains the filename, while:

```python
sys.argv[1]
```

contains `"David"`.

### Initial Approach

```python
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("too few arguments")
```

### Improved Validation

```python
import sys

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is", sys.argv[1])
```

### Lesson Learned

Exception handling is useful, but simple conditional checks can often provide clearer and more precise feedback.

---

## `sys.exit()`

Terminates a program immediately.

```python
import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")
```

This keeps the program from continuing when required input is missing.

---

## List Slicing

A slice is a subset of a sequence.

```python
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
```

`sys.argv[1:]` means:

* Start at index `1`
* Continue until the end of the list

This is useful when processing multiple command-line arguments.

---

## Third-Party Packages

Beyond Python's built-in modules, developers can install packages created by the community.

Most packages are available from:

```text
https://pypi.org
```

---

## Virtual Environments

Since I use CachyOS, I learned that installing packages globally is discouraged. Instead, packages should be installed inside a virtual environment.

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate (Fish Shell)

```bash
source .venv/bin/activate.fish
```

### Save Dependencies

```bash
pip freeze > requirements.txt
```

### Benefits

* Keeps system Python clean
* Avoids dependency conflicts
* Makes projects reproducible

---

## The `cowsay` Package

My first third-party package was `cowsay`.

Example:

```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
```

I experimented with different ASCII-art characters, including the cow and the T-Rex.

**Practice File:** `say.py`

---

## APIs

API stands for **Application Programming Interface**.

APIs allow programs to communicate with external services and retrieve data over the internet.

---

## The `requests` Package

The `requests` package is used to send HTTP requests.

```python
import requests

response = requests.get(url)
```

This was my first introduction to retrieving data from external services.

---

## JSON

Many APIs return data in JSON format.

Python's `json` module can be used to format and display that data more clearly.

```python
json.dumps(response.json(), indent=2)
```

---

## iTunes API Practice

**Practice File:** `itunes.py`

```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)

print(json.dumps(response.json(), indent=2))
```

### Concepts Practiced

* HTTP requests
* API responses
* JSON formatting
* Pretty-printing data

---

## Creating Custom Libraries

The final topic was creating my own reusable modules.

**File:** `sayings.py`

```python
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")
```

### The `__name__` Variable

```python
if __name__ == "__main__":
    main()
```

This ensures that `main()` runs only when the file is executed directly and not when it is imported elsewhere.

---

## Importing My Own Module

```python
import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
```

This demonstrated that custom modules can be imported and reused just like Python's built-in libraries.

---

## Key Takeaways

* Modules allow code reuse.
* `import` and `from ... import ...` provide different ways to access module functionality.
* The `random` and `statistics` modules offer useful built-in features.
* `sys.argv` enables command-line interaction.
* `sys.exit()` provides clean program termination.
* Slicing allows working with subsets of lists.
* PyPI provides access to thousands of third-party packages.
* Virtual environments isolate project dependencies.
* APIs allow Python programs to communicate with external services.
* JSON is a common format for exchanging structured data.
* Custom modules make code reusable and maintainable.
* `if __name__ == "__main__"` is an important pattern for building reusable Python files.
