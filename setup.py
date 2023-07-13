# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='jsonschema',
    version='4.18.1',
    description='An implementation of JSON Schema validation for Python',
    author='Julian Berman',
    author_email='Julian+jsonschema@GrayVines.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: File Formats :: JSON',
        'Topic :: File Formats :: JSON :: JSON Schema',
    ],
    install_requires=[
        'attrs>=22.2.0',
        'importlib-resources>=1.4.0; python_version < "3.9"',
        'jsonschema-specifications>=2023.03.6',
        'pkgutil-resolve-name>=1.3.10; python_version < "3.9"',
        'referencing>=0.28.4',
        'rpds-py>=0.7.1',
    ],
    extras_require={
        'format': [
            'fqdn',
            'idna',
            'isoduration',
            'jsonpointer>1.13',
            'rfc3339-validator',
            'rfc3987',
            'uri-template',
            'webcolors>=1.11',
        ],
        'format-nongpl': [
            'fqdn',
            'idna',
            'isoduration',
            'jsonpointer>1.13',
            'rfc3339-validator',
            'rfc3986-validator>0.1.0',
            'uri-template',
            'webcolors>=1.11',
        ],
    },
    entry_points={
        'console_scripts': [
            'jsonschema = jsonschema.cli:main',
        ],
    },
    packages=[
        'jsonschema',
    ],
)
