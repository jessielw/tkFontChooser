from typing import Union
from tkfontselector.tkfontselector import FontSelector
from tkinter import Tk, Toplevel


def ask_font(
    master: Union[Tk, Toplevel, None] = None,
    text: str = "Abcd",
    title: str = "Font Selector",
    fixed_only: bool = False,
    families_only: bool = False,
    font_args: dict = {},
) -> dict:
    """
    Open the Font Selector and return a dictionary of the font properties.

    General Arguments:
        master: Tk or Toplevel instance
            master window
        text: str
            sample text to be displayed in the Font Selector
        title: str
            dialog title
        fixed_only: bool
            Display fixed only families
        families_only: bool
            Will only display Families part of the UI
        font_dict: dict
            dictionary, like the one returned by the ``actual`` method of a ``Font`` object:
                {'family': str,
                    'size': int,
                    'weight': 'bold'/'normal',
                    'slant': 'italic'/'roman',
                    'underline': bool,
                    'overstrike': bool}
        kwargs: dict

    Font arguments:
        family: str
            font family
        size: int
            font size
        slant: str
            "roman" or "italic"
        weight: str
            "normal" or "bold"
        underline: bool
            whether the text is underlined
        overstrike: bool
            whether the text is overstriked

    Output:

        dictionary is similar to the one returned by the ``actual`` method of a tkinter ``Font`` object:
            {'family': str,
             'size': int,
             'weight': 'bold'/'normal',
             'slant': 'italic'/'roman',
             'underline': bool,
             'overstrike': bool}

    """
    chooser = FontSelector(master, text, title, fixed_only, families_only, font_args)
    chooser.wait_window(chooser)
    return chooser.get_res()
