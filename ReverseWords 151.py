# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:42:39 2019

@author: haimingwd
"""

def reverseWords(s):
    s = s.lstrip(' ').rstrip(' ')
    x = [ ea for ea in s.split(' ') if ea ]
    return ' '.join( x[::-1] )