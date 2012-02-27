#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-oklinks',
    version='0.1',
    description='A simple bookmarking app for Django.',
    author='Benny Daon',
    author_email='bennydaon@gmail.com',
    url='https://daonb@github.com/daonb/django-oklinks.git',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'oklinks',
        'oklinks.management',
        'oklinks.management.commands',
        'oklinks.templatetags',
    ],
    include_package_data=True,
    requires=[ 'django_tastypie', ],
    install_requires=[ 'django_tastypie', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
