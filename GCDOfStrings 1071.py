# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:53:15 2019

@author: haimingwd
"""

# GCD of Strings
def gcdOfStrings(str1, str2):
    n1, n2 = len(str1), len(str2)
    for i in range(min(n1,n2), 0, -1):
        if n1%i == 0 and n2%i == 0:
            x = str1[:i]
            if str1 == x*(n1//i) and str2 == x*(n2//i):
                return x
            else:
                return ''
            