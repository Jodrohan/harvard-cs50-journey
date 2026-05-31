# 🧠 Week 0 Reflection: Functions, Variables, and the Professional Mindset

## 1. The Shift to Structural Architecture
Before today, I wrote "flat scripts"—just dumping logic from top to bottom. By refactoring `faces.py` and building `tip.py` from scratch, I learned that professional programming requires architecture. I learned how to separate the "Manager" (`main()`) from the "Tools" (custom helper functions). 

## 2. The "Soundproof Room" Realization
The biggest roadblock I hit was variable scope. I initially tried to access variables like `meal_cost` directly inside my helper functions and crashed my program. I had a major lightbulb moment: functions are like soundproof rooms. They cannot see outside variables. You must explicitly pass data in via arguments, and explicitly pass data out using `return`. I also realized that Python reads nested functions from the inside out (e.g., pausing to get `input()` before running the conversion).

## 3. The `check50` Discipline
The automated grader is brutal, but it taught me precision. I learned that a single extra space, a slightly modified string (like `Enter mass:` instead of `m:`), or an unexpected formatting comma will completely fail a test case. In cybersecurity and programming, precision is not optional; it is mandatory.

## 4. Professional Version Control
I stopped using the "shotgun approach" (`git add .`) as a crutch for my code. Today, I transitioned to a professional Git workflow using atomic commits. I deliberately staged single files using the "sniper approach" (`git add <file>`) and wrote concise, imperative commit messages. My repository is no longer a messy dump of code; it is a professional, logical timeline of my progress.