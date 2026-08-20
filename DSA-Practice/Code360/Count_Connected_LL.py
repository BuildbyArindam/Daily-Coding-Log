"""
  Problem: Count Connected LL
  Link: https://www.naukri.com/code360/problems/day-21-count-connected-ll_2420237
  Date: 2026-08-20
  Difficulty: Medium
  Topics: Linked List, Hashing, Group Counting Pattern

  Approach:
      Traverse the linked list once, tracking whether the previous node's
      value was in `arr` (via a hash set for O(1) lookup). Every time we
      transition from "not in arr" -> "in arr", that marks the start of a
      new connected block, so we increment the count. Consecutive nodes
      whose values are in `arr` are treated as one connected group.

  Time Complexity: O(n + m), where n = number of nodes in the list,
                    m = length of arr (for building the set).
  Space Complexity: O(m), for storing arr as a set.
"""


# ---------------------------- Solution -----------------------------


from typing import List

'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
'''

def countConnected(head, arr: List[int], m: int) -> int:
    # write your code here
    arr_set = set(arr)
    count = 0
    current = head
    while current is not None:
        if current.data in arr_set:
            if current == head or current.data != prev_data:
                pass
        prev_data = current.data
        current = current.next
    count = 0
    current = head
    prev_in_arr = False
    while current is not None:
        if current.data in arr_set:
            if not prev_in_arr:
                count += 1
            prev_in_arr = True
        else:
            prev_in_arr = False
        current = current.next
    return count
