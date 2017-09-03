Serial monitor
==============

Serial monitor is a simple serial port monitor for linux.

For python2 and 3.

Get started
-----------

```bash
$ pip install git+https://github.com/boarnasia/serial_monitor
$ python -m serial_monitor -p /dev/serial0 -b 9600
$ python -m serial_monitor -p /dev/ttyS0
Message 1
Message 2
Message 3
Message 4
Message 5
^C

====
Stop, because of keyboard interruption.
```

