#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: combo
"""
with open("combo.in", "r") as f:
    n = int(f.readline())                           # highest number in combination
    k = [int(x) for x in f.readline().split()]      # farmer's combination
    m = [int(x) for x in f.readline().split()]      # master combination

# returns a list in the inerval [x-2, x+2] with numbers from 1 to n,
# considering periodic boundary conditions
def range2(x):
    r = [(y+n)%n for y in range(x-2, x+3)]
    for k in range(len(r)):
        if r[k] == 0:
            r[k] = n
    return r
    
# creates all opening combinations
openers = [[x0, x1, x2] for x0 in range2(k[0]) for x1 in range2(k[1]) for x2 in range2(k[2])]
masters = [[x0, x1, x2] for x0 in range2(m[0]) for x1 in range2(m[1]) for x2 in range2(m[2])]
    
# discards redundant combinations
for master in masters:
    if master not in openers:
        openers += [master]

# treats cases for n <= 5 where all combinations are openers 
o = len(openers) if n > 5 else n**3
        
with open("combo.out", "w") as f:
    f.write("{}\n".format(o))
