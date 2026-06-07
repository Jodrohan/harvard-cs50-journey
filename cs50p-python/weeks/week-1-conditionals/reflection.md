# Reflection

## What I learned
I learned how to give my Python programs a brain using control flow (`if`, `elif`, `else`). I figured out how to chain logic together to make decisions, and how to safely unpack and clean user input using tools like `.split()`, `.strip()`, and `.lower()`. Most importantly, I learned how to protect my main program from automated graders using the `if __name__ == "__main__":` bouncer.

## What confused me
Figuring out how `check50` interacts with my code behind the scenes was confusing at first—specifically understanding the difference between a human running a file directly versus a robot importing a function. Also, wrapping my head around the mathematical logic to convert a time string like "7:30" into a clean decimal fraction like `7.5` took some serious problem-solving.

## Mistakes I made
The biggest trap I fell into was the "Type Contradiction." I tried to use mathematical comparisons (`<=`) on text strings, and I tried to run `.split()` on floats. I also used `int()` at one point when I should have used `float()`, which completely erased my decimals. Finally, I tried to combine my final hour and minute values using an f-string (which just squished them into text) instead of using actual mathematical addition. 

## Next action
Close out Week 1, update my GitHub repository, and dive straight into Week 2: Loops.