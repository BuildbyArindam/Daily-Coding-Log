"""
Problem   : Deletion In Circular Linked List
Platform  : Coding Ninjas Code360
Link      : https://www.naukri.com/code360/problems/deletion-in-circular-linked-list_630409
Date      : 2026-08-20
Difficulty: Easy
Topics    : Linked List, Circular Linked List

Approach:
- Handle empty list (head is None) upfront.
- Find 'last' node (the one pointing back to head) by traversing until last.next == head.
- Case 1: key is at head -> if it's the only node, return None; else move head
  forward and fix last.next to point to new head.
- Case 2: key is elsewhere -> standard prev/curr traversal around the circle,
  unlink curr when found.
- If key not found, list is returned unchanged.

Time Complexity : O(N) - single pass to find 'last', worst-case another pass to find key
Space Complexity: O(1) - in-place pointer manipulation, no extra data structures
"""


# --------------------------- Solution -------------------------------

'''
Following is the Node class used to represent the Node of a Circular Linked List

class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None

'''

def deleteNode(head, key):
    if head is None:
        return None
    last = head
    while last.next != head:
        last = last.next
    if head.data == key:
        if head.next == head:
            return None
        head = head.next
        last.next = head
        return head
    prev = head
    curr = head.next
    while curr != head:
        if curr.data == key:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next
    return head
