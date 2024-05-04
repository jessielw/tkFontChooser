# tkFontChooser

A simple font chooser for tkinter that allows the user to select the font
family among the fonts available on his/her system. The size and style
(bold, italic, underline, strike-through) of the text can be set too.

This module contains a `FontSelector` class which implements the font
chooser and an `ask_font` function that displays the font chooser and
returns the chosen font when the user closes the font chooser. The font
is returned as a dictionary like the one returned by the function
`tkFont.Font.actual`.

## Requirements

- Linux, Windows, Mac
- Python 3 with tkinter

## Installation

`pip install tkFontSelector`

## Documentation

```python
from tkfontselector import ask_font

ask_font(master=None, text="Abcd", title="Font Chooser", **font_args)
```

Open the font chooser and return a dictionary of the font properties. This
dictionary is similar to the one returned by the `actual` method of a tkinter
`Font` object.

```python
# example dictionary
{'family': str,
    'size': int,
    'weight': 'bold'/'normal',
    'slant': 'italic'/'roman',
    'underline': bool,
    'overstrike': bool}
```

## General arguments

`master`: Tk, Toplevel, or None (Optional)

`text`: str (Optional) _text to show in the font selection window_

`title`: str (Optional) _changes the title of the window_

`fixed_only`: bool (Optional), _if set to `True` will only show `Fixed (mono spaced)` fonts_

`families_only`: bool (Optional), _if set to `True` will only show Font Families part of the UI_

`font_dict`: dict (Optional) _font dictionary like an actual Font object_

`**kwargs`: (Optional) _pass any other args that might be accepted_

## Font Arguments

`family`: str

`size`: int

`slant`: str (roman or italic)

`weight`: str (normal or bold)

`underline`: bool

`overstrike`: bool

## Example

```python
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
        font = ask_font(root, title="Choose a font", font_args=EXAMPLE_FONT_FAMILY)
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
```
