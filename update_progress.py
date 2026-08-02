import os

# 1. Define your exact folder target
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
        if os.path.isdir(item_path) and (item.startswith("week") or "project" in item):
            completed += 1
            
    return completed

# 2. Calculate exact math
total_required = sum(SYLLABUS.values())
total_completed = 0

for course in SYLLABUS.keys():
    total_completed += count_completed_modules(course)

# Prevent going over 100% if extra test folders exist
raw_percentage = (total_completed / total_required) * 100
percentage = min(round(raw_percentage, 1), 100.0)

print(f"Total Progress: {total_completed}/{total_required} modules ({percentage}%)")

# 3. Generate the Modern SVG Graphic
# Width of the fill bar (max 400px)
fill_width = (percentage / 100) * 400

svg_content = f"""<svg width="500" height="60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Neon Blue/Cyan Gradient -->
    <linearGradient id="neonGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe"/>
      <stop offset="100%" stop-color="#4facfe"/>
    </linearGradient>
    <!-- Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Transparent Background (Blends with GitHub Dark Mode) -->
  <rect width="500" height="60" fill="transparent" />

  <!-- Track (Dark Grey) -->
  <rect x="10" y="30" width="400" height="12" rx="6" fill="#21262d" />

  <!-- Progress Fill with Gradient and Glow -->
  <rect x="10" y="30" width="{fill_width}" height="12" rx="6" fill="url(#neonGlow)" filter="url(#glow)" />

  <!-- Percentage Text -->
  <text x="425" y="41" fill="#c9d1d9" font-family="Courier New, monospace" font-size="16" font-weight="bold">{percentage}%</text>
  
  <!-- Title Text -->
  <text x="10" y="20" fill="#8b949e" font-family="Arial, sans-serif" font-size="12" font-weight="bold" letter-spacing="1">OVERALL FOUNDATION PROGRESS</text>
</svg>"""

# 4. Save the SVG file
with open("progress.svg", "w") as file:
    file.write(svg_content)

print("progress.svg generated successfully.")