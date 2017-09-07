import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('serial_monitor/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('readme.md', 'r') as f:
    long_description = f.read()

setup(
    name    = "Serial monitor",
    version = version,
    url = 'https://github.com/boarnasia/serial_monitor/',
    description = 'Simple serial port monitor for linux',
    long_description = long_description,
    install_requires = [
        'pyserial',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

