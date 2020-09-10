sphinx-rtd-theme color contrast extension
=========================================

This increases some color contrast in sphinx_rtd_theme to better
satisfy web content accessibility guidelines.  This is by no means a
proper fix, but some quick hacks by an uneducated person.  It tries to
make minimal changes, though.

This package will be deprecated once sphinx_rtd_theme is improved
upstream: https://github.com/readthedocs/sphinx_rtd_theme/issues/971

Currently it is not on PyPI (but could be), because I am hoping
sphinx_rtd_theme will be updated before that is necessary.  To
install, add this to ``requirements.txt``::

  https://github.com/AaltoSciComp/sphinx_rtd_theme_ext_color_contrast/archive/master.zip

And then add the extension in ``conf.py``::

  extensions = [
     ...
     'sphinx_rtd_theme_ext_color_contrast',
  ]

Style changes
-------------

Text contrast:

- Increase link text saturation
- Increase literal text saturation
- Increase footer contrast

Update pygments elements for contrast

Admonition colors

- Make the admonition title backgrounds darker.
- These are very long CSS selectors, copied from what the current
  theme uses.

Make the sidebar background darker
