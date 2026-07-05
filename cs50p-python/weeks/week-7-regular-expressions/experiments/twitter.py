import re

url = input("URL: ").strip()

# Extract the alphanumeric username from a strict Twitter URL, ignoring case and optional www
if matches := re.search(r"^https://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")