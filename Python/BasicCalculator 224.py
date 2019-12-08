# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:17:05 2019

@author: haimingwd
"""

def calculate(s):
    n = len(s)
    i = 0
    res = 0
    symNum, symStack = 1, []
    nums = {str(ea) for ea in range(10)}
    while i < n:
        if s[i] in {'+', '-'}:
            symNum = 1 if s[i] == '+' else -1
            i += 1
        elif s[i] in nums:
            j = i
            while i < n and s[i] in nums:
                i += 1
            res += int(s[j:i]) * ( symNum if not symStack else symNum*symStack[-1] )
        elif s[i] == '(':
            symStack.append(symNum if not symStack else symNum*symStack[-1])
            symNum = 1
            i += 1
        elif s[i] == ')':
            symStack.pop()
            i += 1
        else:
            i += 1
    return res

calculate("-(1-(4+5+2)-13)+(6+8)")
