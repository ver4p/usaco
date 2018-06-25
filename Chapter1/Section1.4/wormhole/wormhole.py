#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: wormhole
"""

with open("wormhole.in", "r") as f:
    n = int(f.readline())                                           #total number of wormholes
    wh = [[int(x) for x in line.split()] for line in f.readlines()] #coordinates of wormholes

#labels wormholes with numbers
wh_num = list(range(n))

#returns all possible pairings of wormholes, labelling wormholes with numbers
def get_all_pairings(w_num, p = [], r = []):
    if w_num == []:
        r.append(p)
    else:
        for k in range(1,len(w_num)):
            get_all_pairings(w_num[1:k]+w_num[k+1:], p+[[w_num[0], w_num[k]]], r)
    return r

#finds next wormhole starting at coordinates x and
#returns number of next wormhole or -1 if next wormhole does not exist
def get_next_wormhole(x, w):
    next_wh = [float('Inf'), float('Inf')]
    next_wh_index = -1
    
    for k in range(len(w)):
        if w[k][1] == x[1] and w[k][0] > x[0]:
            if w[k][0] < next_wh[0]:
                next_wh = w[k]
                next_wh_index = k
                
    return next_wh_index

#checks whether a pairing contains a loop
def has_loop(pairing, w):
    for starter in w:
        x = starter
        k = get_next_wormhole(x, w)
        while k != -1:
            for j in range(len(pairing)):
                if pairing[j][0] == k:
                    x = w[pairing[j][1]]
                    break
                if pairing[j][1] == k:
                    x = w[pairing[j][0]]
                    break
            if x == starter:
                return True
            k = get_next_wormhole(x, w)
    return False

#counts number of pairings containing loops
o = len([p for p in get_all_pairings(wh_num) if has_loop(p, wh)])
with open("wormhole.out", "w") as f:
    f.write("{}\n".format(o))
