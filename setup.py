import os
from setuptools import setup

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: POSIX :: Linux",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
    "Natural Language :: English",
    "Natural Language :: French",
    "Natural Language :: Italian",
    "Natural Language :: Russian",
    "Natural Language :: Spanish",
    "Operating System :: OS Independent",
]

with open(os.path.join(os.path.dirname(__file__), "README.md")) as fd:
    ext_long_desc = fd.read()

setup(
    name="tkFontSelector",
    version="1.0.2",
    description="Simple font chooser for Tkinter",
    long_description=ext_long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/jlw4049/tkFontChooser",
    author="Jessie Wilson",
    author_email="jessielw4049@gmail.com",
    license="MIT",
    classifiers=CLASSIFIERS,
    keywords=["tkFontSelector", "tkinter", "font", "fontchooser"],
    packages=["tkfontselector"],
)
