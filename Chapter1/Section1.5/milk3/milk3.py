#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: milk3
"""

with open("milk3.in", "r") as f:
    
    #capacities of buckets
    A, B, C = [int(x) for x in f.readline().strip().split()]

s = []              #contains processed combinations of filling levels
q = [[0, 0, C]]     #contains initial combination of filling levels
                    #all possible combinations will be added to q
                    

while len(q) != 0:
    u = q.pop(0)    #provides next combination and removes it from q

    if u not in s:  #checks whether combination has already been treated
        s.append(u)
    
        x, y, z = u
        
        #computes next possible combination of filling levels starting from u
        q.append([x - min(x, B-y), y + min(x, B-y), z])
        q.append([x - min(x, C-z), y, z + min(x, C-z)])
        q.append([x + min(y, A-x), y - min(y, A-x), z])
        q.append([x, y - min(y, C-z), z + min(y, C-z)])
        q.append([x + min(z, A-x), y, z - min(z, A-x)])
        q.append([x, y + min(z, B-y), z - min(z, B-y)])

r = [z for x, y, z in s if x==0]    #keeps filling level C if A is empty
r.sort()

with open("milk3.out", "w") as f:
    f.write(" ".join(map(str, r))+"\n")
    