#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: skidesign
"""

with open("skidesign.in", "r") as f:
    n = int(f.readline())                   #number of hills
    h = [int(x) for x in f.readlines()]     #elevation of each hill
    
h.sort()
hmin = h[0]                                 #lowest altitude
hmax = h[-1]                                #highest altitude
dmax = hmax-hmin

#calculates costs to change hills in order to have them in the intervall [h1, h2]
def calculate_costs(h1, h2, h):
    lower = [(x-h1)**2 for x in h if x<h1]
    higher = [(x-h2)**2 for x in h if x>h2]
    return sum(lower) + sum(higher)

#computes costs to have hills in [hmin, hmin+17], [hmin+1, hmin-16],... [hmax-17, hmax]
#and finds minimum
o = min([calculate_costs(k, k+17, h) for k in range(hmin, hmax - 17)]) if hmax-hmin > 17 else 0

with open("skidesign.out", "w") as f:
    f.write("{}\n".format(o))
