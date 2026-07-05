import re

name = input("What's your name? ").strip()

# Reformat "Last, First" inputs into standard "First Last" order
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")