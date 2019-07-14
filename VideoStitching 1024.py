# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:28:20 2019

@author: haimingwd
"""

def videoStitching(clips, T):
    """
    :type clips: List[List[int]]
    :type T: int
    :rtype: int
    """
    clips = sorted(clips)
    ans = [0]
    maxLen = 0
    for clip in clips:
        s, e = clip[0], clip[1]
        if s >= len(ans):
            return -1
        if e <= maxLen:
            pass
        else:
            for _ in range(maxLen+1, e+1):
                ans.append(ans[s]+1)
            maxLen = e
        if maxLen >= T:
            return ans[T]
    return -1

videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)