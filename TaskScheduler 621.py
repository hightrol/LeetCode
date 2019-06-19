# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:12:06 2019

@author: haimingwd
"""

## Task Scheduler
def leastInterval(tasks, n):
    counts = [tasks.count(s) for s in set(tasks)]
    M = max(counts)
    return max(len(tasks),(M-1)*(n+1)+counts.count(M))