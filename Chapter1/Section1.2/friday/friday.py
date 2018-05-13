#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: friday
"""

def is_leap_year(y):
    if y%400 == 0:
        return True
    elif y%100 == 0:
        return False
    elif y%4 == 0:
        return True
    else:
        return False
    
with open("friday.in", "r") as f:
    N = int(f.read().strip())
    
occurance = [0]*7
p = 0

for y in range(1900, 1900 + N):
    for m in range(1,13):
        p %= 7
        occurance[p] += 1
        if m in {1, 3, 5, 7, 8, 10, 12}:
            p += 31%7
        elif m in {4, 6, 9, 11}:
            p += 30%7
        elif m == 2 and is_leap_year(y):
            p += 29%7
        else:
            p += 28%7

with open("friday.out", "w") as f:
    f.write(" ".join([str(n) for n in occurance]) + "\n")
