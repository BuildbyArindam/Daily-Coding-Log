'''
Problem   : Next Greater Node In Linked List
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/next-greater-node-in-linked-list_1262083
Difficulty: Easy
Topics    : Linked List, Stack, Monotonic Stack
Date      : 2026-08-22

Approach:
  Traverse the linked list once and copy values into an array (values[]),
  since random access is easier on an array than a linked list for this pattern.
  Use a monotonic decreasing stack of INDICES over this array:
    - For each value, pop all stack indices whose values are smaller than
      the current value -> current value is their "next greater" element.
    - Push the current index onto the stack.
  Any indices left on the stack at the end have no next greater element,
  so their answer stays 0 (default).

Time complexity  : O(n) - each index is pushed and popped at most once
Space complexity : O(n) - values[] array + stack + ans[] array
'''


# --------------------------- Solution ---------------------------


from os import *
from sys import *
from collections import *
from math import *

'''
  ----Linked list Node class for reference-----
    class Node:
        def __init__(self, data):
            self.val = data
            self.next = None
            
'''

def findNextGreaterNodeList(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    n = len(values)
    ans = [0] * n
    stack = []
    for i in range(n):
        while stack and values[i] > values[stack[-1]]:
            idx = stack.pop()
            ans[idx] = values[i]
        stack.append(i)
    return ans
