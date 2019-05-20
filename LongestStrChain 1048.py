# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:51:33 2019

@author: haimingwd
"""

def longestStrChain(words):
    def subWord(word1, word2):
        n1, n2 = len(word1), len(word2)
        if n2 - n1 != 1:
            return False
        for j in range(n2):
            if word1.startswith(word2[:j]) and word1.endswith(word2[(j+1):]):
                return True
        return False
        
    words = sorted( words, key = lambda x:len(x) )
    n = len(words)
    dp = [1 for _ in range(n)]
    k = 0
    for i in range(1, n):
        while len(words[k]) < len(words[i])-1:
            k += 1
        for j in range(k, i):
            if subWord(words[j], words[i]):
                dp[i] = max(dp[i], dp[j]+1)
    #print(dp)
    return max(dp)