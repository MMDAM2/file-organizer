#!/usr/bin/env python3
# Do NOT remove the line above or I'll kill you
# cSpell: words Mobin Saghebi MMDAM padx pady onvalue offvalue yscrollcommand

"""Main app"""

# import logging  # Logging the app
import os
import tkinter as tk  # The basic GUI framework
from pathlib import Path
from subprocess import run as command

# from pathlib import Path  # No `os.path` allowed
from tkinter import (
    filedialog,
    messagebox,
    ttk,
)

from file_organizer.organizer import organizer, preview

if os.name != "posix":
    command(args=["cls"], shell=True, check=True)
else:
    if os.environ.get(key="TERM", default=None) is not None:
        # subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True, check=True)
        command(args=["clear"], shell=True, check=True)

# Make a 'log' folder
# log_path: Path = Path(__file__).parent / "log"  # In this case, __file__ is the script's path
# log_path.mkdir(exist_ok=True) # Don't create the directory again if it exists
#
# # Log file's configuration
# logging.basicConfig(
#     filename=log_path / "main.log",
#     level=logging.DEBUG, # Severity is DEBUG
#     format="%(levelname)s: %(message)s", # This is enough for information
# )
#
# # Get a logger with the app's name
# logger: logging.Logger = logging.getLogger(name=__name__)
# Not logging for now


def browse() -> None:
    """Open a file browser"""
    path: str = filedialog.askdirectory(title="Select a folder")

    # Check if there was a path provided
    if path == "":
        messagebox.showwarning(title="Warning", message="No given directory", icon="question")
        show_get.config(text="Empty", fg="white", bg="gray")

    # Put the given path inside an `Entry`
    txt1.insert(index=0, string=path)


def show_preview(op_preview: list[tuple[str, Path]]) -> None:
    """Show a preview of the whole operation

    Args:
        op_preview (list[tuple[str, Path]]): a list containing the filename and it's destination
    """
    preview_window: tk.Toplevel = tk.Toplevel(master=window)  # Make window on top of the root one
    preview_window.deiconify()
    preview_window.attributes("-topmost", 1)
    preview_window.title(string="Preview")  # Window title
    preview_window.geometry(newGeometry="600x400")  # Window size (w: width, h: height)

    label: tk.Label = tk.Label(master=preview_window, text="The following files will be moved:")
    label.pack(
        anchor="w", padx=10, pady=(10, 5)
    )  # Change the label direction to left (anchor w is basically west or left)

    frame: tk.Frame = tk.Frame(master=preview_window)  # Make a frame for the listbox

    scrollbar: ttk.Scrollbar = ttk.Scrollbar(master=frame)  # Make a scrollbar
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox: tk.Listbox = tk.Listbox(
        master=frame, yscrollcommand=scrollbar.set
    )  # A list for representing changes
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=listbox.yview)

    for name, dest in op_preview:
        listbox.insert(tk.END, f"{name} -> {dest}")

    preview_button_frame: tk.Frame = tk.Frame(master=preview_window)  # Make a frame for the buttons
    preview_button_frame.pack(fill=tk.X, padx=10, pady=10)

    cancel_button: ttk.Button = ttk.Button(
        master=preview_button_frame, text="Cancel", command=preview_window.destroy
    )  # Make a button for cancelling the operation
    cancel_button.pack(side=tk.RIGHT, padx=(5, 0))

    continue_button: ttk.Button = ttk.Button(
        master=preview_button_frame,
        text="Continue",
        command=lambda: organize_files(path=txt1.get()),
    )  # Make a button to start processing the files
    continue_button.pack(side=tk.RIGHT)

    frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)  # Expand the ListBox from both sides


def organize_files(path: str) -> None:
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
            title="Completed",
            message=f"""Operation completed successfully

            Total files: {total}
            Moved files: {moved}""",
        )
    else:
        messagebox.showerror(
            title="Failed",
            message=f"""Operation failed

            Total files: {total}
            Moved files: {moved}""",
        )


def dry_run_check(check: bool) -> None:
    """Check whether we should do a dry run

    Args:
        check (bool): Status for dry run availability
    """
    if not txt1.get():  # If no path is given, throw a window
        messagebox.showerror(title="Empty", message="Empty directory is given")
        return
    if check:  # Check if dry run is enabled
        organize_files(path=txt1.get())
    else:
        show_preview(op_preview=preview(input_path=txt1.get()))


# Note: fill=tk.Y means expand when window height changes
# fill=tk.X means expand when window width changes
# fill=tk.BOTH means expand when window size changes

# Initialize a window

window: tk.Tk = tk.Tk()
window.title(string="Folder")

dry_run: tk.BooleanVar = tk.BooleanVar(master=window)  # Make a `tkinter` boolean

window.geometry(newGeometry="500x325")  # Window size (w, h)
window.resizable(width=True, height=False)
window.minsize(460, 325)  # The minimum requirements for window size

button_frame: tk.Frame = tk.Frame(master=window)

txt1: ttk.Entry = ttk.Entry(master=window)
txt1.pack(fill=tk.X, expand=True)

btn2: tk.Button = tk.Button(master=button_frame, text="Browse", bg="yellow", command=browse)
btn2.pack(fill=tk.X)

show_get: tk.Label = tk.Label(master=window)
show_get.pack()

checkbutton: ttk.Checkbutton = ttk.Checkbutton(  # Make a checkbox
    master=window,
    text="Dry run (Experimental)",
    variable=dry_run,
    onvalue=True,
    offvalue=False,
)
checkbutton.pack(pady=10, side=tk.TOP)  # Align the button in the middle

# We're using a lambda because we need to pass an argument
org_button: tk.Button = tk.Button(
    master=button_frame,
    text="Organize folder",
    bg="green",
    command=lambda: dry_run_check(check=dry_run.get()),
)

# pady is essentially putting a space to breath in the userspace between widgets
org_button.pack(side=tk.LEFT, pady=10, expand=True, fill=tk.X)

button_frame.pack(anchor=tk.W, fill=tk.BOTH)

credit: tk.Label = tk.Label(master=window, text="Made By: Mobin Saghebi, MMDAM2", fg="gray")
# IDK why this exists
credit.pack_configure(pady=10)

# Run the program
if __name__ == "__main__":
    window.mainloop()
