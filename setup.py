"""Minimal setup file for route planner project"""

from setuptools import setup, find_packages

setup(
    name='route planner',
    version='1.0.0',
    description='Finds the shortest path between the two given points on the map',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['routeplanner=routeplanner.cli:main'],
    },

    # metadata
    author='Yuriy Jurayev',
    author_email='',
    license='proprietary',
    install_requires=['pytest', 'networkx', 'pytest-html', 'pytest-cov', 'coverage']
)