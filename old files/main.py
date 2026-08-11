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

    def browse():
        path = filedialog.askdirectory(title="Select a folder")
        if path == "":
            messagebox.showwarning("Warning", "The given directory does not exist")
            show_get.config(text="Empty", fg="white", bg="gray")
        txt1.insert(0, path)

    def back() -> None:
        """Destroys the new initialized window and brings `root` window to focus"""
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title("Folder")
    window.geometry("400x250")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW", window.quit)

    txt1 = ttk.Entry(window, width=40)
    txt1.pack()

    btn2 = tk.Button(window, text="Browse", bg="yellow", command=browse)
    btn2.pack_configure(pady=5)

    show_get = tk.Label(window)
    show_get.pack()

    def on_click_button(path: str) -> bool | None:

        try:
            (
                total,
                moved,
                success,
            ) = organizer(path)
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"{e}")
            return False

        if success:
            messagebox.showinfo(
                "Completed",
                f"Operation completed successfully\n\nTotal files: {total}\nMoved files: {moved}",
            )
        else:
            messagebox.showerror(
                "Failed", f"Operation failed\n\nTotal files: {total}\nMoved files: {moved}"
            )

        return None

    org_button = tk.Button(
        window,
        text="Organize folder",
        bg="green",
        command=lambda: on_click_button(txt1.get()),
    )
    org_button.pack(pady= 10)

    back_button = tk.Button(window, text="Return to menu", bg="red", command=back)
    back_button.pack_configure(pady=5)

    window.mainloop()


root: tk.Tk = tk.Tk()  # Amir nabayad az 'ttk.Tk' estefade koni kar nemikone
root.title("File Organizer")
root.geometry("400x200")
root.resizable(width=False, height=False)

# cSpell: words padx pady

btn2: ttk.Button = ttk.Button(root, text="Organize the folder", command=organize_folder)
btn2.pack_configure(padx=5, pady=5)

credit = tk.Label(root, text="Made By :\nMobin Saghebi\nMMDAM2", fg="gray")
credit.pack_configure(pady=10)

root.mainloop()

# Comment kon code man gayide shodam ta ino befahmam
# cSpell haye manam pak nakon
