"""
Problem   : The Lantern Festival Finale
Platform  : Unstop
Link      : https://unstop.com/code/practice/658933
Date      : 2026-08-29
Difficulty: Medium
Topics    : Array, Sliding Window, Two Pointers, Monotonic Queue, Deque, Prefix Sum

Approach:
    Maintain a variable-size sliding window [left, right] using two
    monotonic deques to track the max and min elements in the window
    in O(1) amortized time. Expand `right` each step, pushing/popping
    from both deques to keep them monotonic (min_dq increasing,
    max_dq decreasing). While the window's max-min exceeds L, shrink
    from the left (popping stale indices from the deques and
    updating current_sum). Track the maximum current_sum seen over
    all valid windows.

Time Complexity : O(n) — each index is pushed/popped from each deque at most once.
Space Complexity: O(n) — deques can hold up to n indices in the worst case.
"""


# ------------------------------ Solution -----------------------------------


from collections import deque
n, L = map(int, input().split())
a = list(map(int, input().split()))
min_dq = deque()  
max_dq = deque() 
left = 0
current_sum = 0
answer = 0
for right in range(n):
    current_sum += a[right]
    while min_dq and a[min_dq[-1]] >= a[right]:
        min_dq.pop()
    min_dq.append(right)
    while max_dq and a[max_dq[-1]] <= a[right]:
        max_dq.pop()
    max_dq.append(right)
    while a[max_dq[0]] - a[min_dq[0]] > L:
        if min_dq[0] == left:
            min_dq.popleft()
        if max_dq[0] == left:
            max_dq.popleft()
        current_sum -= a[left]
        left += 1
    answer = max(answer, current_sum)
print(answer)
