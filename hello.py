#!/usr/bin/env python3

"""
Print an uppercased arg

How to use:
$ ./hello.py <arg>


"""
__version__ = "0.1.0"
__author__ = "Rafael Z Tanganelli"

import sys

arguments = sys.argv[1:]

for arg in arguments:
    print(f"{arg.upper()}")


