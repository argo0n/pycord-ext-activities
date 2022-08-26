project = "pycord.ext.activities"
copyright = "2022, MaskDuck, argo0n"
author = "MaskDuck, argo0n"
release = "2022.04.02"
version = "2022.04.02"

autosectionlabel_prefix_document = True
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel"
]

language = "en"

autodoc_member_order = "bysource"

html_theme = "furo"

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "pycord": ("https://docs.pycord.dev/en/master/index.html", None),
}
