'''
Problem: Divide Linked List In Two
Link: https://www.naukri.com/code360/problems/divide-linked-list-in-two_763646
Platform: Coding Ninjas (Code360)
Date: 2026-08-20
Difficulty: Easy
Topics: Linked List, Two Pointers

Approach:
Split the list into two by alternating node positions - even-indexed
nodes (0, 2, 4...) go to list1, odd-indexed nodes (1, 3, 5...) go to
list2. Use two pointers (p1, p2) that each hop forward by re-linking
to the next available node from a single traversal pointer `current`,
then terminate both lists with None.

Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - only pointer reassignment, no extra structures
'''


# ------------------------- Solution ---------------------------


from os import *
from sys import *
from collections import *
from math import *

'''

    Following is the list node structure:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
'''

def divideList(head):
    # Write your code here.
    if head is None or head.next is None:
        if head is None:
            return None, None
        return head, None
    head1 = head
    head2 = head.next
    p1 = head1
    p2 = head2
    current = head.next.next
    while current is not None:
        p1.next = current
        p1 = p1.next
        current = current.next
        if current is not None:
            p2.next = current
            p2 = p2.next
            current = current.next
    p1.next = None
    p2.next = None
    return head1, head2
