import os
import re

# 1. Define your exact folder target (Total = 32 modules)
SYLLABUS = {
    "cs50p-python": 9,       
    "cs50x-computer-science": 11,       
    "cs50-cybersecurity": 5,   
    "cs50-ai-python": 7       
}

# 2. Count completed folders
def count_completed_modules(course_name):
    # Check if the course has a nested "weeks" directory
    target_dir = course_name
    if os.path.exists(os.path.join(course_name, "weeks")):
        target_dir = os.path.join(course_name, "weeks")

    if not os.path.exists(target_dir):
        return 0
    
    completed = 0
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
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