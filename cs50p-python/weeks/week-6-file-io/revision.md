# Week 6 File I/O: Universal Revision Notes

## 1. Context Management
* **Concept:** The `with` statement acts as a context manager.
* **Mechanism:** It guarantees that `file.close()` is automatically called when the indentation block exits, preventing resource leaks even if the program crashes.
* **Gotcha:** Falling back to `f = open(...)` and manually calling `.close()`. If an exception occurs before `.close()` is reached, the file remains locked in memory.

## 2. CSV Parsing Robustness
* **Concept:** `csv.reader` vs. `csv.DictReader`.
* **Mechanism:** `csv.reader` returns lists (reliant on rigid index order, e.g., `row[0]`). `csv.DictReader` returns dictionaries (reliant on column names, e.g., `row["name"]`).
* **Gotcha:** Hardcoding integer indices makes the script fragile. If the CSV columns are swapped by a user in the future, `csv.reader` logic will silently parse the wrong data, whereas `csv.DictReader` adapts automatically.

## 3. Data Persistence Modes
* **Concept:** `"w"` (write) vs. `"a"` (append).
* **Mechanism:** `"w"` truncates and overwrites the entire file from the beginning. `"a"` places the file pointer at the absolute end of the file to preserve existing data.
* **Gotcha:** Using `"w"` mode in a continuous logging script. It will wipe all historical data every time the script is executed.

## 4. Writing Dictionaries to CSV
* **Mechanism:** `csv.DictWriter` requires a `fieldnames` parameter to know exactly what order to write the dictionary keys into the CSV columns.
* **Gotcha:** Failing to pass `newline=""` to the `open()` function when writing CSV files. Omitting this causes operating systems like Windows to inject unintended blank rows between every entry.

## 5. Sorting Complex Data
* **Concept:** Sorting lists of dictionaries using the `key` parameter in `sorted()`.
* **Mechanism:** Python cannot natively sort a dictionary by comparing it to another dictionary. You must pass a function to the `key` parameter, often an anonymous `lambda` function (e.g., `sorted(students, key=lambda student: student["name"])`), telling Python exactly which value to use for comparison.
* **Gotcha:** Confusing `sorted(list)` with `list.sort()`. `sorted()` returns a brand new sorted list, leaving the original intact. `list.sort()` modifies the existing list in place.

## 6. Binary File I/O
* **Concept:** Handling non-text files (e.g., images, PDFs) using libraries like `PIL` (Pillow).
* **Mechanism:** Text files map bytes to characters via encodings (like UTF-8). Binary files contain raw byte data. They require binary modes: `"rb"` (read binary) and `"wb"` (write binary).
* **Gotcha:** Attempting to open a `.gif` or `.jpg` using standard `"r"` mode. This will immediately throw a `UnicodeDecodeError` because the program tries to decode raw image pixels as text characters.