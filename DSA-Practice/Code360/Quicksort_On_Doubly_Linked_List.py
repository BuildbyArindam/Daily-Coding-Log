"""
Problem   : QuickSort on Doubly Linked List
Platform  : Coding Ninjas - Code360
Link      : https://www.naukri.com/code360/problems/quicksort-on-doubly-linked-list_1071013
Difficulty: Hard
Date      : 2026-08-20

Approach:
    Adapt Lomuto-partition quicksort to a doubly linked list by swapping
    node VALUES (not relinking pointers). Find the tail once, then
    recursively partition the range [low, high]:
      - pivot = high.value
      - i = low.prev (boundary of elements <= pivot), j scans low -> high
      - whenever j.value <= pivot, advance i and swap(i, j)
      - after the scan, swap pivot into position (i.next)
      - recurse on (low, pivot_node.prev) and (pivot_node.next, high)
    Base case stops when low/high cross or are adjacent in wrong order.

Time Complexity : O(n log n) average, O(n^2) worst case (sorted/reverse input)
Space Complexity: O(log n) average recursion depth, O(n) worst case
"""


# -------------------------- Slution --------------------------


from os import *
from sys import *
from collections import *
from math import *

# Node structure
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


def quickSort(head):
    # Write your code here
    if head is None or head.next is None:
        return head
    tail = head
    while tail.next:
        tail = tail.next
    def swap(a, b):
        a.value, b.value = b.value, a.value
    def partition(low, high):
        pivot = high.value
        i = low.prev
        j = low
        while j != high:
            if j.value <= pivot:
                i = low if i is None else i.next
                swap(i, j)
            j = j.next
        i = low if i is None else i.next
        swap(i, high)
        return i
    def quicksort(low, high):
        if low is not None and high is not None:
            if low != high and low != high.next:
                pivot_node = partition(low, high)
                quicksort(low, pivot_node.prev)
                quicksort(pivot_node.next, high)
    quicksort(head, tail)
    return head
