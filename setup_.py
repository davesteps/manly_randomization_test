import unittest

from setuptools import setup

def test_suite():
   test_loader = unittest.TestLoader()
   test_suite = test_loader.discover('tests', pattern='test_*.py')
   return test_suite

setup(
   name='manly_randomization_test',
   version='0.1',
   description='A python implementation of Manly randomization test ',
   author='David Stephens',
   author_email='davesteps@gmail.com',
   packages=['manly_randomization_test'],  #same as name
   install_requires=['numpy'],  # any additional packages that
   url='https://github.com/davesteps/manly_randomization_test',
   license='Apache-2.0',
   test_suite='setup.test_suite',
)