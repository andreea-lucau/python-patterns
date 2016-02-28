#!/usr/bin/env python
import distutils.cmd


import setuptools.command.build_py
from setuptools import setup, find_packages


class BuildWithLintCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):
        self.run_command('lint')
        setuptools.command.build_py.build_py.run(self)


setup(
    name="python-patterns",
    version="1.0",
    description="Sample degisn patterns used in Python",
    author="Andreea Lucau",
    author_email="andreea.lucau@gmail.com",
    url="https://github.com/andreea-lucau/python-patterns",
    packages=find_packages("src"),
    package_dir = {
        "": "src",
    },
    install_requires=[
        "psutil",
        "setuptools",
        "setuptools-lint",
    ],
    cmdclass={
        'build_py': BuildWithLintCommand,
    },
)
