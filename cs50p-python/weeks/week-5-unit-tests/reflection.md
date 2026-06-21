# Reflection

## What I learned

This week taught me that testing is not just about checking if code works; it is about proving that code works under different conditions. I learned how to use `pytest`, write unit tests, and think about edge cases such as uppercase letters, spaces, numbers, and symbols.

I also learned the importance of designing functions that return values instead of printing directly. This made it possible to test logic independently from user interaction.

Another major lesson was learning to break problems into smaller pieces using pseudocode before writing Python code.

---

## What confused me

The biggest challenge was understanding validation logic and deciding where `return True` should go. I often wanted to return too early before all conditions had been checked.

I also struggled with tracking state in loops, especially in the Vanity Plates problem where I had to remember when numbers started appearing and enforce multiple rules at the same time.

Understanding that string methods like `.lower()`, `.strip()`, and `.replace()` return new strings instead of modifying existing ones was another point of confusion.

---

## Mistakes I made

* Forgot parentheses when calling methods such as `.isalpha()` and `.isdigit()`.
* Returned values too early before all validation rules were checked.
* Forgot to save the results of string methods back into variables.
* Mixed up printed output with function return values while writing tests.
* Tried to write Python immediately instead of first planning the algorithm in plain English.

These mistakes helped me understand Python's behavior more deeply and improved my debugging skills.

---

## Next action

For Week 6, I want to focus on improving my problem-solving process rather than memorizing syntax.

My plan is to:

1. Write pseudocode before touching the keyboard.
2. Think about edge cases before writing tests.
3. Practice designing functions that are easy to test.
4. Continue documenting my learning journey on GitHub.
5. Spend more time understanding the logic behind solutions instead of rushing to code.

My goal is to become faster at turning problem statements into clear algorithms and then translating those algorithms into Python.
