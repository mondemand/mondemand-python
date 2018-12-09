#!/usr/bin/env python

from setuptools import setup

setup(
	use_scm_version=True,
	cffi_modules=['mondemand_build.py:ffibuilder']
)
