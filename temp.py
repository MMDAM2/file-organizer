"""Temporary file for planning"""

import tkinter as tk
from tkinter import ttk


def mmd() -> None:
    root.withdraw()

    def back() -> None:
        window.destroy()
        root.deiconify()

    window: tk.Tk = tk.Tk()
    window.title(string="MMD")
    window.geometry(newGeometry="500x500")

    window.protocol(name="WM_DELETE_WINDOW", func=window.quit)

    bb: tk.Button = tk.Button(master=window, text="Return to menu", bg="red", command=back)
    bb.pack_configure()

    kar_ha: tk.Label = tk.Label(
        master=window,
        text="Boro log kardan barname ro yad begir,\n baraye temp ham baraye raftan be\n khat badi az '\\n' estefade kon",
    )
    kar_ha.pack_configure(pady=5)

    window.mainloop()


def mobin() -> None:
    root.withdraw()

    def back() -> None:
        window.destroy()
        root.deiconify()

    window: tk.Tk = tk.Tk()
    window.title(string="Mobin")
    window.geometry(newGeometry="500x500")
    window.protocol(name="WM_DELETE_WINDOW", func=window.quit)

    bb: tk.Button = tk.Button(master=window, text="Return to menu", bg="red", command=back)
    bb.pack_configure()

    kar_ha: tk.Label = tk.Label(master=window, text="hanooz kamelesh nakardam vali bebin bug ya chizi nadare")
    kar_ha.pack_configure(pady=5)

    window.mainloop()


root: tk.Tk = tk.Tk()
root.title(string="کار هایی که باید انجام بدی")
root.geometry(newGeometry="500x150")
root.protocol(name="WM_DELETE_WINDOW", func=root.quit)

b1: ttk.Button = ttk.Button(master=root, text="کار های MMD", command=mmd)
b1.pack_configure(pady=10)

b2: ttk.Button = ttk.Button(master=root, text="کار های mobin", command=mobin)
b2.pack_configure(pady=10)

root.mainloop()
