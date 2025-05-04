import os
import json
from datetime import datetime
import glob

BASE_URL = "https://raw.githubusercontent.com/aizalovv/dialogspro/main/"

def load_metadata():
    metadata = {}
    try:
        with open("tutorials/metadata.json", "r") as f:
            metadata = json.load(f)
    except FileNotFoundError:
        pass
    return metadata

def save_metadata(metadata):
    with open("tutorials/metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

def generate_json():
    metadata = load_metadata()
    videos = []
    for file_path in glob.glob("tutorials/*.mp4"):
        filename = os.path.basename(file_path)
        video_data = metadata.get(filename, {
            "title": filename.replace(".mp4", ""),
            "description": f"Tutorial video: {filename}"
        })
        video = {
            "id": filename,
            "title": video_data["title"],
            "description": video_data["description"],
            "url": f"{BASE_URL}tutorials/{filename}",
            "thumbnail": "",
            "timestamp": int(datetime.now().timestamp())
        }
        videos.append(video)
    
    with open("tutorials.json", "w") as f:
        json.dump(videos, f, indent=4)

if __name__ == "__main__":
    generate_json()
