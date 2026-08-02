import os
import re

# 1. Exact module targets
SYLLABUS = {
    "cs50p-python": 9,       
    "cs50x-computer-science": 11,       
    "cs50-cybersecurity": 5,   
    "cs50-ai-python": 7       
}

FILLED_CHAR = '■'
EMPTY_CHAR = '□'

def get_course_progress(course_name, total_modules):
    target_dir = course_name
    if os.path.exists(os.path.join(course_name, "weeks")):
        target_dir = os.path.join(course_name, "weeks")

    completed = 0
    if os.path.exists(target_dir):
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            
            # Check if it's a week/project directory
            if os.path.isdir(item_path) and (item.startswith("week") or item.startswith("project")):
                
                has_work = False
                for root, dirs, files in os.walk(item_path):
                    # Trigger completion when notes or code are found
                    if any(f.endswith(".py") or f.endswith(".c") or f == "notes.md" for f in files):
                        has_work = True
                        break
                
                if has_work:
                    completed += 1

    # Cap completed at total_modules to prevent overflow bugs
    completed = min(completed, total_modules)
    
    # Generate the box string for this specific course
    boxes = (FILLED_CHAR * completed) + (EMPTY_CHAR * (total_modules - completed))
    return completed, boxes

total_required = 0
total_completed = 0
course_boxes = []

for course, total in SYLLABUS.items():
    comp, boxes = get_course_progress(course, total)
    total_required += total
    total_completed += comp
    # Create bracketed box chunks per course
    course_boxes.append(f"[{boxes}]")

# Format: [■■□□□□□□□] [□□□□□□□□□□□] [□□□□□] [□□□□□□□]
combined_boxes = " ".join(course_boxes)

# Calculate percentage safely
raw_percentage = (total_completed / total_required) * 100
percentage = min(round(raw_percentage, 1), 100.0)

print(f"Total Progress: {total_completed}/{total_required} modules ({percentage}%)")

unicode_progress = f"**Journey Progress:** `{combined_boxes} {percentage}%`"

# Inject strictly into README.md
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as file:
        readme_content = file.read()

    # Regex looks for the new segmented format
    pattern = r"\*\*Journey Progress:\*\* `\[.*?\].*?%`"
    
    if re.search(pattern, readme_content):
        new_readme = re.sub(pattern, unicode_progress, readme_content)
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(new_readme)
        print("README.md updated with course-specific boxes.")
    else:
        print("Error: Could not find the target string in README.md.")
else:
    print("Error: README.md not found.")