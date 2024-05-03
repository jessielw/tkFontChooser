import unittest
import logging
from tkfontselector import FontSelector, ask_font
from tkinter import Toplevel, ttk
from tkinter import font as tkFont


class BaseWidgetTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(filename="/tmp/test.log", level=logging.DEBUG)
        self.window = Toplevel()
        self.window.update()

    def tearDown(self):
        self.window.update()
        self.window.destroy()


class TestEvent:
    """Fake event for testing."""

    def __init__(self, **kwargs):
        self._prop = kwargs

    def __getattr__(self, attr):
        if attr not in self._prop:
            raise AttributeError("TestEvent has no attribute %s." % attr)
        else:
            return self._prop[attr]


class TestFontSelector(BaseWidgetTest):
    def test_FontSelector_init(self):
        FontSelector(
            self.window,
            {"family": "Arial", "weight": "bold", "slant": "italic"},
            text="Abcd" * 20,
            title="Test",
        )
        self.window.update()

    def test_FontSelector_methods(self):
        props = {
            "family": "TkDefaultFont",
            "weight": "bold",
            "size": 27,
            "slant": "italic",
        }
        fc = FontSelector(self.window, props)
        self.window.update()

        e = ttk.Entry(self.window)
        e.insert(0, "abcd")
        fc.select_all(TestEvent(widget=e))
        self.assertEqual(e.selection_get(), "abcd")

        self.assertEqual(fc.get_res(), "")
        fc.ok()
        self.window.update()
        font = tkFont.Font(self.window, **props)
        self.assertEqual(fc.get_res(), font.actual())
        # ok() destroys the toplevel
        fc = FontSelector(self.window, {"family": "TkDefaultFont", "size": 20})
        self.window.update()
        i = fc.list_family.curselection()[0]
        self.assertEqual(fc.fonts[i], "TkDefaultFont")

        self.assertEqual(fc.preview_font.actual()["weight"], "normal")
        fc.var_bold.set(True)
        fc.toggle_bold()
        self.window.update()
        self.assertEqual(fc.preview_font.actual()["weight"], "bold")

        self.assertEqual(fc.preview_font.actual()["slant"], "roman")
        fc.var_italic.set(True)
        fc.toggle_italic()
        self.window.update()
        self.assertEqual(fc.preview_font.actual()["slant"], "italic")

        self.assertEqual(fc.preview_font.actual()["underline"], False)
        fc.var_underline.set(True)
        fc.toggle_underline()
        self.window.update()
        self.assertEqual(fc.preview_font.actual()["underline"], True)

        self.assertEqual(fc.preview_font.actual()["overstrike"], False)
        fc.var_overstrike.set(True)
        fc.toggle_overstrike()
        self.window.update()
        self.assertEqual(fc.preview_font.actual()["overstrike"], True)
        fc.up_family(None)
        self.window.update()
        self.assertEqual(fc.list_family.curselection()[0], i - 1)
        fc.down_family(None)
        self.window.update()
        self.assertEqual(fc.list_family.curselection()[0], i)

        i = fc.list_size.curselection()[0]
        self.assertEqual(fc.sizes[i], "20")
        fc.up_size(None)
        self.window.update()
        self.assertEqual(fc.list_size.curselection()[0], i - 1)
        fc.down_size(None)
        self.window.update()
        self.assertEqual(fc.list_size.curselection()[0], i)

        fc.entry_size.delete(0, "end")
        fc.entry_size.insert(0, "17")
        i = fc.list_size.curselection()[0]
        self.assertEqual(fc.sizes[i], "18")
        fc.up_size(None)
        self.window.update()
        self.assertEqual(fc.sizes[fc.list_size.curselection()[0]], "16")
        self.assertEqual(fc.entry_size.get(), "16")
        fc.entry_size.delete(0, "end")
        fc.entry_size.insert(0, "17")
        fc.down_size(None)
        self.window.update()
        self.assertEqual(fc.sizes[fc.list_size.curselection()[0]], "18")
        self.assertEqual(fc.entry_size.get(), "18")

        fc.keypress(TestEvent(char=fc.fonts[0][0]))
        self.assertEqual(fc.list_family.curselection()[0], 0)

    def test_askfont(self):

        def test(event):
            event.widget.ok()
            fontprops = event.widget.get_res()
            self.assertEqual(fontprops["size"], 20)
            self.assertEqual(fontprops["slant"], "italic")
            self.assertEqual(fontprops["weight"], "bold")
            self.assertTrue(fontprops["underline"])
            self.assertTrue(fontprops["overstrike"])

        def events():
            self.window.update()
            c = list(self.window.children.values())[0]
            c.bind("<Visibility>", test)
            self.window.update()
            c.withdraw()
            self.window.update()
            c.deiconify()

        self.window.after(100, events)
        ask_font(
            master=self.window,
            family="TkDefaultFont",
            size=20,
            slant="italic",
            weight="bold",
            underline=True,
            overstrike=True,
        )
