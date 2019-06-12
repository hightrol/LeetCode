# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:47:17 2019

@author: haimingwd
"""

def longestPalindrome(s):
    palinPos = [0]
    n = len(s)
    start, end = 0, 0
    maxLen = 1
    for i in range(1, n):
        new = []
        for j in palinPos:
            if j == 0:
                if s[i] == s[0] == s[i-1]:
                    if len(palinPos) == i:
                        new.append(0)
            else:
                if s[i] == s[j-1]:
                    new.append(j-1)
        if s[i] == s[i-1]:
            new.append(i-1)
        new.append(i)
        palinPos = new
        if i-new[0]+1 > maxLen:
            maxLen = i-new[0]+1
            start, end = new[0], i
    return s[start:(end+1)]