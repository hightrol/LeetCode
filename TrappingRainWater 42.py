# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:44:20 2019

@author: haimingwd
"""

def trap(height):
    # For index i, the water volume of i: vol_i = min(left_max_i, right_max_i) - height_i.
    n = len(height)
    if n < 3:
        return 0
    l, r = 0, n-1
    maxL, maxR = height[0], height[-1]
    res = 0
    while l <= r:
        if maxL <= maxR:
            maxL = max(maxL, height[l])
            res += maxL - height[l]
            l += 1
        else:
            maxR = max(maxR, height[r])
            res += maxR - height[r]
            r -= 1
    return res

trap([0,1,0,2,1,0,1,3,2,1,2,1])
