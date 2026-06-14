# 🚨 Revision Log: Week 3 Exceptions — Fuel Gauge

## 1. Architectural Lesson: The Blast Shield (`try` / `except` / `else`)
* **The Mistake:** Placing non-dangerous code outside the `try:` block, or placing `break` in a way that escapes the loop prematurely regardless of success.
* **The Lesson:** * A `try:` block is a controlled experiment. Only the code that **can** fail belongs inside it. 
    * The `else:` block is strictly for the "happy path" (successful execution). 
    * `break` belongs inside the `else:` block to ensure the loop only terminates once data is validated and processed.

## 2. Type Contradiction: Scissors vs. Integers
* **The Mistake:** Attempting to run `.split()` on an invalid separator or trying to convert a raw string containing non-numeric characters (like "4/2") directly to `int()`.
* **The Lesson:** Data processing must happen in distinct stages:
    1. **Clean:** Sanitize the raw input (e.g., `.strip()`).
    2. **Chop:** Use the correct "scissors" (`.split("/")`).
    3. **Convert:** Cast to numeric types (`int()`) only **after** the string is successfully unpacked.

## 3. The "Empty Scissors" Fallacy
* **The Mistake:** Assuming `.split("/")` would return three variables (`x`, `operator`, `y`) when it only returns two.
* **The Lesson:** When you cut a string at a character, that character is consumed by the "scissors." Cutting `"3/4"` at the `/` leaves you with exactly two pieces, not three. Always match your variable unpacking to the exact number of pieces produced by the split.