# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in metabase_ngse/__init__.py
from metabase_ngse import __version__ as version

setup(
	name='metabase_ngse',
	version=version,
	description='Metabase for Nandan GSE',
	author='firsterp',
	author_email='support@firsterp.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
