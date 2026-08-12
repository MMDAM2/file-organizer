#!/usr/bin/env python3
# Do NOT remove the line above or I'll kill you
# cSpell: words Mobin Saghebi MMDAM padx pady

"""Main app"""

import logging  # Logging the app
import tkinter as tk  # The basic GUI framework
from pathlib import Path  # No `os.path` allowed
from tkinter import (
    filedialog,
    messagebox,
    ttk,
)

from file_organizer.organizer import organizer

# filedialog.askdirectory()

# Make a 'log' folder

log_path = Path(__file__).parent / "log"  # In this case, __file__ is the script's path
log_path.mkdir(exist_ok=True)

# Log file's configuration
logging.basicConfig(
    filename=log_path / "main.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)


def browse() -> None:
    """Open a file browser"""
    path = filedialog.askdirectory(title="Select a folder")

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
    ) = organizer(path)
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


# Initialize a window
window = tk.Tk()
window.title("Folder")

# Maybe we should change the size of the window
# FIXME: Change the window size
window.geometry("400x250")
window.resizable(width=False, height=False)
window.protocol("WM_DELETE_WINDOW", window.quit)

txt1 = ttk.Entry(window, width=40)
txt1.pack()

btn2 = tk.Button(window, text="Browse", bg="yellow", command=browse)  # type: ignore
btn2.pack()

show_get = tk.Label(window)
show_get.pack()

# We're using a lambda because we need to pass a argument
org_button = tk.Button(
    window,
    text="Organize folder",
    bg="green",
    command=lambda: on_click_button(txt1.get()),  # type: ignore
)

# pady is essentially putting a space to breath in the userspace
org_button.pack(pady=10)


credit = tk.Label(window, text="Made By :\nMobin Saghebi\nMMDAM2", fg="gray")
credit.pack_configure(pady=10)

# Run the program
window.mainloop()
