# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:16:11 2019

@author: haimingwd
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        
        if not head:
            return None
        else:
            p, q = None, head
            while q:
                q.next, p, q = p, q, q.next
            return p