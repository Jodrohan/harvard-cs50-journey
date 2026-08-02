import os
import re

# ==========================================
# 📝 UPDATE YOUR PROGRESS HERE
# Simply change these numbers as you finish weeks.
# ==========================================
COMPLETED = {
    "cs50p-python": 0,           # Max: 9
    "cs50x-computer-science": 0, # Max: 11
    "cs50-cybersecurity": 0,     # Max: 5
    "cs50-ai-python": 0          # Max: 7
}

# ==========================================
# ⚙️ SCRIPT LOGIC (Do not edit below this line)
# ==========================================
TOTALS = {
    "cs50p-python": 9,
    "cs50x-computer-science": 11,
    "cs50-cybersecurity": 5,
    "cs50-ai-python": 7
}

FILLED_CHAR = '■'
EMPTY_CHAR = '□'

total_required = sum(TOTALS.values())
total_completed = 0
course_boxes = []

for course, total in TOTALS.items():
    # Cap completed at the maximum just in case you type a wrong number
    comp = min(COMPLETED[course], total) 
    total_completed += comp
    
    # Generate the box string for this specific course
    boxes = (FILLED_CHAR * comp) + (EMPTY_CHAR * (total - comp))
    course_boxes.append(f"[{boxes}]")

# Format: [■■□□□□□□□] [□□□□□□□□□□□] [□□□□□] [□□□□□□□]
combined_boxes = " ".join(course_boxes)

# Calculate percentage
percentage = round((total_completed / total_required) * 100, 1)

print(f"Total Progress: {total_completed}/{total_required} modules ({percentage}%)")

unicode_progress = f"**Journey Progress:** `{combined_boxes} {percentage}%`"

# Inject strictly into README.md
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as file:
        readme_content = file.read()

    # Regex looks for the segmented format
    pattern = r"\*\*Journey Progress:\*\* `\[.*?\].*?%`"
    
    if re.search(pattern, readme_content):
        new_readme = re.sub(pattern, unicode_progress, readme_content)
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(new_readme)
        print("README.md updated successfully with manual progress.")
    else:
        print("Error: Could not find the target string in README.md.")
        print("Please ensure this exact string is in your README:")
        print("**Journey Progress:** `[□□□□□□□□□] [□□□□□□□□□□□] [□□□□□] [□□□□□□□] 0.0%`")
else:
    print("Error: README.md not found.")