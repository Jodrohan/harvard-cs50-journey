# Reflection

## What I learned
* **Regex Fundamentals:** Utilizing the Python `re` module to implement anchors, character classes, quantifiers, grouping, and flags.
* **Syntax Optimization:** Applying the walrus operator (`:=`) for efficient pattern matching and utilizing raw strings (`r""`) to prevent escape character conflicts.
* **Ecosystem Integration:** Leveraging PyPI and third-party libraries (`validators`) instead of reinventing complex standards.
* **Git Operations:** Structuring atomic commits, discarding unstaged modifications (`git restore`), correcting history (`git commit --amend`), and establishing upstream tracking (`git push --set-upstream`).
* **Workflow:** Bypassing web GUIs for CLI fast-forward merges and integrating `black` for automated code formatting prior to committing.

## What confused me
* Transitioning from standard Python string manipulation methods to complex regular expression syntax.
* The structural difference between native local Git merges and proprietary GitHub Pull Requests.
* Git remote tracking mechanics, specifically errors encountered when pushing branches that only exist locally.

## Mistakes I made
* Initially including overly verbose comments rather than writing clean, self-documenting code.
* Staging multiple unrelated feature scripts together instead of adhering to the atomic commit standard.
* Attempting to push to a remote repository without first paving the tracking connection.
* Attempting to build complex regex for email validation manually before recognizing the efficiency of standard libraries.

## Next action
* Execute branch deletions to clear obsolete local feature branches and maintain repository hygiene.
* Implement strict regex boundaries and adopt a "search PyPI first" protocol in future Python tasks.
* Initialize the CS50P Week 8 (Object-Oriented Programming) directory structure.