# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:49:19 2019

@author: haimingwd
"""

def monotoneIncreasingDigits(N):
    nStr = str(N)
    n = len(nStr)
    if n == 1:
        return N
    i = 1
    while i < n:
        if nStr[i] < nStr[i-1]:
            break
        else:
            i += 1
    if i == n:
        return N
    else:
        M0 = monotoneIncreasingDigits( int(nStr[:i])-1 )
        M1 = int('9'*(n-i) if i != n else 0)
    return 10**(n-i)*M0 + M1    