# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:28:40 2019

@author: haimingwd
"""

def leastInterval(tasks, n):
    counts = [tasks.count(s) for s in set(tasks)]
    M = max(counts)
    return max(len(tasks),(M-1)*(n+1)+counts.count(M))