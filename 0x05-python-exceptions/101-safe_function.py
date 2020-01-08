#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as msj:
        print("Exception: {}". format(msj), file=sys.stderr)
