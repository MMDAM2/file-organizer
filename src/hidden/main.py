#!/usr/bin/env python3

"""Main app"""

import tkinter as tk
from tkinter import (  # TODO: Use `filedialog` for target directory
    messagebox,
    ttk,
)


def organize_file() -> None:
    """File window"""
    root.withdraw()

    def back() -> None:
        """Destroys the new initialized window and brings `root` window to focus"""
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title()
    window.geometry("400x150")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW", window.quit)

    helper = tk.Label(
        window,
        text="Enter your file (path) also you can with ',' enter multiple files",
        fg="gray",
    )
    helper.pack_configure(pady=1)

    get = ttk.Entry(window, width=40)
    get.pack_configure(pady=5)

    org_button = tk.Button(
        window,
        text="organize file / files",
        bg="green",
        command=lambda: messagebox.showinfo("Not available", "Still under development"),
    )
    org_button.pack_configure(pady=5)

    back_button = tk.Button(window, text="Return to main menu", bg="red", command=back)
    back_button.pack_configure(pady=5)

    window.mainloop()


def organize_folder() -> None:
    """Folder window"""
    root.withdraw()

    def back() -> None:
        """Destroys the new initialized window and brings `root` window to focus"""
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title()
    window.geometry("400x150")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW", window.quit)

    helper = tk.Label(
        window,
        text="Enter your folder (path) also you can with ',' enter multiple folder",
        fg="gray",
    )
    helper.pack_configure(pady=1)

    get = ttk.Entry(window, width=40)
    get.pack_configure(pady=5)

    org_button = tk.Button(
        window,
        text="Oganize folder / folders",
        bg="green",
        command=lambda: messagebox.showinfo("Not available", "Still under development"),
    )
    org_button.pack_configure(pady=5)

    back_button = tk.Button(window, text="Return to menu", bg="red", command=back)
    back_button.pack_configure(pady=5)

    window.mainloop()


root: tk.Tk = tk.Tk()  # Amir nabayad az 'ttk.Tk' estefade koni kar nemikone
root.title("File Organizer")
root.geometry("400x150")
root.resizable(width=False, height=False)

btn1: ttk.Button = ttk.Button(
    root,
    text="Select Folder",
    command=organize_file,
)
# cSpell: words padx pady
btn1.pack_configure(padx=5, pady=5)

btn2: ttk.Button = ttk.Button(root, text="Organize the folder", command=organize_folder)
btn2.pack_configure(padx=5, pady=5)

credit = tk.Label(root, text="Made By :\nMobin Saghebi\nMMDAM2", fg="gray")
credit.pack_configure(pady=10)

root.mainloop()

# Comment kon code man gayide shodam ta ino befahmam
# cSpell haye manam pak nakon
