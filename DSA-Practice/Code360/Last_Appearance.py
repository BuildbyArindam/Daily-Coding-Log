"""
Problem   : Last Appearance
Platform  : Coding Ninjas / Naukri Code360
Link      : https://www.naukri.com/code360/problems/last-appearance_763269?kunjiRedirection=true
Difficulty: Medium
Date      : 2026-08-20

Approach:
    For each value in the linked list, keep only its LAST occurrence while
    preserving the original relative order of the remaining nodes.
    1. Reverse the list in-place (O(1) extra space).
    2. Traverse the reversed list; the first time a value is seen here
       corresponds to its LAST occurrence in the original list.
       Build a new list by prepending each first-seen node.
       Prepending while walking the reversed list naturally restores
       the original relative order.

Time Complexity : O(n)   - one pass to reverse, one pass to filter
Space Complexity: O(n)   - hash set to track seen values (reversal itself is O(1) extra)
"""


# ------------------------ Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *

# List Node Class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lastAppearance(head):
    # Write your code here.
    if head is None:
        return None
    last = set()
    temp = head
    while temp:
        last.add(temp.data)
        temp = temp.next
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    seen = set()
    curr = prev
    new_head = None
    tail = None
    while curr:
        nxt = curr.next
        if curr.data not in seen:
            seen.add(curr.data)
            curr.next = new_head
            new_head = curr
        curr = nxt
    return new_head
