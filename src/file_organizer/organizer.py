# organizer.py

"""Used by `main.py`"""

import logging
import shutil
from pathlib import Path

from .categories import EXTENSIONS

logging.basicConfig(
    filename="organizer.log", level=logging.DEBUG, format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


def organizer(
    path: str | Path,
) -> tuple[int, int, bool]:
    """Organizes the given folder based on the filename's suffix (extension)

    Args:
        path (str): _description_

    Returns:
        tuple[int, int, bool]: Returns the total amount processing, moved files, and the success
    """
    # __file__ is the script's directory
    folder: Path = Path(path).expanduser().resolve()
    if not folder.exists():
        logger.debug("Folder doesn't exist, terminating...")
        return 0, 0, False

    total: int = 0
    moved: int = 0

    files: list[Path] = []

    for item in folder.iterdir():
        if item.is_file():
            files.append(item)
            logger.debug("Added %s to the list", item)

    for item in files:
        if item.parent.name in EXTENSIONS.values():
            continue

        total += 1

        category: str = EXTENSIONS.get(item.suffix.lower(), "Other")
        if not item.suffix in EXTENSIONS:
            logger.debug("Unknown file extension for %s", item.suffix)

        destination: Path = folder / category

        if destination.exists():
            logger.debug("Destination already exists: %s", destination)

        destination.mkdir(exist_ok=True)

        new_location: Path = destination / item.name

        counter: int = 1

        while new_location.exists():
            new_name: str = f"{item.stem} ({counter}){item.suffix}"
            logger.debug("Renamed %s to %s for conflict prevention", item.name, new_name)
            new_location: Path = destination / new_name
            counter += 1

        shutil.move(item, new_location)
        logger.info("Moved %s -> %s", item, new_location)
        moved += 1

    return total, moved, True
