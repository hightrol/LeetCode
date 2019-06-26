# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:14:09 2019

@author: haimingwd
"""

## subarrayProductLessThanK
def numSubarrayProductLessThanK(self, nums, k):
    if k <= 1:
        return 0
    cumprod = 1
    i, j, n = 0, 0, len(nums)
    total = 0
    for j in range(n):
        cumprod *= nums[j]
        while cumprod >= k:
            cumprod /= nums[i]
            i += 1
        total += j-i+1
    return total