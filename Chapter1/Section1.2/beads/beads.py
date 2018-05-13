#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ID: vera.po1
LANG: PYTHON3
TASK: beads
"""
#with open("beads.in", "r") as f:
#    n, chain = f.read().split()
#    n = int(n)
#
#def number_of_beads(j, inc, lmax):
#    
#    #ignores whites and sets color
#    l = 0
#    while l<lmax:
#        if chain[(j+inc*l+n)%n] != "w":
#            c = chain[(j+inc*l+n)%n]
#            break
#        if l == lmax-1:
#            return n
#        l += 1
#        
#    #counts number of c- or w-beads
#    q = 0
#    while l<lmax:
#        if chain[(j+inc*l+n)%n] == c:
#            q+=1
#        elif chain[(j+inc*l+n)%n] == "w":
#            q+=1
#        else:
#            break
#        l += 1
#    
#    return q
#
#m = 0 
#for j in range(n):
#    l1 = number_of_beads(j,1,n)
#    l2 = number_of_beads((j-1+n)%n,-1,n-l1)
#    m = max(l1+l2, m)
#
#def main():
#    print(m)
#
#main()

def parts(nl):
    N = len(nl)
    s = ''
    
    for b in range(N):
        if nl[b] != "w":
            color = nl[b]
            break
    
    for b in range(N):
        if nl[b] == "w":
            s += nl[b]
        elif nl[b] == color:
            s += nl[b]
        else:
            break
    
    return s

with open("beads.in", "r") as f:
    N, necklace = f.read().split() 

necklace += parts(necklace)

len_parts = []
p = 0
while p < len(necklace):
    n = len(parts(necklace[p:]))
    len_parts.append(n)
    p += n

if len(len_parts) == 1:
    m = N
    
else:
    len_2parts = [len_parts[j] + len_parts[j+1] for j in range(len(len_parts) - 1)]
    m = max(len_2parts)
    
    if len(len_2parts) > 2:
        m_pos = [j for j in range(len(len_2parts)) if len_2parts[j] == m]
        m_w = []
        for j in m_pos:
            m_j = m
            n = sum(len_parts[:j])
            for k in range(n):
                if necklace[n-1-k] == "w":
                    m_j += 1
                else:
                    break
            m_w.append(m_j)
        
        m = max(m_w)

with open("beads.out", "w") as f:
    f.write("{0}\n".format(m))
