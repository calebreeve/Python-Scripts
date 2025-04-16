### Script to organize my downloads folder ###
### Created 4/15/2025 ###

import os
import shutil
from pathlib import path

### file types are listed here ###
### Feel free to edit to your personal preference ###

file_types = {
    "images": [
        ".apng",
        ".png",
        ".avif",
        ".jpg",
        ".jpeg",
        ".jfif",
        ".pjpeg",
        ".pjp",
        ".png"
        ".svg",
        ".webp",
        ".bmp",
    ],
    "videos": [
       ".mp4",
       ".mov",
       ".avi",
       ".wmv",
       ".avchd",
       ".webm",
       ".flv" 
    ],
    "documents": [
        ".xlsx",
        ".html",
        ".txt",
        ".ppt",
        ".odt",
        ".7z",
        ".zip",
        ".exe",
        ".py",
        ".iso",
        ".pdf",
        ".xml",
    ],
}

### list downloads folder ###
downloads_Path = os.listdir("C:\\Users\\caleb\\Downloads")

### file sorting function ###

def file_sort(file_type, base_path):
    for word in file_type:
        for kw in base_path:
            if word in kw:
                print(kw)

file_sort(file_types["images"],downloads_Path)