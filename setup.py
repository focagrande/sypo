#!/usr/bin/env python

from __future__ import print_function

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(name='Sypo',
      version='1.0',
      description='Simple But Possible Organism',
      author='Jacek Spiewak',
      tests_require=['pytest'],
      author_email='jacek.spiewak@gmail.com',
      url='https://github.com/focagrande/sypo',
      packages=['sypo'],
      cmdclass={'test': PyTest},
      extras_require={
         'testing': ['pytest'],
      }
    )
