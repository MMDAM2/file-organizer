"""Temporary file for planning"""

import tkinter as tk
from tkinter import ttk


def mmd():
    root.withdraw()
    windowmd.deiconify()

    def back():
        windowmd.withdraw()
        root.deiconify()

    bb = tk.Button(windowmd, text="Return to menu", bg="red", command=back)
    bb.pack_configure()

    kar_ha = tk.Label(
        windowmd,
        text="""Tkinteret ro yek zare dorost kon bad shekl shode, 
        az ttk.Tk ham estefade nakon vojood nadare, 
        va boro filedialog tkinter ro yad begir az tarigh oon az user file bekhah""",
    )
    kar_ha.pack_configure(pady=5)


def mobin():
    root.withdraw()
    windowm.deiconify()

    def back():
        windowm.withdraw()
        root.deiconify()

    bb = tk.Button(windowm, text="Return to menu", bg="red", command=back)
    bb.pack_configure()

    kar_ha = tk.Label(
        windowm,
        text=" برو و اون کامند های دف فایل و فولدر رو انجام بده\nچون من نمیدونم چه دفی میخوای بزاری و همینطور \nتوهم برو برام بنویس چیکار کنم",
    )
    kar_ha.pack_configure(pady=5)


root = tk.Tk()
root.title("کار هایی که باید انجام بدی")
root.geometry("500x150")
root.protocol("WM_DELETE_WINDOW", root.quit)

windowmd = tk.Tk()
windowmd.title("MMD")
windowmd.geometry("500x500")
windowmd.withdraw()
windowmd.protocol("WM_DELETE_WINDOW", windowmd.quit)

windowm = tk.Tk()
windowm.title("Mobin")
windowm.geometry("500x500")
windowm.withdraw()
windowm.protocol("WM_DELETE_WINDOW", windowm.quit)

b1 = ttk.Button(root, text="کار های MMD", command=mmd)
b1.pack_configure(pady=10)

b2 = ttk.Button(root, text="کار های mobin", command=mobin)
b2.pack_configure(pady=10)

root.mainloop()
windowmd.mainloop()
windowm.mainloop()
