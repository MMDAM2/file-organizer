import tkinter as tk
from tkinter import (  # DO NOT REMOVE 'filedialog', it's needed for future file selection
    filedialog,  # noqa: F401
    messagebox,
    ttk,
)


def organize_file():
    root.withdraw()

    def back():
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title()
    window.geometry("400x150")
    window.resizable(width=False,height=False)
    window.protocol("WM_DELETE_WINDOW", window.quit)

    helper = tk.Label(
        window,
        text= "Enter your file (path) also you can with ',' enter multiple files",
        fg= "gray"
    )
    helper.pack_configure(pady=1)

    get = ttk.Entry(
            window,
            width=40
        )
    get.pack_configure(pady = 5)

    org_button = tk.Button(
        window,
        text= "organize file / files",
        bg= "green"
        #, command= 
    )
    org_button.pack_configure(pady= 5)

    back_button = tk.Button(
        window,
        text= "Return to main menu",
        bg= "red",
        command= back
    )
    back_button.pack_configure(pady= 5)

    window.mainloop()

def organize_folder():
    root.withdraw()

    def back():
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title()
    window.geometry("400x150")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW", window.quit)

    helper = tk.Label(
        window,
        text= "Enter your folder (path) also you can with ',' enter multiple folder",
        fg = "gray"
    )
    helper.pack_configure(pady= 1)

    get = ttk.Entry(
        window,
        width=40
    )
    get.pack_configure(pady= 5)

    org_button = tk.Button(
        window,
        text= "Oganize folder / folders",
        bg= "green"
        #, command=
    )
    org_button.pack_configure(pady= 5)

    back_button = tk.Button(
        window,
        text= "Return to menu",
        bg= "red",
        command= back
    )
    back_button.pack_configure(pady= 5)

    window.mainloop()

root: ttk.Tk = tk.Tk()
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

btn2: ttk.Button = ttk.Button(
    root,
    text="Organize the folder",
    command=organize_folder
)
btn2.pack_configure(padx=5, pady=5)

credit = tk.Label(
    root,
    text= "Made By :\nMobin Saghebi\nMMDAM2",
    fg= "gray"
)
credit.pack_configure(pady= 10)

root.mainloop()