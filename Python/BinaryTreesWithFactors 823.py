# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:33:30 2019

@author: haimingwd
"""

def numFactoredBinaryTrees(A):
    A.sort()
    headSum = {}
    for i in A:
        s = 1
        for j in headSum:
            if j > i ** 0.5:
                break
            if i % j == 0 and i//j in headSum:
                mul = 1 if i // j == j else 2
                s += mul * headSum[j] * headSum[i//j]                       
        headSum[i] = s
    return sum(headSum.values())

numFactoredBinaryTrees([2,3,4,5,6,7,8,9])
