# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:16:46 2019

@author: haimingwd
"""

## palindrome Partitioning 132
def minCut(s):
    if s == s[::-1]:
        return 0
    n = len(s)
    palindromeVec = [ True ]   # whether s[i:j] is palindrome or not
    cut = [ i for i in range(n) ]
    for i in range(1, n):
        palindromeVec = [ palindromeVec[j+1] and s[i] == s[j] for j in range(i-1)] + [s[i-1] == s[i]] + [True]
        for j in range(i+1):
            if palindromeVec[j]:
                if j == 0:
                    cut[i] = 0
                    break
                else:
                    cut[i] = min(cut[i], cut[j-1] + 1)
    return cut[-1]

minCut('aab')