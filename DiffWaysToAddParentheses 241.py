# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:39:53 2019

@author: haimingwd
"""

def diffWaysToCompute(inputs):
    opIx = [ i for i in range(len(inputs)) if inputs[i] in ['+', '-', '*'] ]
    if not opIx:
        return [int(inputs)]
    total = []
    for i in opIx:
        xList = diffWaysToCompute(inputs[:i])
        yList = diffWaysToCompute(inputs[(i+1):])
        if inputs[i] == '+':
            res = [ x + y for x in xList for y in yList ]
        elif inputs[i] == '-':
            res = [ x - y for x in xList for y in yList ]
        elif inputs[i] == '*':
            res = [ x * y for x in xList for y in yList ]
        total.extend(res)
    return total


diffWaysToCompute("2*3-4*5")
