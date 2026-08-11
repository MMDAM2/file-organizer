"""Temporary file for planning"""

import tkinter as tk
from tkinter import ttk


def mmd():
    root.withdraw()

    def back():
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title("MMD")
    window.geometry("500x500")

    window.protocol("WM_DELETE_WINDOW", window.quit)

    bb = tk.Button(window, text="Return to menu", bg="red", command=back)
    bb.pack_configure()

    kar_ha = tk.Label(
        window,
        text="Boro log kardan barname ro yad begir,\n baraye temp ham baraye raftan be\n khat badi az '\\n' estefade kon",
    )
    kar_ha.pack_configure(pady=5)

    window.mainloop()


def mobin():
    root.withdraw()

    def back():
        window.destroy()
        root.deiconify()

    window = tk.Tk()
    window.title("Mobin")
    window.geometry("500x500")
    window.protocol("WM_DELETE_WINDOW", window.quit)

    bb = tk.Button(window, text="Return to menu", bg="red", command=back)
    bb.pack_configure()

    kar_ha = tk.Label(
        window, text="hanooz kamelesh nakardam vali bebin bug ya chizi nadare"
    )
    kar_ha.pack_configure(pady=5)

    window.mainloop()


root = tk.Tk()
root.title("کار هایی که باید انجام بدی")
root.geometry("500x150")
root.protocol("WM_DELETE_WINDOW", root.quit)

b1 = ttk.Button(root, text="کار های MMD", command=mmd)
b1.pack_configure(pady=10)

b2 = ttk.Button(root, text="کار های mobin", command=mobin)
b2.pack_configure(pady=10)

root.mainloop()
