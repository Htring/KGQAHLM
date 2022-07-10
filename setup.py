#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: juzipi
@file: setup.py
@time:2022/07/10
@description:
"""

from setuptools import find_packages, setup

setup(
    name='kgqahlm',
    version='1.0.0',
    author='juzipi',
    url='https://piqiandong.blog.csdn.net/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'jieba',
        'py2neo'
    ],
)

