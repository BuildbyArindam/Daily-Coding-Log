"""
Platform: Code360 (Naukri)
Problem: N Queue Using Array
Link: https://www.naukri.com/code360/problems/n-queue-using-array_1170053?kunjiRedirection=true
Date: 2026-08-24
Difficulty: Easy
Topics: Arrays, Queue, Data Structure Design

Approach:
Implement n independent queues inside a single fixed-size array using a
"free list" (linked-list-style indexing) to manage unused slots.
- arr[]: stores actual values
- next[]: for each index, points to the next index in its queue (or free list)
- front[]/rear[] : per-queue pointers into arr/next chain
- free: head of the free-slot list, reused on dequeue for O(1) reuse

Time Complexity: O(1) per enqueue/dequeue
Space Complexity: O(s + n), where s = array size, n = number of queues
"""


# --------------------------- Solution -----------------------------


from os import *
from sys import *
from collections import *
from math import *

class NQueue:
    def __init__(self, n, s):
        self.arr = [0] * s
        self.next = [-1] * s
        self.front = [-1] * n
        self.rear = [-1] * n
        for i in range(s - 1):
            self.next[i] = i + 1
        self.next[s - 1] = -1
        self.free = 0
    def enqueue(self, x, m):
        m -= 1
        if self.free == -1:
            return False
        index = self.free
        self.free = self.next[index]
        self.arr[index] = x
        self.next[index] = -1
        if self.front[m] == -1:
            self.front[m] = index
            self.rear[m] = index
        else:
            self.next[self.rear[m]] = index
            self.rear[m] = index
        return True
    def dequeue(self, m):
        m -= 1
        if self.front[m] == -1:
            return -1
        index = self.front[m]
        value = self.arr[index]
        self.front[m] = self.next[index]
        if self.front[m] == -1:
            self.rear[m] = -1
        self.next[index] = self.free
        self.free = index
        return value
