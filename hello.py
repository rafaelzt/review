#!/usr/bin/env python3

"""
Print an uppercased arg

How to use:
$ ./hello.py <arg>


"""
__version__ = "0.1.0"
__author__ = "Rafael Z Tanganelli"
__license__ = "Unlicense"

import sys
import os

arguments = sys.argv[1:]
language = os.getenv("LANG", "en_US.UTF-8")

language = language.split(".")[0]


msg = {
    "en_US": "Hello, world!",
    "pt_BR": "Olá, mundo!",
    "fr_FR":"Bon jour, monde",
    "it_IT":"Ciao, mondo!",
}


if arguments:
    for arg in arguments:
        print(f"{arg.upper()}")
else:
    print(f"{msg[language]}")

