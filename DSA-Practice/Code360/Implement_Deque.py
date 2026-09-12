"""
Problem   : Implement Deque
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/651074/offering/10442137
Difficulty: Easy
Date      : 2026-09-12
Topic     : Arrays, Queue, Deque

Approach:
Circular array implementation of a fixed-size deque. Use two pointers,
front and rear, both initialized to -1 as the "empty" sentinel. All
push/pop operations move front or rear circularly using modulo
arithmetic, so no shifting of elements is ever needed. isFull() checks
whether advancing rear by one would collide with front, which works
cleanly here since front == -1 (not a wasted slot) is used to signal
empty rather than the usual "reserve one slot" trick — so the full
array capacity is usable.

Time Complexity : O(1) for pushFront, pushRear, popFront, popRear, getFront, getRear
Space Complexity: O(n), n = size of the deque array
"""


# ------------------------ Solution ----------------------------------


from os import *
from sys import *
from collections import *
from math import *

class Deque:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.front = -1
        self.rear = -1
    def pushFront(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.arr[self.front] = x
        return True
    def pushRear(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = x
        return True
    def popFront(self):
        if self.isEmpty():
            return -1
        value = self.arr[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value
    def popRear(self):
        if self.isEmpty():
            return -1
        value = self.arr[self.rear]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        return value
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.rear]
    def isEmpty(self):
        return self.front == -1
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
