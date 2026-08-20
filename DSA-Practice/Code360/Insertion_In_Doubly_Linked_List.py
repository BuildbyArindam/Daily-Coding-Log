'''
Problem   : Insertion In Doubly Linked List
Platform  : Coding Ninjas (Code360)
Link      : https://www.naukri.com/code360/problems/insertion-in-doubly-linked-list_4609682
Difficulty: Easy
Topics    : Linked List, Doubly Linked List, Node Manipulation
Date      : 2026-08-20

Approach:
    - If insertion index k == 0, insert new_node before current head,
      link new_node.next to old head, and fix old head's prev pointer.
      Return new_node as the new head.
    - Otherwise, traverse (k-1) steps from head to reach the node just
      before the insertion point (curr).
    - Splice new_node in between curr and curr.next, updating both
      forward (next) and backward (prev) pointers on all three nodes
      involved (curr, new_node, curr.next).
    - Return the original head (unchanged unless k == 0).

Time Complexity : O(k)  -- traversal to the insertion point
Space Complexity: O(1)  -- constant extra space, in-place pointer updates
'''


# --------------------------- Solution --------------------------


from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the class structure of the Node class:
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
            self.prev = None
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert(k, val, head):
    new_node = Node(val)
    if k == 0:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        return new_node
    curr = head
    for _ in range(k - 1):
        curr = curr.next
    new_node.next = curr.next
    new_node.prev = curr
    if curr.next is not None:
        curr.next.prev = new_node
    curr.next = new_node
    return head
