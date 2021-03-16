#!/usr/bin/python3

import sys

input_str = sys.argv[1]
output_str = ''

for c in input_str:
    o = hex(ord(c))
    output_str += o.replace('0x', '\\x')

print(output_str)
