#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: ride
"""

def letter_to_num(l):
    return ord(l) - ord("A") + 1

def letter_prod(s):
    n = 1
    for l in s:
        n = n*letter_to_num(l)
    return n

with open("ride.in", "r") as f:
    x = f.read()
    comet, group = x.strip().split("\n")

with open("ride.out", "w") as f:
    if letter_prod(comet)%47 == letter_prod(group)%47:
        f.write("GO\n")
    else:
        f.write("STAY\n")
