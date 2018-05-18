#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: crypt1
"""

with open("crypt1.in", "r") as f:
    n = int(f.readline())
    digits = [int(x) for x in f.readline().strip().split()]

def are_allowed_digits(x, m):
    if x < int('1'*m) or x > int('9'*m):       # rejects numbers with other than
        return False                           # m digits
                    
    for d in str(x):                           # rejects numbers with digits other
                                               # than in list 'digits'
        if not int(d) in digits:
            return False
        
    return True
 
# all numbers with 3 digits and digits from list
factors = [x2*100+x1*10+x0 for x2 in digits for x1 in digits for x0 in digits]

o = 0

for factor in factors:
    
    for x0 in digits:
        p1 = factor*x0
        if are_allowed_digits(p1,3):           # checks conditions for 1st p.p.

            for x1 in digits:
                p2 = factor*x1
                if are_allowed_digits(p2,3):   # checks conditions for 2nd p.p.
                    
                    p = p1 + 10*p2
                    if are_allowed_digits(p,4):# checks conditions for product
                        o +=1                  # counts number of valid solutions

with open("crypt1.out", "w") as f:
    f.write("{}\n".format(o))
            