from setuptools import find_packages
from setuptools import setup

setup(
    name='autorccar_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('autorccar_interfaces', 'autorccar_interfaces.*')),
)
