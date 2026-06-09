# 🔁 Week 2: Loops & Iteration (CS50P)

## 📌 Overview
[cite_start]This week marks the transition from top-to-bottom execution to cyclic execution[cite: 23]. [cite_start]This is where you will truly start applying the DRY principle (Don't Repeat Yourself)—a core tenet for any software engineer[cite: 24].

---

## 🛑 1. The `while` Loop & Loop Controls
[cite_start]Used when you want a block of code to repeat an unknown number of times until a condition is met[cite: 104].

* [cite_start]**Standard Convention:** Set a counter to 0, check if it's less than your target, and increment by 1 (`i += 1`) at the bottom of the loop[cite: 105].
* [cite_start]**The Infinite Loop Trap:** If you forget to increment your counter, the loop runs forever[cite: 106]. [cite_start]Press `Ctrl + C` in the terminal to kill it[cite: 107].
* [cite_start]**Input Validation (The "Gotcha"):** Use a `while True:` loop to force a user to give you valid input[cite: 108]. [cite_start]It will loop forever until they provide the right data, at which point you use the `break` keyword to escape the loop[cite: 109].
* **Loop Breakers (`break` vs. `continue`):**
    * [cite_start]`break`: Completely destroys the loop[cite: 142]. 
    * [cite_start]`continue`: Skips the current iteration and jumps right back to the top of the loop[cite: 142]. [cite_start]It is highly useful for ignoring bad data (like skipping a string if you only want to process numbers) without crashing the whole program[cite: 143].

## 🔄 2. The `for` Loop & Iteration
[cite_start]Used when you want to iterate over a specific list of items or a known number of times[cite: 111].

* [cite_start]**Lists:** You can iterate directly through a list: `for i in [0, 1, 2]:` [cite: 112]
* [cite_start]**The `range()` Function:** `range(n)` automatically generates a sequence of numbers from 0 up to (but not including) n[cite: 113].
* [cite_start]**The Throwaway Variable (The "Gotcha"):** If you are running a loop just to execute an action (like printing "meow") and you don't actually care about the loop's index number, use an underscore `_` instead of a variable name: `for _ in range(3):`[cite: 114]. [cite_start]This tells other developers, "I just need this to run 3 times, ignore the variable"[cite: 115].

## 🖨️ 3. Overriding `print()` Defaults
[cite_start]By default, Python's `print()` function automatically adds a newline (`\n`) at the end of whatever you print, and separates multiple items with a space[cite: 145].

* [cite_start]**`end=""`:** Using `end=""` tells Python to stay on the exact same line for the next print statement (which is how your Mario blocks print side-by-side)[cite: 146].
* [cite_start]**`sep=", "`:** Using `sep=", "` tells Python to separate your variables with a comma instead of a space[cite: 147].

## 🗂️ 4. Data Structures: Lists vs. Dictionaries
* [cite_start]**Lists (`[]`):** Ordered collections of data[cite: 116]. [cite_start]You can use the `len()` function to find the length of a list and iterate through its indices: `for i in range(len(students)):`[cite: 117].
    > **Pythonic Pro-Tip:** While you *can* iterate using `range(len())`, it is considered "un-Pythonic." Instead, iterate directly: `for student in students:`
* [cite_start]**Dictionaries (`{}`):** Data stored in Key-Value pairs[cite: 118]. [cite_start]Highly useful for associating related information (e.g., a student and their Hogwarts house)[cite: 119].
    > [cite_start]**Dictionary Iteration (The "Gotcha"):** When you write `for i in students:`, the loop only hands you the Keys (the names)[cite: 120]. [cite_start]To get the Values (the houses), you must pass that key back into the dictionary like this: `students[i]`[cite: 121].
    > **Pythonic Pro-Tip:** Use the `.items()` method to grab both at the same time: `for key, value in students.items():`
* [cite_start]**The `None` Keyword:** A special data type representing the intentional absence of a value (e.g., if a student has no assigned color)[cite: 122].

## 🧱 5. Nested Loops & Abstraction
* [cite_start]**List of Dictionaries:** You can combine structures to hold complex data[cite: 123]. [cite_start]Iterating through a list of dictionaries allows you to access specific keys for each item: `student["name"]`[cite: 124].
* [cite_start]**Nested Loops (`mario.py`):** Putting a loop inside another loop is useful for 2D spatial reasoning (like printing grids or blocks)[cite: 125]. 
* [cite_start]**Abstraction:** Instead of writing massive nested loops, you can abstract the inner logic into its own function (e.g., having a `print_square` function call a separate `print_row` function)[cite: 126].