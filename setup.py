#!/usr/bin/env python
#-*- coding: utf-8 -*-
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = cythonize(
    [Extension(
            "nbio",
            ["nbio.c"],
            extra_link_args=['lib/libNBioBSP.so'],
        )
    ]
)

setup(name="nbio", version="1.1", ext_modules=exts)
