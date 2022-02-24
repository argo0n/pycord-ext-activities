import os
import sys

project = "nextcord.ext.activities"
copyright = "2022, MaskDuck"
author = "MaskDuck"
release = "2022.02.24"
version = "2022.02.24"

autosectionlabel_prefix_document = True
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx-book-theme"
]

language = "en"

autodoc_member_order = "bysource"

html_theme = 'sphinx_book_theme'

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None)
}
