# Problem: Signal Peaks at Mission Control
# Link: https://unstop.com/code/practice/660826
# Date: 2026-09-16
# Difficulty: Medium
# Topics: Array, Sliding Window, Monotonic Queue, Deque
#
# Approach:
# - Use a monotonic decreasing deque to store indices of useful candidates.
# - Remove indices that fall outside the current window.
# - Remove smaller/equal elements from the back since they cannot be the maximum.
# - The front of the deque always contains the maximum of the current window.
#
# Time Complexity: O(n)
# Space Complexity: O(k)


# ------------------------------- Solution ----------------------------------


from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
dq = deque()
result = []
for i in range(n):
    while dq and dq[0] <= i - k:
        dq.popleft()
    while dq and a[dq[-1]] <= a[i]:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        result.append(a[dq[0]])
print(*result)
