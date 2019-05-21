#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["pyaml"]

setup_requirements = [ ]

test_requirements = []

setup(
    author="Joakim Hove",
    author_email='joakim.hove@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Small package to run django manage commands through cron",
    scripts=["bin/django-cron"],
    install_requires=requirements,
    license="GNU General Public License v3",
    include_package_data=True,
    keywords='django_cron',
    name='django_cron',
    packages=find_packages(include=['django_cron']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/joakim-hove/django_cron',
    version='0.1.0',
    zip_safe=False,
)
