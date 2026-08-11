##!/usr/bin/env python3
# خط بالارو برا ویندوز نمیشد حذف کردم

"""Main app"""

import tkinter as tk
from tkinter import (  # TODO: Use `filedialog` for target directory
    filedialog,
    messagebox,
    ttk,
)

from organizer import organizer

# filedialog.askdirectory()


def browse():
    path = filedialog.askdirectory(title="Select a folder")
    if path == "":
        messagebox.showwarning("Warning", "The given directory does not exist")
        show_get.config(text="Empty", fg="white", bg="gray")
    txt1.insert(0, path)

    

    

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




window = tk.Tk()
window.title("Folder")
window.geometry("400x250")
window.resizable(width=False, height=False)
window.protocol("WM_DELETE_WINDOW", window.quit)

# cSpell: words padx pady

txt1 = ttk.Entry(window, width=40)
txt1.pack()

btn2 = tk.Button(window, text="Browse", bg="yellow", command=browse)  # type: ignore
btn2.pack_configure(pady=5)

show_get = tk.Label(window)
show_get.pack()

org_button = tk.Button(
    window,
    text="Organize folder",
    bg="green",
    command=lambda: on_click_button(txt1.get()),  # type: ignore
)
org_button.pack(pady= 10)

credit = tk.Label(window, text="Made By :\nMobin Saghebi\nMMDAM2", fg="gray")
credit.pack_configure(pady=10)

window.mainloop()

# Comment kon code man gayide shodam ta ino befahmam
# cSpell haye manam pak nakon
