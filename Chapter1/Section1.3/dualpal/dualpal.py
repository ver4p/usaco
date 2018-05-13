#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: dualpal
"""

def baseB(x, B):
    s = ""
    while x > 0:
        s += str(x % B)
        x //=B
    return s

def is_palindrome(s):
    return s == s[::-1]

with open("dualpal.in", "r") as f:
    n, s = [int(x) for x in f.read().strip().split()]
    

pals = []

while len(pals) < n:
    s += 1
    c = 0
    for b in range(2,11):
        if is_palindrome(baseB(s, b)):
            if c == 1:
                pals.append(s)
                break
            c += 1

with open("dualpal.out", "w") as f:
    for pal in pals:
        f.write(str(pal))
        f.write("\n")
