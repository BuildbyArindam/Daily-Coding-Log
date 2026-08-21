"""
Problem: Cycle Detection in a Singly Linked List
Platform: Coding Ninjas / Naukri Code360
Link: https://www.naukri.com/code360/problems/cycle-detection-in-a-singly-linked-list_628974?kunjiRedirection=true
Difficulty: Medium
Date Solved: 2026-08-21
Topics: Linked List, Two Pointers, Floyd's Cycle Detection Algorithm

Approach:
    Floyd's Tortoise and Hare technique. Use two pointers - 'slow' moves
    one node at a time, 'fast' moves two nodes at a time. If the list has
    a cycle, fast will eventually "lap" slow and they meet at the same
    node. If fast (or fast.next) hits None, the list is acyclic.

Time Complexity: O(n)  -- each pointer traverses at most ~2n nodes combined
Space Complexity: O(1) -- only two extra pointers used, no auxiliary structure
"""


# ------------------------ Solution -----------------------------


'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    # Write your code here.
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
