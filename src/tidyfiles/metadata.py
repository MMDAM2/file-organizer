"""Manage metadata for `TidyFiles`-organized directories."""

import json
from pathlib import Path
from typing import Final

# cSpell: words tidyfiles

METADATA_FILE: Final[str] = ".tidyfiles"
CREATED_BY: Final[str] = "tidyfiles"


def create_metadata(folder: Path) -> None:
    """Create the metadata file if it does not already exist."""

    metadata: dict[str, str | float | list[str]] = {
        "created_by": CREATED_BY,
        "version": 1.1,
        "categories": [],
    }

    file: Path = folder / METADATA_FILE

    if not file.exists():
        file.write_text(
            json.dumps(metadata, indent=4),
            encoding="utf-8",
        )


def read_metadata(folder: Path) -> dict:
    """Read and return the folder's metadata."""

    file: Path = folder / METADATA_FILE

    if not file.exists():
        return {
            "categories": [],
        }

    return json.loads(file.read_text(encoding="utf-8"))


def get_categories(folder: Path) -> list[str]:
    """Get folders created by the organizer."""

    metadata = read_metadata(folder)
    return metadata.get("categories", [])


def add_category(folder: Path, category: str) -> None:
    """Add a category to the metadata file."""

    metadata = read_metadata(folder)

    if category not in metadata["categories"]:
        metadata["categories"].append(category)

    file: Path = folder / METADATA_FILE

    file.write_text(
        json.dumps(metadata, indent=4),
        encoding="utf-8",
    )
