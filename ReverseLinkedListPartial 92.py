# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:17:40 2019

@author: haimingwd
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i, fakeHead = 1, ListNode(None)
        fakeHead.next = head
        p0, p1 = fakeHead, head
        while i < m:
            p0, p1 = p1, p1.next
            i += 1
        q0, q1 = p1.next, p1
        while i < n:
            q0.next, p1, q0 = p1, q0, q0.next
            i += 1
        p0.next, q1.next = p1, q0
        return fakeHead.next