# Week 1: Conditionals

Conditionals allow programs to make decisions and branch execution based on Boolean logic (`True` or `False`).

## 🛠️ Operators
* **Comparison:** `>`, `<`, `>=`, `<=`, `==` (Equal), `!=` (Not equal)
* **Logical:** * `and`: BOTH conditions must be True.
  * `or`: ONLY ONE condition needs to be True.
* **Math (Crucial for Logic):** `%` (Modulo) calculates the remainder of a division. Used often to check if a number is even (`n % 2 == 0`) or to evaluate parity.

## 🔀 Control Flow
* **`if`:** Python checks every `if` statement independently. This can be slow or lead to unintended bugs if choices are mutually exclusive.
* **`elif` (Else If):** Links conditions into a sequential chain. Python stops checking the moment it hits the *first* `True` condition, making the execution highly efficient.
* **`else`:** The absolute catch-all. Requires no condition. It runs only if every condition above it evaluated to `False`.
*(See `experiments/compare.py` & `experiments/grade.py`)*

## 🗂️ Match Statements (Python 3.10+)
A cleaner alternative to massive `elif` chains when checking a single variable against many specific, discrete values.
* **`case "X":`** Checks if the variable matches "X".
* **`|` (Pipe):** Acts as an inline `or` statement within cases (e.g., `case "A" | "B":`).
* **`case _:`** The wildcard/catch-all character (behaves exactly like `else`).
*(See `experiments/house.py`)*

## ⚖️ Boolean Logic & Parity
Instead of using bulky `if/else` blocks to explicitly return `True` or `False`, you can directly return the evaluation result of a comparison expression. This is the clean, idiomatic "Pythonic" way to handle boolean flags.

```python
# Bulky Architecture
if n % 2 == 0:
    return True
else:
    return False

# Clean, Pythonic Architecture
return n % 2 == 0

## 🏆 Assignment Playbook (The "Gotchas")

* 🧹 **Clean Inputs Fast (`deep`, `bank`)**
  * Never trust user typing. Fix spacing and casing *before* your logic.
  * `text = input().strip().lower()` 

* 🎯 **Target Specific Words (`bank`, `extensions`)**
  * `.startswith("hello")` ➡️ Safely check the front of a string.
  * `.endswith(".gif")` ➡️ Safely check the back (perfect for file types).

* ✂️ **The 3-Way Split (`interpreter`)**
  * Extract multiple variables from one input instantly.
  * `x, y, z = text.split(" ")`

* 🛑 **The Type Trap (`interpreter`, `meal`)**
  * **Strings** are for scissors (`.split()`).
  * **Floats/Ints** are for math (`+`, `-`).
  * *Rule:* Split the text first, then force it into a number (`float()`) *before* you calculate.

* 🛡️ **The `check50` Bouncer (`meal`)**
  * If you build custom functions alongside `main()`, put this at the very bottom:
  * `if __name__ == "__main__": main()`
  * *Why?* It acts as a shield. It lets the grading bot quietly test your helper tools without accidentally triggering your whole game.