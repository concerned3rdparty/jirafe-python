#!/usr/bin/env python

import setuptools

setup_params = dict(
    name='jirafe',
    version="2.-",
    description='Jirafe API for Python',
    author='Jirafe',
    author_email='systems@jirafe.com',
    url='https://docs.jirafe.com',
    packages=setuptools.find_packages(),
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
