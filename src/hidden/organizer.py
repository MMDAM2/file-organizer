import shutil
from pathlib import Path
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


def organizer(dir: str, event: object = None) -> bool:
    # __file__ is the script's directory
    folder: Path = Path(dir).expanduser().resolve()

    total: int = 0
    moved: int = 0

    files: list[Path] = []

    for item in folder.iterdir():
        if item.is_file:
            files.append(item)

    for item in files:
        if any(parent.name in EXTENSIONS for parent in item.parents):
            continue

        total += 1

        category = EXTENSIONS.get(item.suffix.lower(), "Other")

        destination = folder / category
        destination.mkdir(exist_ok=True)

        new_location = destination / item.name

        counter: int = 1

        while new_location.exists():
            new_name = f"{item.stem} ({counter}){item.suffix}"
            new_location = folder / new_name
            print(f"Renamed {item.name} to {new_name}")
            counter += 1

        _ = shutil.move(item, new_location)
        print(f"Moved {item.name} to {new_location}")
        moved += 1

    return True


folder = Path(__file__).expanduser().parent

organizer(str(folder))
