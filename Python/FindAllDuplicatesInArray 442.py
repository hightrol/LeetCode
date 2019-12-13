# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:05:55 2019

@author: haimingwd
"""

def findDuplicates(nums):
    n = len(nums)
    lst = []
    for i in range(n):
        if nums[abs(nums[i])-1] > 0:
            nums[abs(nums[i]-1)] *= -1
        else:
            lst.append(abs(nums[i]))
    for i in range(n):
        nums[i] = abs(nums[i])
    return lst
