import os
import json
import re

def sanitize_filename(filename):
    # Replace special characters with underscores, keep alphanumeric and dots
    return re.sub(r'[^\w.]', '_', filename)

tutorials_dir = "tutorials"
tutorials = []

# Ensure tutorials directory exists
if not os.path.exists(tutorials_dir):
    print(f"Directory {tutorials_dir} not found, creating it")
    os.makedirs(tutorials_dir)

for filename in os.listdir(tutorials_dir):
    if filename.endswith(".mp4"):
        sanitized_name = sanitize_filename(filename)
        if sanitized_name != filename:
            try:
                os.rename(
                    os.path.join(tutorials_dir, filename),
                    os.path.join(tutorials_dir, sanitized_name)
                )
                print(f"Renamed {filename} to {sanitized_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
                continue
        tutorials.append({
            "name": sanitized_name,
            "sha": "",  # SHA will be updated by Admin App
            "title": sanitized_name.replace(".mp4", ""),
            "description": f"Tutorial video: {sanitized_name}",
            "url": f"https://github.com/aizalovv/dialogspro/raw/main/tutorials/{sanitized_name}"
        })

# Write tutorials.json
with open("tutorials.json", "w", encoding="utf-8") as f:
    json.dump(tutorials, f, indent=2)

print("Generated tutorials.json")
