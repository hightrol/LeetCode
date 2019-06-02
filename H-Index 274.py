# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:35:54 2019

@author: haimingwd
"""

def hIndex(citations):
    if not citations:
        return 0
    n = len(citations)
    l, r = 0, min(n, max(citations))
    while r-l >= 1:
        mid = (l+r+1)//2
        if sum([ea >= mid for ea in citations]) >= mid:
            l = mid
        else:
            r = mid-1
    return l

hIndex([1,2,3,4,2])
