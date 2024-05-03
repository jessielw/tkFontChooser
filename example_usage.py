from tkinter import Tk, ttk
from sys import platform
from tkfontselector.ask_font import ask_font

EXAMPLE_FONT_FAMILY = {
    "family": "Comic Sans MS",
    "size": 10,
    "weight": "normal",
    "slant": "roman",
    "underline": 0,
    "overstrike": 0,
}


if __name__ == "__main__":
    """Example Usage"""
    root = Tk()
    style = ttk.Style(root)
    if "win" == platform[:3]:
        style.theme_use("vista")
    elif "darwin" in platform:
        style.theme_use("clam")
    else:
        style.theme_use("clam")
    bg = style.lookup("TLabel", "background")
    root.configure(bg=bg)
    label = ttk.Label(root, text="Chosen font: ")
    label.pack(padx=10, pady=(10, 4))

    def callback():
        font = ask_font(root, title="Choose a font")
        if font:
            # spaces in the family name need to be escaped
            font["family"] = font["family"].replace(" ", "\ ")
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
            if font["underline"]:
                font_str += " underline"
            if font["overstrike"]:
                font_str += " overstrike"
            label.configure(
                font=font_str, text="Chosen font: " + font_str.replace("\ ", " ")
            )

    ttk.Button(root, text="Font Selector", command=callback).pack(padx=10, pady=(4, 10))
    root.mainloop()
