#!/usr/bin/env python3

from setuptools import setup

setup(
    name='BiscuIT-App-Untis',
    version='1.0dev0',
    url='https://edugit.org/Teckids/BiscuIT/BiscuIT-App-Untis',
    author="Teckids e.V.",
    author_email="verein@teckids.org",
    packages=[
        'biscuit.apps.untis',
        'biscuit.apps.untis.management.commands'
    ],
    namespace_packages=[
        'biscuit',
        'biscuit.apps'
    ],
    include_package_data=True,
    install_requires=[
        'BiscuIT-ng',
        'BiscuIT-App-Chronos',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
    ],
)
