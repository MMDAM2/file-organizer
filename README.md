# File Organizer

> A Python script that automatically organizes files based on their file extensions.

## Features

- Organizes files based on their extensions
- Automatically handles duplicate filenames
- Features a entry level GUI

## Installation

### Requirements

- Python v3.10+

### Steps

- Clone the repository:

```bash
git clone https://github.com/MMDAM2/file_organizer.git
cd file_organizer
```

- Make the file executable:

> [!NOTE]
> You can skip this part in Windows

```bash
chmod +x src/file_organizer/main.py
```

- Run the file using:

> [!NOTE]
> You can also skip this in Windows :point_down:

```bash
src/hidden/main.py
```

or

```bash
python3 src/file_organizer/main.py
```

## File Structure

<!-- cSpell: words pyproject -->

```none
-> .github
  -> workflows
    -> github-yml.yml
-> src
  -> file_organizer
    -> README.md
    -> main.py
    -> __init__.py
    -> organizer.py
    -> categories.py
-> tests
  -> test_organizer.py
-> .gitignore
-> .prettierrc
-> .python-version
-> uv.lock
-> README.md
-> pyproject.toml
```

<!-- Github Markdown Link: https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax  -->
<!-- cSpell: disable-next-line  -->
<!-- mikhay in zaban ro yad begiri az link bala estefade kon -->

## Notes

- File are moved, not copied nor deleted
- Do not use this as a main organizing app
- Existing files with same names will be renamed to prevent overwriting
