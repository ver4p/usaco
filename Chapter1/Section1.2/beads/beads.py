#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: beads
"""

with open("beads.in", "r") as f:
    n = int(f.readline())
    chain = f.readline()

def number_of_beads(j, inc, lmax):
    
    # ignores whites and sets color
    l = 0
    while l < lmax:
        if chain[(j+inc*l+n)%n] != 'w':
            c = chain[(j+inc*l+n)%n]
            break
        if l == lmax - 1:
            return n
        l += 1
    
    # counts beads of same color
    l = 0
    r = 0
    while l < lmax:
        if chain[(j+inc*l+n)%n] in {c, 'w'}:
            r += 1
        else:
            break
        l += 1
    
    return r

# counts beats of same color or white in each direction and stores longest segment
segment = 0
for k in range(n):
    l1 = number_of_beads(k, 1, n)
    l2 = number_of_beads(k-1, -1, n-l1)
    segment = max(segment, l1+l2)

with open("beads.out", "w") as f:
    f.write("{}\n".format(segment))
