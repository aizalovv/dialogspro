import os
import json
from datetime import datetime
import glob

# Base URL for raw GitHub content
BASE_URL = "https://raw.githubusercontent.com/aizalovv/dialogspro/main/"

def generate_json():
    videos = []
    # Find all MP4 files in tutorials/
    for file_path in glob.glob("tutorials/*.mp4"):
        filename = os.path.basename(file_path)
        video = {
            "id": filename,
            "title": filename.replace(".mp4", ""),
            "description": f"Tutorial video: {filename}",
            "url": f"{BASE_URL}tutorials/{filename}",
            "thumbnail": "",  # Add logic later if needed
            "timestamp": int(datetime.now().timestamp())
        }
        videos.append(video)

    # Write to tutorials.json
    with open("tutorials.json", "w") as f:
        json.dump(videos, f, indent=4)

if __name__ == "__main__":
    generate_json()
