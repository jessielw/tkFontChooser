import ctypes
import locale
import os
import platform
from typing import Union


def system_locale() -> Union[str, None]:
    lang = None
    if platform.system() == "Windows":
        windll = ctypes.windll.kernel32
        language_str = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        lang = language_str.split("_")[0]
    else:
        language_str = os.environ.get("LANG")
        lang = language_str.split("_")[0]
    return lang
