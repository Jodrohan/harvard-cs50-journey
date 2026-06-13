# Week 3 — Exceptions

This week introduced a major shift in how I think about errors in programming.

Until now, whenever a program encountered an error, I mostly thought the solution was to go back and fix the code. I learned that while this is true for syntax errors, not all errors are the same.

## Syntax Errors vs Runtime Errors

A syntax error happens when Python cannot understand the structure of the code. Since the program cannot even start running, these errors must be fixed manually by reviewing and correcting the code.

Runtime errors are different. The program starts running successfully, but encounters a problem during execution. Instead of allowing the program to crash, Python provides a mechanism called **exceptions** to handle these situations gracefully.

This distinction was one of the most important lessons of the week.

---

## Exceptions

The core concept of this lecture was the use of exceptions.

Using `try` and `except`, a program can attempt an operation and respond appropriately if something goes wrong.

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("Not an integer")
```

Rather than crashing, the program can recover from mistakes and continue running.

I learned that exceptions are not about preventing every possible error beforehand. Instead, they allow us to attempt an operation and handle failure if it occurs.

---

## Common Exception Types

David introduced a few built-in exceptions, including:

### ValueError

Occurs when Python receives a value that cannot be used in the expected way.

```python
int("cat")
```

### NameError

Occurs when trying to use a variable that has not been defined.

```python
print(x)
```

This showed me that Python has different exception types for different categories of problems.

---

## else with try/except

I learned that exception handling also supports an `else` block.

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("Invalid input")
else:
    print(f"x is {x}")
```

The `else` block executes only when no exception occurs.

This helps separate successful program logic from error-handling logic, making code easier to read.

---

## Writing Better Programs

Another important idea from this week was writing programs that expect users to make mistakes.

Instead of assuming perfect input, programs should be designed to handle invalid input safely and guide users toward providing correct input.

This makes programs more robust and user-friendly.

---

## Functions and Abstraction

David continued emphasizing the importance of breaking programs into smaller functions.

Example:

```python
def main():
    x = get_int("What's x?: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
```

The `get_int()` function hides all validation logic from the rest of the program.

This demonstrated abstraction: creating reusable tools so other parts of the program do not need to worry about implementation details.

---

## pass

I learned about the `pass` keyword.

```python
except ValueError:
    pass
```

`pass` tells Python to do nothing.

In this example, the exception is ignored and the loop continues asking the user for valid input.

---

## Input Validation Loops

A useful pattern throughout the lecture was combining `while True`, `try`, and `except` to repeatedly request input until the user provides valid data.

This allows programs to recover from mistakes instead of terminating.

---

## raise (Preview)

At the end of the lecture, David briefly introduced `raise`.

Unlike previous examples where Python automatically generated exceptions, `raise` allows programmers to create exceptions themselves.

We did not explore it deeply yet, but it showed that exceptions are also a tool programmers can use intentionally.

---

## Main Takeaway

The biggest lesson from Week 3 was that good programs should not assume users will always provide correct input.

Instead of crashing when something unexpected happens, programs should anticipate mistakes, handle exceptions gracefully, and continue operating whenever possible.

This week shifted my mindset from "fixing errors after they happen" to "designing programs that can respond to errors intelligently."
