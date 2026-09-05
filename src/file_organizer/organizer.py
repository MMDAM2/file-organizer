"""Used by `main.py`"""

import logging as log
from pathlib import Path  # `os.path` is stupid, let's use pathlib instead
from shutil import move  # For moving the files

from .categories import EXTENSIONS

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


def find_files(path: Path) -> list[tuple[Path, Path]]:
    """Find all organizable files in `path` paired with their destination folder.

    Args:
        path (Path): Directory to scan

    Returns:
        list[tuple[Path, Path]]: (file, destination_folder) pairs
    """
    files: list[tuple[Path, Path]] = []  # Initialize a empty list

    # Iterate over each item in the given directory
    for item in path.iterdir():
        # If the item is not a file, skip it
        if not item.is_file():
            continue

        # If the same category exists in parent directory
        # skip it
        if item.parent.name in EXTENSIONS.values():
            continue

        # Get the category name for the current item
        category = EXTENSIONS.get(item.suffix.lower(), "Other")

        # Include the item in the list
        files.append((item, path / category))

    # Return the resulting list
    return files


def organizer(
    path: str | Path,
) -> tuple[int, int, int, bool]:
    """Organizes the given folder based on the filename's suffix (extension)

    Args:
        path (str | Path): Give a Path or a string depending on the usage

    Returns:
        `tuple[int, int, int, bool]`:
        Returns the total amount processed, moved files, failed files, and the success status
    """
    # __file__ is the script's directory
    folder: Path = Path(path).expanduser().resolve()

    # Check if the folder doesn't exist or isn't actually a directory (e.g. a file was given)
    # `is_dir()` covers both cases in one check, since it's False for both
    if not folder.is_dir():
        logger.debug(msg="Folder doesn't exist or isn't a directory, terminating...")
        return 0, 0, 0, False

    # Get the (file, destination) pairs from the shared finder function
    # This is the same logic `preview()` uses, so both stay in sync
    pairs: list[tuple[Path, Path]] = find_files(path=folder)

    # Total is just however many files were found and paired up
    total: int = len(pairs)

    # Initialize the amount of successfully moved files
    # and the amount that failed to move
    moved: int = 0
    failed: int = 0

    # Go through each (file, destination) pair and actually perform the move
    for item, destination in pairs:
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
        # Catch any OS-level failure (permission denied, file locked, etc.)
        # so one bad file doesn't crash the whole batch
        try:
            move(src=item, dst=item_location)  # shutil.move(item, item_location)
        except OSError as e:
            logger.error("An unexpected error happened: %s", e)
            failed += 1
            continue
        logger.info("Moved %s -> %s", item, item_location)

        # Now it's one moved file and processed after one iteration
        moved += 1

    # If no files were processed in the given directory
    # log it...
    if total == 0:
        logger.debug("No file has been moved.")

    # Success only if nothing failed along the way
    success: bool = failed == 0

    # Return and deconstruct in the main program
    return total, moved, failed, success


def preview(input_path: str) -> tuple[list[tuple[str, Path]], bool]:
    """Take a Preview of the following changes

    Args:
        input_path (str): The user given path

    Returns:
        `list[tuple[str, Path]]`: a Preview of the whole operation
    """
    path: Path = Path(input_path).expanduser().resolve()

    if not path.is_dir():
        return [], False
    pairs = find_files(path)
    # Return the list
    return [(item.name, dest) for item, dest in pairs], True
