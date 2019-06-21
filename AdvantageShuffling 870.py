# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:00:41 2019

@author: haimingwd
"""

def advantageCount(A, B):
    n = len(A)
    A.sort()
    B_ix = sorted(range(n), key = lambda ea:B[ea])
    n = len(A)
    j, k = 0, n-1
    C = [ 0 for _ in range(n) ]
    for i in range(n):
        if A[i] > B[B_ix[j]]:
            C[B_ix[j]] = A[i]
            j += 1
        else:
            C[B_ix[k]] = A[i]
            k -= 1
    return C