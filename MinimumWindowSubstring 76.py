# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:38:20 2019

@author: haimingwd
"""

def minWindow(s, t):
    from collections import Counter
    if not s or not t:
        return ""
    dict_t = Counter(t)
    dict_window = dict({})  # char counter for s[i:(j+1)]
    required, paired = len(dict_t), 0
    l, r, n = 0, 0, len(s)
    minL = float('inf')
    while r < n:
        c = s[r]
        dict_window[c] = dict_window.get(c, 0) + 1
        if c in dict_t and dict_window[c] == dict_t[c]:
            paired += 1
        while l <= r and paired == required:
            if r-l+1 < minL:
                start, end, minL = l, r, r-l+1
            c = s[l]
            dict_window[c] -= 1
            if c in dict_t and dict_window[c] < dict_t[c]:
                paired -= 1
            l += 1
        r += 1
    return "" if minL == float('inf') else s[start:(end+1)]

minWindow("ADOBECODEBANC", "ABC")