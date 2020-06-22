#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import setuptools
from setuptools.command.build_py import build_py

NAME = "skulk"
DESCRIPTION = "Streamline release for Conductor client tools and others"
URL = "https://github.com/AtomicConductor/skulk"
EMAIL = "julian@conductortech.com"
AUTHOR = "Julian Mann"
REQUIRES_PYTHON = "~=2.7"
REQUIRED = ["GitPython==2.1.15"]
HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'VERSION')) as version_file:
    VERSION = version_file.read().strip()

class BuildCommand(build_py):
    def run(self):
        build_py.run(self)
        if not self.dry_run:
            target_dir = os.path.join(self.build_lib, NAME)
            with open(os.path.join(target_dir, "VERSION"), "w") as f:
                f.write(VERSION)
 
setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python"
    ],
    cmdclass={"build_py": BuildCommand},
    description=DESCRIPTION,
    entry_points={"console_scripts": ["skulk=skulk.skulk:main"]},
    include_package_data=True,
    install_requires=REQUIRED,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    name=NAME,
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=REQUIRES_PYTHON,
    url=URL,
    version=VERSION,
    zip_safe=False
)
