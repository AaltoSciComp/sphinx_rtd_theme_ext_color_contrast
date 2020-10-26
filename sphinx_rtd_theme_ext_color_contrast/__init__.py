import os

import sphinx

from ._version import __version__

def init_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_static'))
    app.config.html_static_path.append(static_path)


def setup(app):
    app.connect('builder-inited', init_static_path)
    if sphinx.version_info[0] >= 3:
        app.add_css_file('sphinx_rtd_theme_ext_color_contrast.css')
    else:
        app.add_stylesheet('sphinx_rtd_theme_ext_color_contrast.css')
