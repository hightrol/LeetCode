# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:03:54 2019

@author: haimingwd
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1, l2):
    stack1, stack2, stack3 = [], [], []
    while l1:
        stack1.append(l1)
        l1 = l1.next
    while l2:
        stack2.append(l2)
        l2 = l2.next
    t = 0
    while stack1 or stack2:
        x, y = stack1.pop().val if stack1 else 0, stack2.pop().val if stack2 else 0
        node, t = ListNode((x+y+t)%10), (x+y+t)//10
        if stack3:
            node.next = stack3[-1]
        stack3.append(node)
    if t:
        node = ListNode(t)
        node.next = stack3[-1]
        stack3.append(node)
    return stack3[-1]
