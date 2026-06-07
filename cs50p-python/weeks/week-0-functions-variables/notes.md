# 🚀 CS50P Week 0: Functions and Variables 

## 🧠 1. The Core Philosophy of Python
* **The Flow:** All programming follows a strict sequence: **Input → Process → Output**.
* **Top-to-Bottom:** Python executes code from top to bottom.
* **Inside-Out Execution:** When Python encounters nested functions like `dollars_to_float(input("Cost: "))`, it evaluates from the inside out. It will pause to resolve the `input()` first, and *then* throw that resulting string into the outer function.

---

## 📦 2. Variables and Data Types
Variables store data, but you must strictly manage *what kind* of data they hold.
* **`input()` is ALWAYS a String:** No matter what the user types (even a number like `50`), `input()` captures it as text (`str`).
* **No Math on Strings:** You cannot multiply or divide a string. You must cast it to a number first.
* **`int()`:** Converts text into a mathematical integer (whole numbers only).
* **`float()`:** Converts text into a decimal number. This is **mandatory** when handling currency or percentages.

---

## ✂️ 3. String Manipulation Methods
Methods to clean and format text before processing it.
* **`.lower()` / `.capitalize()` / `.title()`**: Changes text casing. 
* **`.split(" ")`**: Breaks a single string into multiple parts based on a separator (e.g., splitting a first and last name).
* **`.replace("old", "new")`**: Swaps specific characters. 
    * *Pro-Tip:* Highly useful for stripping unwanted mathematical symbols before float conversion (e.g., `meal = meal.replace("$", "")`).
* **`.strip()`**: Removes accidental whitespace (spaces, tabs, newlines) from the left and right sides of a user's input.

---

## 🧮 4. Math and Number Formatting
* **The Modulo Trap (`%`):** In Python, `%` is the **modulo operator**, which calculates the *remainder* of a division. It does **not** calculate percentages.
    * *Correct Percentage Math:* Divide the percentage by 100 to get a decimal, then multiply. Example: `(tip / 100) * meal_cost`.
* **F-Strings:** Allows variables to be injected directly into text strings: `f"Hello, {name}"`.
* **Currency Formatting (`:.2f`):** Forces Python to display exactly two digits after the decimal point. This prevents outputs like `$7.5` and forces it to display cleanly as `$7.50`.
* **Comma Formatting (`:,`):** Adds commas to large numbers (e.g., `1,000`).

---

## 🛠️ 5. Advanced Built-in Functions
* **`round(number, digits)`**: Mathematically rounds a floating-point number to the specified number of decimal places.
* **`print()` parameters**: By default, `print()` has hidden behaviors you can override.
    * `end=""`: Overrides the default behavior of adding a hidden newline (`\n`) at the end, allowing you to print on the same line.
    * `sep=""`: Overrides the default space inserted when printing multiple arguments.

---

## 🏗️ 6. Functions (`def`) and Architecture
Large programs must be broken into smaller, focused tasks to be understandable and debuggable.
* **The Manager (`main()`):** `main()` controls the program flow. It gathers the input, hands it to helper functions, receives the clean data back, and executes final calculations and outputs.
* **The Tools (Helper Functions):** Custom functions take arguments, process them, and return results. 
* **Default Parameters:** You can assign a fallback value in a function definition (e.g., `def hello(to="world"):`) if no argument is provided by the user.
* **`print()` vs. `return`:** * `print()` just displays text to the human screen.
    * `return` acts as an envelope. It seals up the calculated value and actually mails it back to the computer/manager (`main()`). *Note: `return` is a statement, so parentheses are not needed (`return d`, not `return(d)`).*

---

## ⚠️ 7. The "Gotchas" (Critical Mechanics)

### A. Variable Scope ("Soundproof Rooms")
Functions do not share variables. A variable created inside `main()` (like `meal_cost`) is completely invisible to helper functions. 
* You **must** pass data into functions via parameters/arguments (e.g., `def dollars_to_float(d):`).

### B. The `check50` Robot
`check50` is a rigid, cloud-based automated grading robot. 
* **Exact Matches:** It will instantly fail your code for a single extra space, a typo in a prompt, or a differently named function.
* **The Silence Trap:** If an assignment (like `indoor.py`) expects raw input, **do not** include prompt text. Use `x = input()` instead of `x = input("Enter text: ")` or the robot will crash.

### C. Git Workflow (Atomic Commits)
* Never dump all fixes into one massive commit. 
* A repository is a professional timeline of logical changes. Practice **atomic commits**: one logical fix = one commit (e.g., `git commit -m "Fix check50 formatting in indoor.py"`).