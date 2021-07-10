from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in itam/__init__.py
from itam import __version__ as version

setup(
	name='itam',
	version=version,
	description='IT asset management (also known as ITAM) is the process of ensuring an organization’s assets are accounted for, deployed, maintained, upgraded, and disposed of when the time comes.',
	author='Res-IT Solutions Ltd.',
	author_email='support@res-it.solutions',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
