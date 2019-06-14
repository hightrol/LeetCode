# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:11:04 2019

@author: haimingwd
"""

def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    MAX = float('inf')
    path = [ [ grid[i][j] for j in range(n) ] for i in range(m) ]
    for i in range(m):
        for j in range(n):
            if i + j != 0:
                path[i][j] = min(path[i-1][j] if i >= 1 else MAX, path[i][j-1] if j >= 1 else MAX) + grid[i][j]
    return path[-1][-1]