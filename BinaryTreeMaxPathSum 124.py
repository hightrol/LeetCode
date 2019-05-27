# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:40:08 2019

@author: haimingwd
"""

class Solution:
    def setUp(self):
        #self._maxDownPathSumDict = {None: 0}
        self._maxSum = -10000000
    
    def helper(self, root):
        if root:
            leftSum, rightSum = self.helper(root.left), self.helper(root.right)
            maxDownPathSum = root.val + max([leftSum, rightSum, 0])
            self._maxSum = max(self._maxSum, root.val + max(leftSum, 0) + max(rightSum, 0))
            return maxDownPathSum
        else:
            return 0
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.setUp()
        _ = self.helper(root)
        return self._maxSum
    