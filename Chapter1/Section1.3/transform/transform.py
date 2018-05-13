#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: transform
"""

#def print_mat(A):
#    print("\n".join(A))

#def identity(A):
#    N = len(A)
#    return [[A[j][k] for k in range(N)] for j in range(N)]

def rot(A):
    N = len(A)
    return ["".join([A[N-(k+1)][j] for k in range(N)]) for j in range(N)]

def reflection(A):
    N = len(A)
    return ["".join([A[j][N-(k+1)] for k in range(N)]) for j in range(N)]

with open("transform.in", "r") as f:
    data = f.read().strip().split("\n")
    N = int(data[0])
    A, B = data[1:N+1], data[N+1:2*N+1]

if rot(A) == B:
    o = 1
elif rot(rot(A)) == B:
    o = 2
elif rot(rot(rot(A))) == B:
    o = 3
elif reflection(A) == B:
    o = 4
elif reflection(rot(A)) == B:
    o = 5
elif reflection(rot(rot(A))) == B:
    o = 5
elif reflection(rot(rot(rot(A)))) == B:
    o = 5
elif A == B:
    o = 6
else:
    o = 7

with open("transform.out", "w") as f:
    f.write("{0}\n".format(o))
