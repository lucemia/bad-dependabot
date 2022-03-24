#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup for speech to text."""


from setuptools import setup, find_packages

setup(
    name='genv-studio',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['genv-queue'],
    packages=find_packages('client'),
    package_dir={'': 'client'},
    zip_safe=False,
)
