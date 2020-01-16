#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'msj', getattr(magic_string, 'msj', 0) + 1)
    return ", ".join(["Holberton"] * magic_string.msj)
