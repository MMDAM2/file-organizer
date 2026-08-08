##!/usr/bin/env python3

"""Main app"""

import tkinter as tk
from tkinter import (  # TODO: Use `filedialog` for target directory
    filedialog,
    messagebox,
    ttk,
)

from organizer import organizer

# filedialog.askdirectory()


def organize_folder() -> None:
    """Folder window"""
    root.withdraw()

    def select_folder():
        path = filedialog.askdirectory(
            title="open folder for organizer"
        )
        show_get.config(text= path, fg= "white", bg= "gray")
        if path == "":
            messagebox.showwarning(
                "Warning",
                "you have not entered folder"
            )
            show_get.config(text= "Empty", fg= "white", bg= "gray")

    def back() -> None:
        """Destroys the new initialized window and brings `root` window to focus"""
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title()
    window.geometry("400x150")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW", window.quit)

    getb = tk.Button(
        window,
        text= "select folder",
        bg= "yellow",
        command= select_folder)
    getb.pack_configure()

    show_get = tk.Label(
        window
    )
    show_get.pack_configure(pady= 5)

    def on_click_button(path: str) -> None:
        (
            total,
            moved,
            success,
        ) = organizer.organizer(path)

        if success:
            messagebox.showinfo(
                "Completed",
                f"Operation completed successfully\n\nTotal files: {total}\nMoved files: {moved}",
            )

    org_button = tk.Button(
        window,
        text="Organize folder",
        bg="green",
        command=lambda: on_click_button(getb.get()),
    )
    org_button.pack_configure(pady=5)

    back_button = tk.Button(window, text="Return to menu", bg="red", command=back)
    back_button.pack_configure(pady=5)

    window.mainloop()


root: tk.Tk = tk.Tk()  # Amir nabayad az 'ttk.Tk' estefade koni kar nemikone
root.title("File Organizer")
root.geometry("400x150")
root.resizable(width=False, height=False)

# cSpell: words padx pady

btn2: ttk.Button = ttk.Button(root, text="Organize the folder", command=organize_folder)
btn2.pack_configure(padx=5, pady=5)

credit = tk.Label(root, text="Made By :\nMobin Saghebi\nMMDAM2", fg="gray")
credit.pack_configure(pady=10)

root.mainloop()

# Comment kon code man gayide shodam ta ino befahmam
# cSpell haye manam pak nakon
