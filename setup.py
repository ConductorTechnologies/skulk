#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import setuptools

NAME = "skulk"
DESCRIPTION = "Streamline release for Conductor client tools and others"
URL = "https://github.com/AtomicConductor/skulk"
EMAIL = "julian@conductortech.com"
AUTHOR = "Julian Mann"
REQUIRES_PYTHON = "~=2.7"
REQUIRED = ["GitPython==2.1.15"]
HERE = os.path.abspath(os.path.dirname(__file__))
SLUG = NAME.lower().replace("-", "_").replace(" ", "_").replace(".", os.sep)

with open(os.path.join(HERE, "src", SLUG, "__version__.py")) as vf:
    for line in vf:
        match = re.compile(
            r"^__version__.*=(?:[\s\"']+)(.*)(?:[\s\"'])$").match(line.strip())
        if match:
            VERSION = match.group(1)
            break

setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python"
    ],
    description=DESCRIPTION,
    entry_points={"console_scripts": ["skulk=skulk.skulk:main"]},
    include_package_data=True,
    install_requires=REQUIRED,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    name=NAME,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=REQUIRES_PYTHON,
    url=URL,
    version=VERSION,
    zip_safe=False
)
