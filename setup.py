# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301
import os

NAME = "criteo_marketing"
VERSION = "1.0.29"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

AUTHOR='Criteo'
README_CONTENT_TYPE='text/markdown'

this_dir = os.path.dirname(__file__)
readme_filename = os.path.join(this_dir, 'README.md')
with open(readme_filename) as f:
    PACKAGE_LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Marketing API v.1.0",
    author_email="",
    author=AUTHOR,
    url="",
    keywords=[AUTHOR, "OpenAPI-Generator", "Marketing API v.1.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type=README_CONTENT_TYPE,
    long_description=PACKAGE_LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
)
