# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:06:01 2019

@author: haimingwd
"""

def find132pattern(nums):
    intervalStack = []
    n = len(nums)
    start = float('inf')
    for i in range(n):
        start, end = min(nums[i], start), nums[i]
        while intervalStack and end >= intervalStack[-1][-1]:
            intervalStack.pop()
        if intervalStack and end > intervalStack[-1][0] and end < intervalStack[-1][1]:
            return True
        while intervalStack and end >= intervalStack[-1][0]:
            end = max(end, intervalStack.pop()[1])
        if end > start:
            intervalStack.append([start, end])
        #print(intervalStack)
    return False

find132pattern([3, 5, 2, -1, -3, 1, 4])