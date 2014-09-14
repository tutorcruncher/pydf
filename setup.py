#!/usr/bin/python

import os, re

from setuptools import setup

description = 'PDF generation in python using wkhtmltopdf suitable for heroku'

setup(
    name='pydf',
    version='0.1',
    description=description,
    author='Samuel Colvin',
    license='MIT',
    author_email='S@muelColvin.com',
    url='https://github.com/samuelcolvin/pydf',
    packages=['pydf'],
    platforms='any',
    package_data={'pydf': ['bin/wkhtmltopdf*']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    test_suite='tests',
    zip_safe=False
)