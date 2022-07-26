import os
from ctypes import *
import ctypes.util
from binascii import unhexlify

def print_hex(data):
    for i in range(0, len(data), 16):
        print("{:08x} ".format(i), end="")
        print(" ".join(data[i:i+8]), end="  ")
        print(" ".join(data[i+8:i+16]), end="  ")
        #print(bytes.fromhex("".join(data[i:i+16])).decode("ascii", "ignore"))
        print(unhexlify("".join(data[i:i+16])).decode("utf-8", "replace"))

def cprint_hex(data):
    libc = CDLL(ctypes.util.find_library("c"))
    for i in range(0, len(data), 16):
        libc.printf(b"%08x ", i)
        libc.printf(b"%s  %s  |%s|\n", bytes(" ".join(data[i:i+8]), "ascii"), bytes(" ".join(data[i+8:i+16]), "ascii"), bytes(repr(unhexlify("".join(data[i:i+16])).decode("utf-8", "replace")), "utf-8"))

path = ("bintest.bin")
path = os.path.expanduser(path)

with open(path, "rb") as f:
    raw = f.read().hex()
    split = [raw[i:i+2] for i in range(0, len(raw), 2)]
    cprint_hex(split)