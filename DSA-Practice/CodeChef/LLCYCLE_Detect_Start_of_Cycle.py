# Problem: Detect Start of Cycle in Linked List
# Link: https://www.codechef.com/problems/LLCYCLE
# Date: 2026-08-25
# Approach: Floyd's Cycle Detection (Tortoise & Hare).
#   Phase 1 - move slow by 1 and fast by 2 until they meet (cycle exists)
#   or fast hits None (no cycle, return -1).
#   Phase 2 - reset slow to head, advance both pointers by 1 step
#   simultaneously; they meet exactly at the cycle's starting node
#   (standard Floyd proof: distance from head to cycle start ==
#   distance from meeting point to cycle start, going around the loop).
# Time Complexity: O(N) - each pointer traverses the list a bounded number of times
# Space Complexity: O(1) - only a few pointers used, no extra data structure


# --------------------------- Solution -----------------------------


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def detectCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return -1
    slow = head
    index = 0
    while slow != fast:
        slow = slow.next
        fast = fast.next
        index += 1
    return index
