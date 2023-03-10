#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Lightsong",
    author_email='qsfan@qq.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Copy tables and their data from one db to another db.",
    entry_points={
        'console_scripts': [
            'sqlalchemy_tables_copier=sqlalchemy_tables_copier.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sqlalchemy_tables_copier',
    name='sqlalchemy_tables_copier',
    packages=find_packages(include=['sqlalchemy_tables_copier', 'sqlalchemy_tables_copier.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/fanqingsong/sqlalchemy_tables_copier',
    version='0.1.1',
    zip_safe=False,
)
