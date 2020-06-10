# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301
import os

NAME = "criteo_marketing"
VERSION = "1.0.166"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

AUTHOR='Criteo'
README_CONTENT_TYPE='text/markdown'
PACKAGE_LONG_DESCRIPTION = """# Criteo Marketing SDK for Python
[![](https://img.shields.io/pypi/pyversions/criteo-marketing.svg)](https://pypi.org/project/criteo-marketing/)

IMPORTANT: This Python package links to Criteo production environment. Any test applied here will thus impact real campaigns.

## Requirements.

Python 2.7 and 3.5+

## Installation & Usage
### pip install


```sh
pip install criteo_marketing
```
(you may need to run `pip` with root permission: `sudo pip install criteo_marketing`)

Then import the package:
```python
import criteo_marketing
```

Full documentation on [Github](https://github.com/criteo/criteo-python-marketing-sdk).

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

setup(
    name=NAME,
    version=VERSION,
    description="Marketing API v.1.0",
    author_email="",
    author=AUTHOR,
    url="https://github.com/criteo/criteo-python-marketing-sdk",
    keywords=[AUTHOR, "OpenAPI-Generator", "Marketing API v.1.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type=README_CONTENT_TYPE,
    long_description=PACKAGE_LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
)
