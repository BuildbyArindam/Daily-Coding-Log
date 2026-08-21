"""
Problem: Remove the Data
Platform: Naukri Code360
Link: https://www.naukri.com/code360/problems/remove-the-data_7103275?kunjiRedirection=true
Date: 2026-08-21
Difficulty: Hard

Approach:
Two-pointer iterative removal on a singly linked list. First, advance `head`
past any leading nodes that match the target value. Then walk the list with
`current`: if current.next holds the target value, splice it out by
relinking current.next to current.next.next (current stays put to re-check
the new current.next); otherwise advance current. Handles removal at the
head, middle, tail, and consecutive duplicates in a single pass.

Time Complexity:  O(n) — single pass over the list
Space Complexity: O(1) — in-place pointer manipulation, no extra structures
"""


# --------------------------- Solution --------------------------------


class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None
def removeData(head: ListNode, data: int) -> ListNode:
    while head is not None and head.data == data:
        head = head.next
    current = head
    while current is not None and current.next is not None:
        if current.next.data == data:
            current.next = current.next.next
        else:
            current = current.next
    return head
