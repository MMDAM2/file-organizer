#!/usr/bin/env python3
# Do NOT remove the line above or I'll kill you
# cSpell: words Mobin Saghebi MMDAM padx pady

"""Main app"""

import logging  # Logging the app
import os
import tkinter as tk  # The basic GUI framework
from pathlib import Path  # No `os.path` allowed
from tkinter import (
    filedialog,
    messagebox,
    ttk,
)
from subprocess import run

import organizer

if os.environ.get("TERM", None) is not None:
    # subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True, check=True)
    run(["cls"] if os.name == "nt" else ["clear"], shell=True, check=True)

# Make a 'log' folder
log_path: Path = Path(__file__).parent / "log"  # In this case, __file__ is the script's path
log_path.mkdir(exist_ok=True) # Don't create the directory again if it exists

# Log file's configuration
logging.basicConfig(
    filename=log_path / "main.log",
    level=logging.DEBUG, # Severity is DEBUG
    format="%(levelname)s: %(message)s", # This is enough for information
)

# Get a logger with the app's name
logger: logging.Logger = logging.getLogger(__name__)


def browse() -> None:
    """Open a file browser"""
    path: str = filedialog.askdirectory(title="Select a folder")

    # Check if there was a path provided
    if path == "":
        messagebox.showwarning("Warning", "The given directory does not exist", icon="question")
        show_get.config(text="Empty", fg="white", bg="gray")

    # Put the given path inside an `Entry`
    txt1.insert(0, path)


def on_click_button(path: str) -> None:
    """The handler for button click

    Args:
        path (str): The user's given path
    """
    # Not so sure if the given path is valid, so we just catch the error
    (
        total,
        moved,
        success,
    ) = organizer.organizer(path)
    # Check if organizing the files actually worked
    if success:
        messagebox.showinfo(
            "Completed",
            f"Operation completed successfully\n\nTotal files: {total}\nMoved files: {moved}",
        )
    else:
        messagebox.showerror(
            "Failed", f"Operation failed\n\nTotal files: {total}\nMoved files: {moved}"
        )



"""Main Program"""
# Initialize a window

window: tk.Tk = tk.Tk()
window.title("Folder")

window.geometry("400x250") # Window size (w, h)
window.resizable(width=False, height=False)

txt1: ttk.Entry = ttk.Entry(window, width=40)
txt1.pack()

btn2 = tk.Button(window, text="Browse", bg="yellow", command=browse)
btn2.pack()

show_get: tk.Label = tk.Label(window)
show_get.pack()

# We're using a lambda because we need to pass an argument
org_button: tk.Button = tk.Button(
    window,
    text="Organize folder",
    bg="green",
    command=lambda: on_click_button(txt1.get()),
)

# pady is essentially putting a space to breath in the userspace
org_button.pack(pady=10)

credit: tk.Label = tk.Label(window, text="Made By :\nMobin Saghebi\nMMDAM2", fg="gray") # IDK why this exists
credit.pack_configure(pady=10)

# Run the program
if __name__ == "__main__":
    window.mainloop()
