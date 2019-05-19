# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:48:57 2019

@author: haimingwd
"""

def isRobotBounded(instructions):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    i = 0
    x, y = 0, 0
    for ea in instructions * 4:
        if ea == 'L':
            i = (i+1)%4
        if ea == 'R':
            i = (i-1)%4
        if ea == 'G':
            direction = directions[i]
            x += direction[0]
            y += direction[1]
            #print(i, x, y)
    if x == 0 and y == 0:
        return True
    return False