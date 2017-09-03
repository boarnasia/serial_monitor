"""
Serial monitor
==============

Serial monitor is a simple serial port monitor for linux.

Get started
-----------

```bash
$ pip install git+https://github.com/boarnasia/serial_monitor
$ python -m serial_monitor -p /dev/serial0 -b 9600
Message 1
Message 2
Message 3
Message 4
Message 5
^C

====
Stop, because of keyboard interruption.
```
"""

import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('serial_monitor/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name    = "Serial monitor",
    version = version,
    url = 'https://github.com/boarnasia/serial_monitor/',
    description = 'Simple serial port monitor for linux',
    long_description = __doc__,
    install_requires = [
        'pyserial',
    ],
)

