#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: namenum
"""

with open("dict.txt", "r") as f:
    names = [name.strip() for name in f.readlines()]

char_to_digit = {
    'A':2, 'B':2, 'C':2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4, 'I':4,
    'J':5, 'K':5, 'L':5, 'M':6, 'N':6, 'O':6, 'P':7, 'R':7, 'S':7,
    'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9, 'Q':0, 'Z':0
}
    
def name_to_num(s):
    o = 0
    for c in s:
        o = 10*o + char_to_digit[c]
    return o

namenums = [name_to_num(name) for name in names]

with open("namenum.in", "r") as f:
    num = int(f.read().strip())

matches = [names[k] for k in range(len(namenums)) if namenums[k] == num]
if len(matches) == 0:
    matches = ["NONE"]

with open("namenum.out", "w") as f:
    for match in matches:
        f.write(match)
        f.write("\n")
