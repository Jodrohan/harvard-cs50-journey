# Week 1: Conditionals

Conditionals allow programs to make decisions and branch execution based on Boolean logic (`True` or `False`).

## 🛠️ Operators
* **Comparison:** `>`, `<`, `>=`, `<=`, `==` (Equal), `!=` (Not equal)
* **Logical:** * `and`: BOTH conditions must be True.
  * `or`: ONLY ONE condition needs to be True.
* **Math (Crucial for Logic):** `%` (Modulo) calculates the remainder. Used often to check if a number is even (`n % 2 == 0`).

## 🔀 Control Flow
* **`if`:** Python checks every `if` statement independently. (Slow/buggy if choices are mutually exclusive).
* **`elif` (Else If):** Links conditions into a chain. Python stops checking the moment it hits the *first* `True` condition. (Efficient).
* **`else`:** The absolute catch-all. Requires no condition. It runs if everything above it was `False`.
*(See `experiments/compare.py` & `experiments/grade.py`)*

## 🗂️ Match Statements (Python 3.10+)
A cleaner alternative to massive `elif` chains when checking a single variable against many specific values.
* **`case "X":`** Checks if the variable matches "X".
* **`|` (Pipe):** Acts as an `or` statement within cases (e.g., `case "A" | "B":`).
* **`case _:`** The wildcard/catch-all (behaves exactly like `else`).
*(See `experiments/house.py`)*

## ⚖️ Boolean Logic & Parity
Instead of using `if/else` to return `True` or `False`, you can directly return the result of a comparison. This is the "Pythonic" way.
```python
# Bulky
if n % 2 == 0:
    return True
else:
    return False

# Pythonic & Clean
return n % 2 == 0