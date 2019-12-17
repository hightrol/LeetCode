# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:16:34 2019

@author: haimingwd
"""

## Longest Turbulent Subarray 978
def maxTurbulenceSize(A):
    A = [A[0]] * 2 + A
    n = len(A)
    length, maxLen = 1, 1
    for i in range(2, n):
        if A[i-1] == A[i]:
            length = 1
        elif (A[i] - A[i-1]) * (A[i-1] - A[i-2]) > 0:
            length = 2
        else:
            length += 1
        maxLen = max(maxLen, length)
    return maxLen

maxTurbulenceSize([9,4,2,10,7,8,8,1,9])
