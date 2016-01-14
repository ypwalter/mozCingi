#!/usr/bin/env python
# -*- coding:utf-8 -*-

# from distutils.sysconfig import get_python_lib
from setuptools import setup, find_packages

# dependencies
with open('requirements.txt') as f:
    deps = f.read().splitlines()

#with open('./FuzzManager_requirements.txt') as b:
#    deps.extend(b.read().splitlines())


version = "0.1.0"


# main setup script
setup(
    name="mozCingi",
    version=version,
    description="Fuzzy testing runner",
    author="Mozilla Taiwan",
    author_email="tw-qa@mozilla.com",
    license="MPL",
    install_requires=deps,
    packages=find_packages(),
    package_data={'': ['conf/*.json']},
    entry_points={'console_scripts': ['cingi = mozCingi.mainRunner:main']},
    include_package_data=True,
    zip_safe=False
)
