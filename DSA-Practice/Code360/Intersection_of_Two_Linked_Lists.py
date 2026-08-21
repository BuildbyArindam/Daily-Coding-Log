"""
Problem: Intersection of Two Linked Lists
Platform: Coding Ninjas / Code360
Link: https://www.naukri.com/code360/problems/intersection-of-two-linked-lists_630457
Date Solved: 2026-08-21
Difficulty: Easy
Topics: Linked List, Two Pointers

Approach:
    Use two pointers starting at the heads of each list. When a pointer
    reaches the end of its list, redirect it to the head of the OTHER list.
    Because both pointers together traverse (lengthA + lengthB) nodes before
    meeting, this naturally cancels out the length difference between the
    two lists — so they arrive at the intersection node (or None, if the
    lists don't intersect) at the same step, without needing to precompute
    lengths separately.

Time Complexity:  O(m + n)   — each pointer traverses at most m+n nodes
Space Complexity: O(1)       — only two extra pointers used
"""


# --------------------------- Solution ----------------------------------


'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def findIntersection(firstHead, secondHead):
    p1 = firstHead
    p2 = secondHead
    while p1 != p2:
        if p1 is None:
            p1 = secondHead
        else:
            p1 = p1.next
        if p2 is None:
            p2 = firstHead
        else:
            p2 = p2.next
    return p1
