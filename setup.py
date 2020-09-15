# https://packaging.python.org/guides/distributing-packages-using-setuptools/
# 'wheel' may be a build-dependency, it's also dep of twine

from os.path import join, dirname
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

version_ns = { }
exec(open('sphinx_rtd_theme_ext_color_contrast/_version.py').read(), version_ns)
version = version_ns['__version__']
del version_ns

requirementstxt = join(dirname(__file__), "requirements.txt")
requirements = [ line.strip() for line in open(requirementstxt, "r") if line.strip() ]

setuptools.setup(name='sphinx_rtd_theme_ext_color_contrast',
      version=version,
      description='sphinx_rtd_theme extension to enhance color contrast',
      long_description=long_description,
      long_description_content_type="text/x-rst",  # ReST is the default
      url="https://github.com/AaltoSciComp/sphinx_rtd_theme_ext_color_contrast/",
      author='Richard Darst',
      #author_email='',
      packages=['sphinx_rtd_theme_ext_color_contrast'],           # packages
      package_data={
          "sphinx_rtd_theme_ext_color_contrast": ['_static/*'],
          },
      #py_modules=["nbscript"],   # single modules
      keywords='sphinx-extension',
      install_requires=requirements,
      # https://pypi.org/classifiers/
      classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Extension",
        "Operating System :: OS Independent",
    ],
  )

# python setup.py sdist bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# twine upload dist/*
