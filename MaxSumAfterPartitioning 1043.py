# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:40:44 2019

@author: haimingwd
"""

def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
    n = len(A)
    dp = [ A[0] for _ in range(n) ]
    maxVal = A[0]
    for i in range(1, K):
        maxVal = max(maxVal, A[i])
        dp[i] = maxVal * (i+1)
    for i in range(K, n):
        maxVal = A[i]
        maxSum = dp[i-1] + A[i]
        for j in range(1, K):
            maxVal = max(maxVal, A[i-j])
            maxSum = max(maxSum, dp[i-j-1] + maxVal * (j+1))
        dp[i] = maxSum
    #print(dp)
    return dp[-1]