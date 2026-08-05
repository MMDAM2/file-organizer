from ast import main
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root: tk.Tk = tk.Tk()

btn1: ttk.Button(root, text = "Nigga run!", command = lambda: messagebox.showinfo("Hey nigga", "Run becuase white are cooming!")) # type: ignore
btn1.pack()

root.mainloop()

if __name__ == "__main__":
    main()
