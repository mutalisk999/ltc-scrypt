#!/usr/bin/env python
# encoding: utf-8


__author__ = 'mutalisk'

from setuptools import setup
from distutils.extension import Extension

ext_modules = [Extension("ltc_scrypt", ["scryptmodule.cpp", "scrypt.cpp"],
    language="c++",
    define_macros=[],
    include_dirs=["."],
    library_dirs=["pywrapper-dependence/lib64-win"],
    libraries=["python27"]
    )]

setup(name='ltc_scrypt',
    version='0.1.0',
    description='Python Wrapper of Litecoin Scrypt Algo',
    author='',
    author_email='',
    url='https://github.com/mutalisk999/ltc_scrypt',
    platforms='win',
    packages=[],
    install_requires=["setuptools"],
    zip_safe=False,
    ext_modules = ext_modules,
    )
