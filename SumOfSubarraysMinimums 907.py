# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:24:52 2019

@author: haimingwd
"""

## Sum of subarrays minimums 907
def sumSubarrayMins(A):        
    res = 0
    A = [float('-inf')] + A + [float('-inf')]
    stack = []  #  only keep index of non-decreasing numbers in A
    for i, n in enumerate(A):
        while stack and A[stack[-1]] > n:
            cur = stack.pop()
            res += A[cur] * (i - cur) * (cur - stack[-1]) 
        stack.append(i)
    return res % (10**9 + 7)
sumSubarrayMins([3,1,2,4]) 