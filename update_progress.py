import os
import re
import math

# 1. Exact module targets
SYLLABUS = {
    "cs50p-python": 9,       
    "cs50x-computer-science": 11,       
    "cs50-cybersecurity": 5,   
    "cs50-ai-python": 7       
}

def count_completed_modules(course_name):
    target_dir = course_name
    if os.path.exists(os.path.join(course_name, "weeks")):
        target_dir = os.path.join(course_name, "weeks")

    if not os.path.exists(target_dir):
        return 0
    
    completed = 0
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        
        # Check if it's a week/project directory
        if os.path.isdir(item_path) and (item.startswith("week") or item.startswith("project")):
            
            # THE FIX: Check if there is actual work inside the folder
            has_work = False
            for root, dirs, files in os.walk(item_path):
                # Count if we find Python files, C files, or notes (ignore hidden/git files)
                if any(f.endswith(".py") or f.endswith(".c") or f == "notes.md" for f in files):
                    has_work = True
                    break
            
            if has_work:
                completed += 1
            
    return completed

total_required = sum(SYLLABUS.values())
total_completed = 0

for course in SYLLABUS.keys():
    total_completed += count_completed_modules(course)

# Calculate percentage safely
raw_percentage = (total_completed / total_required) * 100
percentage = min(round(raw_percentage, 1), 100.0)

print(f"Total Progress: {total_completed}/{total_required} modules ({percentage}%)")

# 2. Generate the Unicode Bar
bar_length = 30
filled_length = math.floor((percentage / 100) * bar_length)
empty_length = bar_length - filled_length

bar = ('█' * filled_length) + ('░' * empty_length)
unicode_progress = f"**Journey Progress:** `[{bar}] {percentage}%`"

# 3. Inject strictly into README.md
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as file:
        readme_content = file.read()

    pattern = r"\*\*Journey Progress:\*\* `\[.*?\] .*?%`"
    
    if re.search(pattern, readme_content):
        new_readme = re.sub(pattern, unicode_progress, readme_content)
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(new_readme)
        print("README.md updated with accurate progress.")
    else:
        print("Error: Could not find the target string in README.md.")
else:
    print("Error: README.md not found.")