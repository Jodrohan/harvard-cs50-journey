# Reflection

## What I learned
* Utilizing the Python `re` module to implement anchors, character classes, quantifiers, grouping, and flags.
* Applying the walrus operator (`:=`) for efficient pattern matching and variable assignment.
* Utilizing raw strings (`r""`) to prevent escape character conflicts in complex regex patterns.
* Discarding unstaged workspace modifications using `git restore`.
* Structuring atomic commits to isolate distinct logical scripts (`validate.py`, `format.py`, `twitter.py`).
* Establishing upstream tracking links for new branches using `git push --set-upstream`.
* Bypassing web GUIs by executing fast-forward merges directly from the command-line interface.

## What confused me
* Transitioning from standard Python string manipulation methods to complex regular expression syntax.
* The structural difference between native local Git merges and proprietary GitHub Pull Requests.
* The error encountered when pushing a branch that only exists locally.

## Mistakes I made
* Initially including overly verbose comments rather than writing clean, self-documenting code.
* Staging multiple unrelated feature scripts together instead of adhering to the atomic commit standard.
* Attempting to push to a remote repository without first paving the tracking connection.

## Next action
* Execute `git branch -d feat-week7-regex` to delete the obsolete local feature branch and maintain a clean repository environment.
* Implement Python 3.11+ security features and strict regex boundaries in future string parsing tasks.
