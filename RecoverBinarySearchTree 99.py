# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:03:12 2019

@author: haimingwd
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def inOrder(self, p):
        if not p:
            return
        self.inOrder(p.left)
        #print(p.val, self.prev.val)
        if not self.first and self.prev.val > p.val:
            self.first = self.prev
        if self.first and self.prev.val > p.val:
            self.second = p
        self.prev = p
        self.inOrder(p.right)
            
    def recoverTree(self, root: TreeNode) -> None:
        
        self.first, self.second, self.prev = None, None, TreeNode(float('-inf'))
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        