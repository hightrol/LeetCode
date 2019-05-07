# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:30:16 2019

@author: haimingwd
"""

def minScoreTriangulation(A):
    n = len(A)
    res = [ [0 for _ in range(n)] for _ in range(n) ]
    def dp(s, e):
        if res[s][e] > 0:
            return res[s][e]
        if e-s == 2:
            res[s][e] = A[s]*A[s+1]*A[e]
        elif e-s > 2:
            res[s][e] = min( [ A[s]*A[e]*A[k] + dp(s, k) + dp(k, e) for k in range(s+1, e) ] )   
        return res[s][e]
    return dp(0, n-1)

minScoreTriangulation([1,3,1,4,1,5])