from setuptools import setup, find_packages

setup(
    name='nominatim',
    version='0.90',
    description='Open MapQuest Nominatim client library',
    author='Austin Gabel',
    author_email='agabel@gmail.com',
    url='https://github.com/agabel/python-nominatim',
    packages=find_packages(),
    license='MIT License',
    install_requires=['simplejson >= 2.1.0',],
    keywords='nominatim, geocoder',
)