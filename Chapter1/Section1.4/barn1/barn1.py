#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: barn1
"""

with open("barn1.in", "r") as f:
    b, s, c = [int(x) for x in f.readline().split()] # max. number of boards,
                                                     # total number of stalls
                                                     # total number of cows
    o = [int(x) for x in f.readlines()]              # occupied stall numbers
    o.sort()

gaps = [o[k+1]-o[k]-1 for k in range(c-1)]           # number of empty stalls in
gaps.sort()                                          # between occupied stalls

blocked = o[-1]-o[0]+1                               # number of blocked stalls
                                                     # if just 1 board is used

for k in range(1, min(b,c)):
    blocked -= gaps[-k]                              # number of blocked stalls
                                                     # using b or the most c boards
    
with open("barn1.out", "w") as f:
    f.write("{}\n".format(blocked))
