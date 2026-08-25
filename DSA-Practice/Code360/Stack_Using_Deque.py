"""
Problem   : Stack Using Deque
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/stack-using-deque_1170512?kunjiRedirection=true
Difficulty: Easy
Date      : 2026-08-25
Topics    : Stack, Queue, Deque, Design

Approach:
Implement a Stack ADT using Python's collections.deque as the
underlying storage. Push/pop/top all operate on the right end (tail)
of the deque, mirroring standard stack (LIFO) behavior. isEmpty and
size are simple length checks.

Time Complexity : O(1) for push, pop, top, isEmpty, size
                   (deque supports O(1) append/pop from both ends)
Space Complexity: O(n) — n elements stored in the deque
"""


# ----------------------- Solution -----------------------------


from os import *
from sys import *
from collections import *
from math import *

class Stack:
    def __init__(self):
        self.deque = deque()
    def push(self, x):
        self.deque.append(x)
        return True
    def pop(self):
        if self.isEmpty():
            return -1
        return self.deque.pop()
    def top(self):
        if self.isEmpty():
            return -1
        return self.deque[-1]
    def isEmpty(self):
        return len(self.deque) == 0
    def size(self):
        return len(self.deque)
