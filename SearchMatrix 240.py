# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:23:14 2019

@author: haimingwd
"""

### searchMatrix 240

def searchMatrix(matrix, target):            
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n-1
    while i < m and j >= 0:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return True
    return False

searchMatrix( [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 25 )