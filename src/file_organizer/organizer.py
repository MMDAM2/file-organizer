"""Used by `main.py`"""

import logging as log
from pathlib import Path  # `os.path` is stupid, let's use pathlib instead
from shutil import move  # For moving the files

from file_organizer.categories import EXTENSIONS

# Make a new log directory if not exists
log_path: Path = Path(__file__).parent / "log"
log_path.mkdir(exist_ok=True)

# Logging configuration
log.basicConfig(
    filename=log_path / "organizer.log",
    level=log.DEBUG,
    format="%(levelname)s: %(message)s",
)

# Get a log file with this file's own name
logger: log.Logger = log.getLogger(name=__name__)


def organizer(
    path: str | Path,
) -> tuple[int, int, bool]:
    """Organizes the given folder based on the filename's suffix (extension)

    Args:
        path (str | Path): Give a Path or a string depending on the usage

    Returns:
        `tuple[int, int, bool]`: Returns the total amount processing, moved files, and the success status
    """
    # __file__ is the script's directory
    folder: Path = Path(path).expanduser().resolve()

    # Check if the folder doesn't exist, wait
    if not folder.exists():
        logger.debug(msg="Folder doesn't exist, terminating...")
        return 0, 0, False

    # Initialize the total amount of processed files
    # and actually moved ones
    total: int = 0
    moved: int = 0

    files: list[Path] = []

    # Doing a list comprehension is just taking a snapshot
    # Doing it outside the list is a bit slower but
    # if the user removed something inside their files
    # and the hard drive is slow af
    # This should not catch the deleted file unless
    # it was caught after the file getting added to the `files` list
    # These are all cover-ups so I can include logging
    for item in folder.iterdir():
        if item.is_file():
            files.append(item)
            logger.debug("Added %s to the list", item)

    # Check if the folder category already exist in the
    # parent directory of the directory given by user
    for item in files:
        if item.parent.name in EXTENSIONS.values():
            continue

        item_extension_lowercased: str = item.suffix.lower()
        # Add 1 as 1 processed file
        total += 1

        # Get the extension type for each file extension
        category: str = EXTENSIONS.get(
            item_extension_lowercased, "Other"
        )  # If the `EXTENSIONS` didn't contain it, give `Other` back
        if not item_extension_lowercased in EXTENSIONS:
            logger.debug("Unknown file extension for %s", item.suffix)

        # Make a new `Path` item
        ## Thank god I'm type hinting all of this
        destination: Path = folder / category

        if destination.exists():
            logger.debug("Destination already exists: %s", destination)

        # Make the destination (a.k.a, the file category of the file extension)
        # If it exists, don't give a fuck about creating a folder and continue
        destination.mkdir(exist_ok=True)

        # Change the item location
        item_location: Path = destination / item.name

        # Make a counter for duplicate files,
        # The counter will be reinitialized after every iteration
        # So no worries about making a new variable each time
        counter: int = 1

        # If the current moving file already exists at the file destination
        # Change its name
        while item_location.exists():
            new_name: str = f"{item.stem} ({counter}){item.suffix}"
            logger.debug("Renamed %s to %s for conflict prevention", item.name, new_name)
            item_location: Path = destination / new_name
            counter += 1

        # Actually move the file
        move(src=item, dst=item_location)  # shutil.move(item, item_location)
        logger.info("Moved %s -> %s", item, item_location)

        # Now it's one moved file and processed after one iteration
        moved += 1

    # If no files were processed in the given directory
    # log it...
    if total == 0:
        logger.debug("No file has been moved.")

    # Return and deconstruct in the main program
    return total, moved, True
