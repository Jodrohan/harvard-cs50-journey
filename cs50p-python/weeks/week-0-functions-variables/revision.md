# 🚨 Week 0: Revision & "Gotchas"

## 1. The `check50` Robot Traps
* **The Silence Rule:** If an assignment (like `indoor.py` or `playback.py`) wants raw input, NEVER put text in the `input()` prompt. `input("Enter string: ")` will crash the grader. Use `input()` instead.
* **Exact String Matches:** If the assignment asks for `m: `, give it exactly `input("m: ")` with the space.
* **No Formatting Clutter:** If it expects an integer output, just use `print(E)`. Do not add words like `print(f"Energy = {E}")`.

## 2. Math & Logic Mistakes
* **The Modulo Trap:** `%` finds the remainder of a division (e.g., `15 % 50`). It does **NOT** calculate a percentage. To find 15%, divide by 100 to get a decimal (`0.15`) and multiply.
* **Overwriting Variables (Shadowing):** Don't use the same name for different states of data. 
    * *Bad:* `tip = percent_to_float(...)` then `tip = tip * meal`
    * *Good:* Use `percent` for the decimal and `tip` for the final dollar amount.

## 3. Function Architecture
* **Soundproof Rooms:** Functions cannot see each other's variables. `main()` cannot see variables created in helper functions, and helper functions cannot see `meal_cost`. You **MUST** pass data through arguments.
* **The Envelope (`return`):** `return` mails the final calculation back to `main()`. If you write an empty `return()`, you are mailing an empty envelope and the data is lost.
* **Flat Scripts vs. Functions:** For programs with specific instructions (like `faces.py` and `tip.py`), never dump all the logic into one block. Build a manager (`main()`) and build dedicated tools (helper functions).