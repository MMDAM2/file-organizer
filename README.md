# `tidyfiles`

> A Python program that automatically organizes files based on their file extensions.

## Features

* Organizes files based on their extensions
* Automatically handles duplicate filenames
* Features an entry-level GUI

> [!WARNING]
> This program should not be used as a primary solution for organizing files.
>
> Consider using a well-known and actively maintained file organizer instead.

## Installation

### Requirements

* Python 3.10+

> [!NOTE]
> `tidyfiles` mostly uses the Python standard library, so there are very few external dependencies.

### Steps

* Clone the repository:

```bash
git clone https://github.com/MMDAM2/tidyfiles.git
cd tidyfiles
```

* Install the project:

```bash
python -m pip install .
```

* Run the program:

```bash
tidyfiles
```

## Running from source

You can run TidyFiles directly from the repository without installing it.

### Linux / macOS

```bash
PYTHONPATH=src python3 -m tidyfiles
```

### Windows Command Prompt

```cmd
set PYTHONPATH=src
python -m tidyfiles
```

### Windows PowerShell

```powershell
$env:PYTHONPATH = "src"
python -m tidyfiles
```

## File Structure

<!-- cSpell: words pyproject tidyfiles -->

```text
-> .github
  -> workflows
    -> github-yml.yml

-> src
  -> tidyfiles
    -> README.md
    -> __init__.py
    -> __main__.py
    -> organizer.py
    -> categories.py
    -> metadata.py

-> tests
  -> test_organizer.py

-> .gitignore
-> .prettierrc
-> .python-version
-> uv.lock
-> README.md
-> pyproject.toml
```

## Notes

* Files are moved, not copied or deleted.
* Do not use `tidyfiles` as your primary file-organizing application.
* Existing files with the same names are renamed to prevent overwriting.
