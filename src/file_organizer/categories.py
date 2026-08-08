"""Category list, can be changed to support more things"""

from typing import Final

EXTENSIONS: Final[dict[str, str]] = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp3": "Music",
    ".flac": "Music",
    ".wav": "Music",
    ".m4a": "Music",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".zip": "Archives",
    ".7z": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".cpp": "Code",
    ".deb": "Packages",
    ".run": "Packages",
}
