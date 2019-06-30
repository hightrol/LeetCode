# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:20:28 2019

@author: haimingwd
"""

## split Array Into Fibonacci Sequence 842
def splitIntoFibonacci(S):
    
    n = len(S)
    def check(i, j, s):
        res = [int(s[j:]), int(s[i:j])]
        while s:
            y, z = int(s[i:j]), int(s[j:])
            x = z - y
            if s[:i].endswith(str(x)):
                res.append(x)
                s = s[:j]
                i, j = i - len(str(x)), i
                if i == 0:
                    return res[::-1]
            else:
                return []
        return res[::-1]
    for j in range(n-1, max(int((n-2)/2-1), 1), -1):
        z = int(S[j:])
        if z > 2**31 - 1:
            break
        for i in range(j-1, 0, -1):
            print(i, j)
            y = int(S[i:j])
            if y <= z:
                res = check(i, j, S)
                if res:
                    return res
            else:
                break
    return []

splitIntoFibonacci("123456579")