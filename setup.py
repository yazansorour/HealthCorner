# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in health_corner/__init__.py
from health_corner import __version__ as version

setup(
	name='health_corner',
	version=version,
	description='Health Corner Services will handle client sub',
	author='Yazan',
	author_email='yazansorour1@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
