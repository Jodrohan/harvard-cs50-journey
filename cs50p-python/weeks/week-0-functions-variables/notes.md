# 🚀 CS50P Week 0: Functions and Variables 

## 🧠 1. The Core Philosophy of Python
* [cite_start]**The Flow:** All programming follows a strict sequence: **Input → Process → Output**[cite: 1125, 1230].
* [cite_start]**Top-to-Bottom:** Python executes code from top to bottom[cite: 1125].
* **Inside-Out Execution:** When Python encounters nested functions like `dollars_to_float(input("Cost: "))`, it evaluates from the inside out. [cite_start]It will pause to resolve the `input()` first, and *then* throw that resulting string into the outer function[cite: 1153].

---

## 📦 2. Variables and Data Types
[cite_start]Variables store data, but you must strictly manage *what kind* of data they hold[cite: 1125].
* [cite_start]**`input()` is ALWAYS a String:** No matter what the user types (even a number like `50`), `input()` captures it as text (`str`)[cite: 1125, 1137].
* **No Math on Strings:** You cannot multiply or divide a string. [cite_start]You must cast it to a number first[cite: 1279, 1535].
* [cite_start]**`int()`:** Converts text into a mathematical integer (whole numbers only)[cite: 1125, 1128].
* **`float()`:** Converts text into a decimal number. [cite_start]This is **mandatory** when handling currency or percentages[cite: 1125, 1129].

---

## ✂️ 3. String Manipulation Methods
Methods to clean and format text before processing it.
* [cite_start]**`.lower()` / `.capitalize()` / `.title()`**: Changes text casing[cite: 1125, 1127]. 
* [cite_start]**`.split(" ")`**: Breaks a single string into multiple parts based on a separator (e.g., splitting a first and last name)[cite: 1127].
* [cite_start]**`.replace("old", "new")`**: Swaps specific characters[cite: 1125, 1274]. 
    * [cite_start]*Pro-Tip:* Highly useful for stripping unwanted mathematical symbols before float conversion (e.g., `meal = meal.replace("$", "")`)[cite: 1275, 1294].
* [cite_start]**`.strip()`**: Removes accidental whitespace (spaces, tabs, newlines) from the left and right sides of a user's input[cite: 1221].

---

## 🧮 4. Math and Number Formatting
* **The Modulo Trap (`%`):** In Python, `%` is the **modulo operator**, which calculates the *remainder* of a division. [cite_start]It does **not** calculate percentages[cite: 1388, 1407].
    * *Correct Percentage Math:* Divide the percentage by 100 to get a decimal, then multiply. [cite_start]Example: `(tip / 100) * meal_cost`[cite: 1420].
* [cite_start]**F-Strings:** Allows variables to be injected directly into text strings: `f"Hello, {name}"`[cite: 1131, 1566].
* [cite_start]**Currency Formatting (`:.2f`):** Forces Python to display exactly two digits after the decimal point[cite: 1576]. [cite_start]This prevents outputs like `$7.5` and forces it to display cleanly as `$7.50`[cite: 1579, 1580].
* [cite_start]**Comma Formatting (`:,`):** Adds commas to large numbers (e.g., `1,000`)[cite: 1131, 1600].

---

## 🛠️ 5. Advanced Built-in Functions
* [cite_start]**`round(number, digits)`**: Mathematically rounds a floating-point number to the specified number of decimal places[cite: 1130, 1217].
* [cite_start]**`print()` parameters**: By default, `print()` has hidden behaviors you can override[cite: 1211].
    * [cite_start]`end=""`: Overrides the default behavior of adding a hidden newline (`\n`) at the end, allowing you to print on the same line[cite: 1212, 1213].
    * [cite_start]`sep=""`: Overrides the default space inserted when printing multiple arguments[cite: 1214, 1215].

---

## 🏗️ 6. Functions (`def`) and Architecture
[cite_start]Large programs must be broken into smaller, focused tasks to be understandable and debuggable[cite: 1134].
* [cite_start]**The Manager (`main()`):** `main()` controls the program flow[cite: 1135]. [cite_start]It gathers the input, hands it to helper functions, receives the clean data back, and executes final calculations and outputs[cite: 1569].
* [cite_start]**The Tools (Helper Functions):** Custom functions take arguments, process them, and return results[cite: 1308, 1569]. 
* [cite_start]**Default Parameters:** You can assign a fallback value in a function definition (e.g., `def hello(to="world"):`) if no argument is provided by the user[cite: 1135, 1219].
* [cite_start]**`print()` vs. `return`:** * `print()` just displays text to the human screen[cite: 1125, 1138].
    * `return` acts as an envelope. [cite_start]It seals up the calculated value and actually mails it back to the computer/manager (`main()`)[cite: 1125, 1138, 1553]. [cite_start]*Note: `return` is a statement, so parentheses are not needed (`return d`, not `return(d)`)*[cite: 1715].

---

## ⚠️ 7. The "Gotchas" (Critical Mechanics)

### A. Variable Scope ("Soundproof Rooms")
[cite_start]Functions do not share variables[cite: 1150]. [cite_start]A variable created inside `main()` (like `meal_cost`) is completely invisible to helper functions[cite: 1151, 1477, 1478]. 
* [cite_start]You **must** pass data into functions via parameters/arguments (e.g., `def dollars_to_float(d):`)[cite: 1506, 1508].

### B. The `check50` Robot
[cite_start]`check50` is a rigid, cloud-based automated grading robot[cite: 1628, 1649]. 
* [cite_start]**Exact Matches:** It will instantly fail your code for a single extra space, a typo in a prompt, or a differently named function[cite: 1101, 1629].
* **The Silence Trap:** If an assignment (like `indoor.py`) expects raw input, **do not** include prompt text. [cite_start]Use `x = input()` instead of `x = input("Enter text: ")` or the robot will crash[cite: 1146, 1679, 1680].

### C. Git Workflow (Atomic Commits)
* [cite_start]Never dump all fixes into one massive commit[cite: 1692]. 
* [cite_start]A repository is a professional timeline of logical changes[cite: 1693]. [cite_start]Practice **atomic commits**: one logical fix = one commit (e.g., `git commit -m "Fix check50 formatting in indoor.py"`)[cite: 1696, 1699].