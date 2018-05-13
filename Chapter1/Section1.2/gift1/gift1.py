#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: gift1
"""

with open("gift1.in", "r") as f:
    x = [s.strip() for s in f.readlines()]

NP = int(x[0])
ppl = x[1:NP+1]

accounts = {name:0 for name in ppl}
p = NP + 1

while p < len(x):
    amount, n = [int(s) for s in x[p+1].split()]
    if n != 0:
        giver = x[p]
        accounts[giver] += -amount + amount%n 
        for name in x[p+2:p+2+n]:
            accounts[name] += int(amount/n)
    p += n+2 

with open("gift1.out", "w") as f:
    for name in ppl:
        f.write("{0} {1}\n".format(name, accounts[name]))
