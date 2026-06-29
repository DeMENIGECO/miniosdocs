from pathlib import Path
import sys

# Percorso del progetto
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# -- Informazioni sul progetto ------------------------------------------------

project = "miniOS"
author = "miniOS"
copyright = "2026, miniOS"

# -- Configurazione generale --------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

language = "it"

# -- Opzioni HTML -------------------------------------------------------------

html_theme = "furo"
html_static_path = ["_static"]

# -- Autodoc ------------------------------------------------------------------

autodoc_member_order = "bysource"
autodoc_typehints = "description"

# -- Napoleon -----------------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True

# -- Todo ---------------------------------------------------------------------

todo_include_todos = True
