# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:44:46 2019

@author: haimingwd
"""

## Subtree of another tree 572
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """    
    def preorder_str(s):
        if not s:
            return 'None'
        res = str(s.val)
        res1 = preorder_str(s.left)
        res2 = preorder_str(s.right)
        return '#' + res + '#' + res1 + '#' + res2 + '#'
    str1 = preorder_str(s)
    str2 = preorder_str(t)
    return str2 in str1