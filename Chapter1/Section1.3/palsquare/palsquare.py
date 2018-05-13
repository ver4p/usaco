#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: palsquare
"""

def baseB(x, B):
    s = ""
    while x > 0:
        y = x % B
        s = (str(y) if y < 10 else chr((y-10) + ord("A"))) + s
        x //=B
    return s

def is_palindrome(s):
    return s == s[::-1]


with open("palsquare.in", "r") as f:
    B = int(f.read())
    
with open("palsquare.out", "w") as f:
    for n in range(1, 301):
        x2 = baseB(n*n, B)
        if is_palindrome(x2):
            x = baseB(n, B)
            f.write("{} {}\n".format(x, x2))
