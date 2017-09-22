#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='{{ cookiecutter.app_name }}',
    version='0.0.1',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    license='{{ cookiecutter.license }}',
    packages=find_packages(
        exclude=['docs', 'tests', 'android']
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: {{ cookiecutter.license }}',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': '{{ cookiecutter.formal_name }}',
            'bundle': '{{ cookiecutter.bundle }}'
        },
    }
)
