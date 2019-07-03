# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:43:18 2019

@author: haimingwd
"""

## Find Eventual Safe States 802
def eventualSafeNodes(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[int]
    """
    n = len(graph)
    visited = [-1 for i in range(n)]
    loop = [-1 for i in range(n)]
    def checkLoop(start):
        if visited[start] == -1:
            visited[start] = 1
            loop[start] = 1
            for end in graph[start]:
                if checkLoop(end):
                    return True
            loop[start] = -1
        else:
            return True if loop[start] == 1 else False
    for i in range(n):
        checkLoop(i)
    return [ i for i in range(n) if loop[i] == -1 ]

eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])