# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:53:28 2019

@author: haimingwd
"""

def lastStoneWeightII(stones):
    weights = {stones[0]}
    n = len(stones)
    for i in range(1, n):
        la = [ abs(ea - stones[i]) for ea in weights ]
        lb = [ abs(ea + stones[i]) for ea in weights ]
        weights = set( la + lb )
    return min(weights)
