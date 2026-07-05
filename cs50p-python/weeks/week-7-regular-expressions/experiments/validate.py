import re

email = input("What's your email? ").strip()

# Validate standard email structure, permitting one optional subdomain before the primary domain
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")