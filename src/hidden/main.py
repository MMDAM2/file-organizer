import tkinter as tk
from tkinter import messagebox, ttk

root: tk.Tk = tk.Tk()
root.title("Nigga helper")
root.geometry("300x150")

btn1: ttk.Button = ttk.Button(
    root,
    text="Nigga run!",
    command=lambda: messagebox.showinfo("Hey nigga", "Run becuase white are cooming!"),
)
btn1.pack()

root.mainloop()
print("closed by : useer")
