"""
Problem: The Museum Ticket Budget
Platform: Unstop
Link: https://unstop.com/code/practice/660827
Date: 2026-09-17
Difficulty: Easy
Topics: Array, Sliding Window, Two Pointers, Prefix Sum

Approach:
Variable-size sliding window. Expand the window by moving `right` and
adding cost[right] to current_sum. Whenever current_sum exceeds the
budget B, shrink from the left (subtract cost[left], increment left)
until the window is valid again. Track the max window length seen —
that's the max number of tickets purchasable within budget B.

Time Complexity: O(n) — each index enters/leaves the window at most once
Space Complexity: O(1) — only a few scalar variables
"""


# ------------------------------ Solution ---------------------------------------------


n, B = map(int, input().split())
cost = list(map(int, input().split()))
left = 0
current_sum = 0
max_len = 0
for right in range(n):
    current_sum += cost[right]
    while current_sum > B and left <= right:
        current_sum -= cost[left]
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)
