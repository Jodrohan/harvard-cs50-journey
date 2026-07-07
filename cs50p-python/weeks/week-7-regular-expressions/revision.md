# CS50P Week 7: Regular Expressions

## Core Functions (`import re`)

| Function | Behavior |
|---|---|
| `re.search(pattern, string)` | Finds the first match anywhere in the string. Returns a Match object or `None`. |
| `re.match(pattern, string)` | Checks for a match only at the beginning of the string. |
| `re.fullmatch(pattern, string)` | Requires the pattern to match the entire string from start to finish. |
| `re.sub(pattern, repl, string)` | Replaces occurrences of the pattern in the string with the replacement string. |
| `re.findall(pattern, string)` | Returns a list of all non-overlapping matches in the string. |

## Metacharacters (Structure)

| Symbol | Meaning |
|---|---|
| `.` | Any character except a newline. |
| `^` | Start of the string. |
| `$` | End of the string. |
| `[abc]` | Matches exactly one character from the set (a, b, or c). |
| `[^abc]` | Matches exactly one character NOT in the set. |
| `a\|b` | Matches either 'a' or 'b' (Boolean OR). |
| `(...)` | Capturing group. Extracts matched sub-strings. |
| `(?:...)` | Non-capturing group. Groups logic without extracting. |

## Quantifiers (Repetition)

| Symbol | Meaning |
|---|---|
| `*` | 0 or more repetitions of the preceding item. |
| `+` | 1 or more repetitions of the preceding item. |
| `?` | 0 or 1 repetition of the preceding item (optional). |
| `{m}` | Exactly `m` repetitions. |
| `{m,n}` | Between `m` and `n` repetitions, inclusive. |

## Special Sequences (Character Classes)

| Sequence | Meaning |
|---|---|
| `\d` | Any decimal digit (0-9). |
| `\D` | Any non-digit character. |
| `\w` | Any word character (a-z, A-Z, 0-9, and underscore). |
| `\W` | Any non-word character. |
| `\s` | Any whitespace character (space, tab, newline). |
| `\S` | Any non-whitespace character. |
| `\b` | Word boundary (transition between `\w` and `\W`). |

## Common Flags

Passed as the third argument to `re` functions (e.g., `re.search(pattern, string, re.IGNORECASE)`).

| Flag | Behavior |
|---|---|
| `re.IGNORECASE` (or `re.I`) | Performs case-insensitive matching. |
| `re.MULTILINE` (or `re.M`) | Allows `^` and `$` to match the start/end of each line, not just the whole string. |
| `re.DOTALL` (or `re.S`) | Allows the `.` metacharacter to match newlines as well. |