#!/usr/bin/env python

import os.path
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

CLASSIFIERS = [
	"Development Status :: 5 - Production/Stable",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: MIT License",
	"Programming Language :: Python",
	"Topic :: Software Development :: Libraries :: Python Modules",
]

import ptch
VERSION = ptch.__version__

setup(
	name = "python-ptch",
	py_modules = ["ptch"],
	author = "Jerome Leclanche",
	author_email = "jerome.leclanche+python-ptch@gmail.com",
	classifiers = CLASSIFIERS,
	description = "Blizzard BSDIFF-based PTCH file format support",
	download_url = "http://github.com/Adys/python-ptch/tarball/master",
	long_description = README,
	url = "http://github.com/Adys/python-ptch",
	version = VERSION,
)
