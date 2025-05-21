# -*- coding: utf-8 -*-
"""
    Setup file for smecv-grid.
"""
import sys
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="smecv-grid",
        version="0.3",  # Use appropriate version number 
        description="SMECV grid definition and resampling",
        author="TU Wien",
        author_email="remote.sensing@geo.tuwien.ac.at",
        license="MIT",
        url="https://github.com/daberer/smecv-grid",
        packages=find_packages(),
        install_requires=[
            "numpy",
            "netCDF4",
            "pykdtree",
            "configparser",
            "pygeogrids",
            "pyproj",
            "more_itertools",
            # Add any other required dependencies
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python",
        ],
    )
