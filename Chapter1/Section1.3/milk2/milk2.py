#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: milk2
"""

with open("milk2.in", "r") as f:
    data = f.read().strip().split('\n')
    N, intervals = int(data[0]), data[1:]
    intervals = [x.split() for x in intervals]
    intervals = [[int(x) for x in y] for y in intervals]


ends = list(zip(*intervals))[1]

secs = [0]*(max(ends)+1)
for pair in intervals:
    secs[pair[0]+1:pair[1]+1] = [1]*(pair[1]-pair[0])
    
    
I = [k for k in range(0,len(secs)-1) if secs[k] == 0 and secs[k+1] == 1 or secs[k] == 1 and secs[k+1] == 0]
I += [max(ends)]

I1 = [I[k]-I[k-1] for k in range(1,len(I)) if k%2==1]
I2 = [I[k]-I[k-1] for k in range(1,len(I)) if k%2==0]

milking = max(I1)
if len(I2) != 0:
    idle = max(I2)
else:
    idle = 0

with open("milk2.out", "w") as f:
    f.write("{0} {1}\n".format(milking, idle))
