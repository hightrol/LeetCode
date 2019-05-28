# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:40:08 2019

@author: haimingwd
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
def maxPathSum(self, root: TreeNode) -> int:
    maxSum = -10000000
    def helper(root):
        if root:
            leftSum, rightSum = helper(root.left), helper(root.right)
            maxDownPathSum = root.val + max([leftSum, rightSum, 0])
            self._maxSum = max(self._maxSum, root.val + max(leftSum, 0) + max(rightSum, 0))
            return maxDownPathSum
        else:
            return 0            
    _ = helper(root)
    return maxSum


    