# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:20:48 2019

@author: haimingwd
"""

def bstToGst(self, root: TreeNode) -> TreeNode:
    def helper(head, maxVal):
        if not head:
            return None, maxVal
        nodeR, maxR = helper(head.right, maxVal)
        node = TreeNode(head.val+maxR)
        nodeL, maxL = helper(head.left, maxR+head.val)
        node.right = nodeR
        node.left = nodeL
        return node, maxL
    newRoot, val = helper(root, 0)
    return newRoot
