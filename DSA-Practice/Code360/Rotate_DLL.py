"""
Problem   : Rotate DLL
Platform  : Coding Ninjas / Naukri Code360
Link      : https://www.naukri.com/code360/problems/rotate-dll_1115782?kunjiRedirection=true
Date      : 2026-08-21
Difficulty: Medium
Topics    : Doubly Linked List, Pointer Manipulation

Approach:
    Rotate the DLL left by k, i.e., the k-th node becomes the new tail
    and the (k+1)-th node becomes the new head.
    1. Walk `k` steps from head to locate the k-th node (kth_node).
    2. Walk from kth_node to the end to find the current tail.
    3. Reconnect: tail.next -> old head (circle the list),
       old head.prev -> tail, new_head = kth_node.next,
       then break the link at kth_node to form the new tail/head boundary.

Time Complexity : O(N) — one pass to reach k-th node (O(k)) + one pass to
                   reach the tail (O(N-k)) = O(N) overall.
Space Complexity: O(1) — in-place pointer rewiring, no extra data structures.
"""


# ------------------------ SOlution --------------------------


from os import *
from sys import *
from collections import *
from math import *

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def rotateDLL(head, k):
    if head is None or head.next is None or k == 0:
        return head
    current = head
    count = 1
    while count < k and current is not None:
        current = current.next
        count += 1
    kth_node = current
    tail = kth_node
    while tail.next is not None:
        tail = tail.next
    new_head = kth_node.next
    tail.next = head
    head.prev = tail
    kth_node.next = None
    new_head.prev = None
    return new_head
