project = "nextcord.ext.activities"
copyright = "2022, MaskDuck"
author = "MaskDuck"
release = "2022.03.14"
version = "2022.03.14"

autosectionlabel_prefix_document = True
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_book_theme"
]

language = "en"

autodoc_member_order = "bysource"

html_theme = 'sphinx_book_theme'

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "nextcord": ("https://nextcord.readthedocs.io/en/latest/", None)
}
