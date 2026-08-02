import os
import re

# 1. Define your exact folder target (Total = 33 modules)
SYLLABUS = {
    "CS50P": 10,       
    "CS50x": 11,       
    "CS50_Cyber": 5,   
    "CS50_AI": 7       
}

# 2. Count completed folders
def count_completed_modules(course_name):
    if not os.path.exists(course_name):
        return 0
    
    completed = 0
    for item in os.listdir(course_name):
        item_path = os.path.join(course_name, item)
        # Counts folders that start with "week" or "project"
        if os.path.isdir(item_path) and (item.startswith("week") or "project" in item):
            completed += 1
            
    return completed

# 3. Calculate exact math
total_required = sum(SYLLABUS.values())
total_completed = 0

for course in SYLLABUS.keys():
    total_completed += count_completed_modules(course)

percentage = round((total_completed / total_required) * 100, 2)
print(f"Total Progress: {total_completed}/{total_required} modules ({percentage}%)")

# 4. Generate the dynamic badge URL
badge_url = f"https://img.shields.io/badge/Journey_Progress-{percentage}%25-blue"

# 5. Inject into README.md
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r") as file:
        readme_content = file.read()

    # Regex replaces the old percentage with the new one
    new_readme = re.sub(
        r"https://img\.shields\.io/badge/Journey_Progress-.*?%25-blue", 
        badge_url, 
        readme_content
    )

    with open(readme_path, "w") as file:
        file.write(new_readme)
    print("README.md updated successfully.")
else:
    print("Error: README.md not found in the current directory.")