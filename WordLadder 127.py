# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:01:59 2019

@author: haimingwd
"""

def ladderLength(beginWord, endWord, wordList):
    n = len(beginWord)
    import queue, string
    dist = {beginWord: 0}
    wordQueue = queue.Queue()
    wordQueue.put(beginWord)
    wordSet = set(wordList)
    while not wordQueue.empty():
        x = wordQueue.get()
        for i in range(n):
            for char in string.ascii_lowercase:
                midWord = x[:i] + char + x[(i+1):]
                if midWord in wordSet and midWord not in dist:
                    dist[midWord] = dist[x] + 1
                    wordQueue.put(midWord)
                    if midWord == endWord:
                        return dist[endWord] + 1
    return 0
            
            
        
        