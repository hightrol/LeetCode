# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:31:41 2019

@author: haimingwd
"""

       
def findKthSmallest(K, list1, list2):
    import bisect
    if not list1:
        return list2[K]
    elif not list2:
        return list1[K]
    n1, n2 = len(list1), len(list2)
    if n1 == 1:
        K0 = bisect.bisect_left(list2, list1[0])
        if K > K0:
            return list2[K-1]
        elif K == K0:
            return list1[0]
        else:
            return list2[K]
    elif n2 == 1:
        K0 = bisect.bisect_left(list1, list2[0])
        if K > K0:
            return list1[K-1]
        elif K == K0:
            return list2[0]
        else:
            return list1[K]
    else:
        if list1[n1//2] >= list2[n2//2]:
            if K >= n1//2 + n2//2:
                return findKthSmallest(K-(n2//2), list1, list2[(n2//2):])
            else:
                return findKthSmallest(K, list1[:(n1//2)], list2)
        else:
            if K >= n1//2 + n2//2:
                return findKthSmallest(K-(n1//2), list1[(n1//2):], list2)
            else:
                return findKthSmallest(K, list1, list2[:(n2//2)])
