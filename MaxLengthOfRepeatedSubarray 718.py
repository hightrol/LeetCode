# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:37:35 2019

@author: haimingwd
"""

def findLength(A, B):
    m, n = len(A), len(B)
    dp = [ 1 if A[-1] == B[j] else 0 for j in range(n) ]
    maxVal = 0
    for i in range(m-2, -1, -1):
        dp = [ 1 + dp[j+1] if A[i] == B[j] else 0 for j in range(n-1) ] + [ 1 if A[i] == B[-1] else 0 ]
        maxVal = max(maxVal, max(dp))
    return maxVal