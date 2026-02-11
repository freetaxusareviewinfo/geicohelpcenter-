# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions are in another directory, add paths here if needed
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'GEICO Insurance Quote Guide'
copyright = '2026, GEICO Insurance Guide'
author = 'GEICO Insurance Guide'

# The full version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Page title (important for SEO)
html_title = "How to Get a GEICO Insurance Quote Online – Step-by-Step Guide"

# Short navigation title
html_short_title = "GEICO Quote Guide"

# Favicon (place favicon.ico inside _static folder)
html_favicon = '_static/favicon.ico'

# Theme (Recommended clean theme)
html_theme = 'alabaster'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks (for clickable FAQs)
html_allow_unsafe = True

# Remove powered by footer
html_theme_options = {
    'show_powered_by': False,
    'description': 'Simple guide to getting a GEICO insurance quote online quickly and easily.',
    'fixed_sidebar': True,
}

# Static files (CSS, images, favicon)
html_static_path = ['_static']
