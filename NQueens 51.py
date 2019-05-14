# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:48:59 2019

@author: haimingwd
"""

def solveNQueens(n):
        
    def helper(y, xyDiff, xySum):
        m = len(y)
        if m == n:
            res.append(y)
            return
        for i in range(n):
            if (i not in y) and (i-m not in xyDiff) and (i+m not in xySum):
                helper( y+[i], xyDiff + [i-m], xySum + [i+m] )
    
    def decode(code):
        return [ '.'*ea + 'Q' + '.'*(n-ea-1) for ea in code ]
                
    res = []
    helper([], [], [])
    return [decode(ea) for ea in res]

solveNQueens(6)

    