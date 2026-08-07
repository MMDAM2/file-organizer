# organizer.py

"""Used by `main.py`"""

import shutil
from pathlib import Path
from typing import Final

# Can be edited to support more files
# TODO: Add more file extensions
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


def organizer(
    dir: str, event: object = None
) -> bool:  # FIXME: fix the connection between main and organizer
    """Organizes the given folder based on the filename's suffix (extension)

    Args:
        dir (str): The given directory.
        event (object, optional): Needed for tkinter. Defaults to None.

    Returns:
        bool: Returns if the operation was successful.
    """
    # __file__ is the script's directory
    folder: Path = Path(dir).expanduser().resolve()

    total: int = 0
    moved: int = 0

    files: list[Path] = []

    for item in folder.iterdir():
        if item.is_file():
            files.append(item)

    for item in files:
        if any(parent.name in EXTENSIONS for parent in item.parents):
            continue

        total += 1

        category: str = EXTENSIONS.get(item.suffix.lower(), "Other")

        destination: Path = folder / category
        destination.mkdir(exist_ok=True)

        new_location: Path = destination / item.name

        counter: int = 1

        while new_location.exists():
            new_name: str = f"{item.stem} ({counter}){item.suffix}"
            new_location: Path = folder / new_name
            counter += 1

        _ = shutil.move(item, new_location)
        moved += 1

    return True
