sphinx-rtd-theme color contrast

This increases some color contrast in sphinx_rtd_theme to better
satisfy web content accessibility guidelines.  This is by no means a
proper fix, but some quick hacks by an uneducated person.  It tries to
make minimal changes, though.

This package will be deprecated once sphinx_rtd_theme is improved
upstream: https://github.com/readthedocs/sphinx_rtd_theme/issues/971


Text contrast:

- Increane link text saturation
- Increase literal text saturation
- Increase footer contrast

Update pygments elements for contrast

Admonition colors

- Make the admonition title backgrounds darker.
- These are very long CSS selectors, copied from what the current
  theme uses.

Make the sidebar background darker
