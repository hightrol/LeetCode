# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:23:34 2019

@author: haimingwd
"""

def maxProfit(k, prices):
    n = len(prices)
    if n <= 1:
        return 0
    ret = [ prices[i+1] - prices[i] for i in range(n-1) ] 
    if k >= n/2:
        return sum([max(ea,0) for ea in ret])
    def helper(k):
        if k == 0:
            return [ 0 for _ in range(n) ]
        res1 = helper(k-1)
        res3 = [ 0 for _ in range(n) ]
        res2, res3[1] = ret[0], max(ret[0], 0)
        for i in range(1, n-1):
            res2 = max( res2 + ret[i], res1[i-1] + ret[i] )
            res3[i+1] = max(res3[i], res2)
        return res3
    return helper(k)[-1]

maxProfit(2, [1,3,4,6,2,9,2,4,6])
