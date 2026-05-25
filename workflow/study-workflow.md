# Global Study Workflow

This file defines how I study, practice, document, and manage progress across this repository.

---

# Environment

System:
- CachyOS Linux
- fish shell
- VS Code
- Git + GitHub
- Terminal-first workflow

Daily workspace:

```fish
cd ~/harvard-cs50-journey
code .
```

---

# Core Workflow

For every course and every week:

```txt
Watch → Understand → Practice → Experiment → Revise → Commit
```

---

# Daily Workflow

## 1. Open Current Course

Example:

```txt
cs50p-python/weeks/week-0-functions-variables
```

---

## 2. Watch

Watch the lecture or topic section.

Focus on:
- concepts
- logic
- problem solving
- debugging process

Do not study passively.

---

## 3. Notes

Write short practical notes in:

```txt
notes.md
```

Include:
- concepts
- syntax patterns
- debugging lessons
- important observations

Do not copy lectures word-for-word.

---

## 4. Assignments

Solve official exercises inside:

```txt
assignments/
```

Rules:
- attempt independently first
- debug before searching
- prioritize understanding over speed

---

## 5. Experiments

Use:

```txt
experiments/
```

For:
- extra practice
- edge cases
- testing ideas
- debugging
- modifying assignment logic
- small utilities

Experiments are part of learning.

---

## 6. Revision

Update:

```txt
revision.md
```

Record:
- repeated mistakes
- weak concepts
- debugging lessons
- topics needing revision

---

## 7. Git Workflow

Check changes:

```fish
git status
```

Push meaningful progress:

```fish
git add .
git commit -m "clear progress message"
git push
```

Examples:

```fish
git commit -m "solve week 0 assignments"
git commit -m "add loop experiments"
git commit -m "update regex notes"
```

---

# Weekly Workflow

At the end of every week:

- review notes
- review mistakes
- clean code
- update progress.md
- push final weekly progress

Goal:
Understand the week before moving forward.

---

# Project Workflow

Create projects only when:
- the course requires it
- an experiment becomes useful
- a concept solves a real problem
- the idea connects to Python, Linux, cybersecurity, AI, or AI security

Priority:

```txt
small finished projects
>
large unfinished projects
```

---

# Productivity Rules

Focus on:
- consistency
- depth
- experimentation
- understanding
- building

Avoid:
- endless planning
- constant repo redesign
- tutorial addiction
- fake productivity
- copying blindly

---

# When Stuck

1. Read the error carefully
2. Try a smaller version
3. Debug step-by-step
4. Search only after trying
5. Record the mistake
6. Continue

Errors are part of engineering.

---

# When Bored

Do one useful small task:
- write notes
- solve one problem
- run one experiment
- fix one bug
- clean one file
- commit one improvement

Small progress still counts.

---

# Main Rule

Every study session should produce at least one of these:

- notes
- code
- experiment
- revision entry
- commit

---

# Long-Term Goal

Build strong foundations in:
- Python
- Computer Science
- Linux
- Cybersecurity
- Artificial Intelligence
- AI Security

---

# Final Reminder

This repository exists to:
- build discipline
- build technical foundations
- document progression
- become a better engineer over time

Consistency matters more than motivation.