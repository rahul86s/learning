# -*- coding: utf-8 -*-
"""
Created on Thu Feb 05 20:05:37 2015

@author: rahull.sharma
"""
""" ax+b
"""
from vec import Vec
from mat import Mat
execfile('mat.py')
def solve(a,b,c):
    return (c-b)/a

def addn(v,w):
    return [v[i]+w[i] for i in range(len(v))]
def list_dot(u,v):
    return sum([u[i]*v[i] for i in range(len(u))])

def tringular_solvw():
    print 20
    t=list_dot([1,2],[4,5])
    print t

def vec_test():
    t={('a','@'):1,('a','#'):2,('a','?'):3,('b','@'):4,('b','#'):5,('b','?'):6}
    print t
    return t

def identity(D):
    dictT = dict();    
    for i in D:
        for j in D:
            if i == j :
                dictT[(i,j)]=1
        else:
            dictT[(i,j)]=0
    return Mat((D,D), dictT)
        
a=Mat((('a', 'b'), ('a', 'b')), {('a', 'a'): 1, ('b', 'b'): 1})
print a
"""print Mat((D,D), {(if i==j: 1 else: 0 for i in range(len(D))) for j in range(len(D))})
"""