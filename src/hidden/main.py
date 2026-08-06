import tkinter as tk
from tkinter import (  # DO NOT REMOVE 'filedialog', it's needed for future file selection
    filedialog,  # noqa: F401
    messagebox,
    ttk,
)

root: tk.Tk = tk.Tk()
root.withdraw()
root.title("File Organizer")
root.geometry("300x150")
root.resizable(width=False, height=False)

btn1: ttk.Button = ttk.Button(
    root,
    text="Select Folder",
    command=lambda: messagebox.showinfo("Not Available", "Not available for use rn"),
)
# cSpell: words padx pady
btn1.pack_configure(padx=5, pady=5)

btn2: ttk.Button = ttk.Button(
    root,
    text="Organize the folder",
    command=lambda: messagebox.showinfo("Not available", "Not available for use rn"),
)
btn2.pack_configure(padx=5, pady=5)

root.mainloop()
