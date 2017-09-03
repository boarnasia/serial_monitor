# -*- coding: utf-8 -*-

import serial
from argparse import ArgumentParser as BaseParser

__version__ = "0.0.1"

class SerialMonitor:
    def __init__(self):
        self.fin = None
        self.args = self._parse_argument()

        self.open()

    def _parse_argument(self):
        parser = ArgumentParser()
        return parser.parse_args()

    def open(self):
        self.fin = serial.Serial(self.args.port.name, self.args.baudrate,
                                 timeout=self.args.timeout)
        self.fin.readline() # Abandon first line, because it will contain faulty data.

    def loop(self):
        try:
            sentence = self.fin.readline().decode('utf-8')
            print(sentence.rstrip())

        except UnicodeDecodeError as e:
            pass

    def run(self):
        try:
            while True:
                self.loop()

        except KeyboardInterrupt as e:
            print("\n")
            print("====")
            print("Stop, because of keyboard interruption.")
            print("")

    def close(self):
        if self.fin != None:
            self.fin.close()

        self.fin = None

    def __del__(self):
        self.close()


class ArgumentParser(BaseParser):
    def __init__(self):
        super(ArgumentParser, self).__init__(
            description="Serial port monitor."
        )
        self.add_argument('-v', '--version', action="version", help="Show version.",
                          version="%(prog)s {}".format( __version__))
        self.add_argument('-p', '--port', action="store", type=open, default='/dev/serial0',
                          help="name of the device port")
        self.add_argument('-b', '--baudrate', action="store", type=int, default=9600,
                          help="baud rate")
        self.add_argument('-t', '--timeout', action="store", type=int, default=10,
                          help="timeout")

