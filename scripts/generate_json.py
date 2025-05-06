import os
import json
from datetime import datetime
import glob

BASE_URL = "https://raw.githubusercontent.com/aizalovv/dialogspro/main/"

def generate_json():
    videos = []
    for file_path in glob.glob("tutorials/*.mp4"):
        filename = os.path.basename(file_path)
        video = {
            "id": filename,
            "title": filename.replace(".mp4", ""),
            "description": f"Tutorial video: {filename}",
            "url": f"{BASE_URL}tutorials/{filename}",
            "thumbnail": "",
            "timestamp": int(datetime.now().timestamp())
        }
        videos.append(video)
    
    with open("tutorials.json", "w") as f:
        json.dump(videos, f, indent=4)

if __name__ == "__main__":
    generate_json()
