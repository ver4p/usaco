#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: skidesign
"""

with open("skidesign.in", "r") as f:
    n = int(f.readline())
    h = [int(x) for x in f.readlines()]
    
h.sort()
hmin = h[0]
hmax = h[-1]
dmax = hmax-hmin

def calculate_costs(hmin, hmax, h):
    lower = [(x-hmin)**2 for x in h if x<hmin]
    higher = [(x-hmax)**2 for x in h if x>hmax]
    return sum(lower) + sum(higher)

o = min([calculate_costs(k, k+17, h) for k in range(hmin, hmax - 17)]) if hmax-hmin > 17 else 0

with open("skidesign.out", "w") as f:
    f.write("{}\n".format(o))
