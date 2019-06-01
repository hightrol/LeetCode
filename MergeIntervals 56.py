# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:36:14 2019

@author: haimingwd
"""

def merge(self, intervals):
    if not intervals:
        return []
    intervals.sort(key = lambda ea:ea[0])
    res = [intervals[0]]
    for ea in intervals:
        last = res[-1]
        if ea[0] > last[1]:
            res.append(ea)
        elif ea[1] > last[1]:
            last[1] = ea[1]
    return res