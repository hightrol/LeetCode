# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:07:48 2019

@author: haimingwd
"""


## convert sorted list to binary search tree 109

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        #recursive without list
        if not head:
            return None
        p1 = p2 = p3 =head
        while p1.next and p2.next and p2.next.next:
            p3 = p1
            p1 = p1.next
            p2 = p2.next.next
        tn = TreeNode(p1.val)
        if p1 != p3:
            p3.next = None
            tn.left = self.sortedListToBST(head)
            tn.right = self.sortedListToBST(p1.next)
        else:
            tn1 = TreeNode(p1.next.val) if p1.next else None
            tn.right = tn1
        return tn    
        
#        arr = []
#        p = head
#        while p:
#            arr.append(p.val)
#            p = p.next
#        n = len(arr)
#        if not arr:
#            return None
#        def makeBST(low, high):
#            if low == high:
#                return TreeNode(arr[low])
#            elif high - low == 1:
#                tn1 = TreeNode(arr[low])
#                tn = TreeNode(arr[high])
#                tn.left = tn1
#                return tn
#            else:
#                mid = (low+high)/2
#                tn1, tn2 = makeBST(low, mid-1), makeBST(mid+1, high)
#                tn = TreeNode(arr[mid])
#                tn.left, tn.right = tn1, tn2
#                return tn
#        return makeBST(0, n-1)
