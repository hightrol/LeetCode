# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:04:06 2019

@author: haimingwd
"""

## Partition Array into Disjoint Intervals 915
def partitionDisjoint(self, A):
    n = len(A)
    minAfter = [ A[i] for i in range(n) ]
    for i in range(n-2, -1, -1):
        minAfter[i] = min(minAfter[i+1], A[i])
    #print(minAfter)
    maxBefore = float('-inf')
    for i in range(n-1):
        maxBefore = max(A[i], maxBefore)
        if maxBefore <= minAfter[i+1]:
            return i+1    