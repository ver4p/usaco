#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: milk
"""

with open("milk.in", "r") as f:
    data = [[int(x) for x in line.strip().split()] for line in f.readlines()]

a, n = data[0]      # units of required milk, number of potential farmers
farmers = data[1:]  # n farmers, characterised by price/unit, available units
farmers.sort()

b = 0               # units of milk already bought
c = 0               # costs for milk

if len(farmers) != 0:          # checking if MMM buys milk from farmers
    for p, u in farmers:
        if b+u < a:
            c += u*p
            b += u
        else:
            c += (a-b)*p
            b += (a-b)
            break

with open("milk.out", "w") as f:
    f.write("{}\n".format(c))
