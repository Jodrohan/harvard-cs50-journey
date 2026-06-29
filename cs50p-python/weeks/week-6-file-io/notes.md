# Week 6: File I/O

## Core Idea

Programs normally store data in **RAM (volatile memory)**, which is erased when the program ends.

**File I/O** allows programs to save and retrieve data from **disk (non-volatile memory)**, making information persist between runs.

---

# 1. Reading & Writing Files

Use `open()` to access files.

Always prefer the **context manager** (`with`) because it automatically closes the file.

```python
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
```

## File Modes

|  Mode | Purpose                                                   |
| :---: | --------------------------------------------------------- |
| `"r"` | Read (default)                                            |
| `"w"` | Write (overwrites existing content or creates a new file) |
| `"a"` | Append (adds data to the end of the file)                 |
| `"x"` | Create a new file (raises an error if it already exists)  |

### Why use `with`?

* Automatically closes the file.
* Prevents resource leaks.
* Cleaner and safer than calling `close()` manually.

---

# 2. Reading Text Files

```python
with open("names.txt") as file:
    for line in file:
        print(line.rstrip())
```

### `rstrip()`

Removes the trailing newline (`\n`) from each line before printing.

Without `rstrip()`:

```text
Harry

Ron

Hermione
```

With `rstrip()`:

```text
Harry
Ron
Hermione
```

---

# 3. CSV Files

A **CSV (Comma-Separated Values)** file stores tabular data.

Example:

```csv
name,house
Harry,Gryffindor
Hermione,Gryffindor
Ron,Gryffindor
```

CSV files are ideal for storing multiple attributes for each record.

---

# 4. Parsing CSV Manually

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")

        students.append({
            "name": name,
            "house": house
        })
```

Each row becomes a dictionary.

Result:

```python
[
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"}
]
```

---

# 5. Sorting Data

```python
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
```

## Lambda Function

A **lambda** is a small anonymous function.

```python
lambda student: student["name"]
```

Equivalent to:

```python
def get_name(student):
    return student["name"]
```

Used when a function is needed only once.

---

# 6. Why Manual `.split(",")` Isn't Reliable

Manual parsing fails when data contains commas.

Example:

```text
Washington, D.C.
```

Using `.split(",")` produces:

```python
["Washington", " D.C."]
```

This can result in incorrect parsing or a `ValueError`.

Other issues include:

* Quoted strings
* Embedded commas
* Escaped characters

---

# 7. Using the `csv` Module

Python's built-in `csv` module safely handles CSV files.

## Reading CSV Files

```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "home": row["home"]
        })
```

### `DictReader`

* Uses the first row as column headers.
* Converts each row into a dictionary.
* Correctly handles commas and quoted values.

Example:

```csv
name,home
Harry,Surrey
Hermione,London
```

Becomes:

```python
{
    "name": "Harry",
    "home": "Surrey"
}
```

---

## Writing CSV Files

```python
import csv

name = input("Name: ")
home = input("Home: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])

    writer.writerow({
        "name": name,
        "home": home
    })
```

### `DictWriter`

* Writes dictionaries directly into a CSV file.
* Uses column names (`fieldnames`) instead of manually formatting strings.
* Produces cleaner and more reliable CSV output.

---

# 8. Binary Files

Not every file stores text.

Examples include:

* Images
* Videos
* Audio
* PDFs

These files store **binary data (bytes)** instead of characters, so opening them in a text editor displays unreadable data.

---

# 9. Pillow (PIL)

**Pillow** is the modern implementation of the **Python Imaging Library (PIL)**.

Install:

```bash
pip install pillow
```

Example:

```python
from PIL import Image

image = Image.open("cat.jpg")
image.show()
```

Common operations:

* Open images
* Resize
* Crop
* Rotate
* Merge
* Apply filters
* Save in different formats

---

# Key Takeaways

* RAM is temporary; files provide permanent storage.
* Use `with open()` for safe file handling.
* Understand the file modes: `r`, `w`, `a`, and `x`.
* Use `.rstrip()` when reading text files.
* CSV files organize structured data.
* Store CSV rows as dictionaries.
* Use `lambda` for short, one-time functions.
* Prefer `csv.DictReader()` over manual `.split(",")`.
* Use `csv.DictWriter()` to write CSV files safely.
* Binary files require specialized libraries.
* Pillow is Python's standard library for image processing.
