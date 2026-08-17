"""
Problem   : Exposition
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/6/E
Difficulty: *1900
Topics    : Two Pointers, Monotonic Deque, DSU, Trees, Binary Search
Date      : 2026-08-17

Approach:
    Sliding window (two pointers) over the array of heights. Maintain two
    monotonic deques - one tracking the max in the current window (decreasing
    deque) and one tracking the min (increasing deque). As `right` expands,
    push into both deques, popping out elements that can no longer be the
    max/min. Whenever (max - min) > k, shrink the window from the left,
    evicting stale deque fronts as they fall outside the window.
    Track the maximum window length found; if a new max length is found,
    reset the results list, otherwise append ties.

    Note: This problem is tagged with DSU/trees/binary search as alternate
    solution approaches on Codeforces, but the two-pointer + monotonic
    deque method implemented here is the more efficient O(n) technique.

Time Complexity : O(n) - each index pushed/popped from each deque at most once
Space Complexity: O(n) - deques + results list in the worst case
"""


# ---------------------- Solution ----------------------------


import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    h = [int(x) for x in data[2:]]
    max_dq = deque()
    min_dq = deque()
    left = 0
    max_len = 0
    results = []
    for right in range(n):
        val = h[right]
        while max_dq and h[max_dq[-1]] <= val:
            max_dq.pop()
        max_dq.append(right)
        while min_dq and h[min_dq[-1]] >= val:
            min_dq.pop()
        min_dq.append(right)
        while h[max_dq[0]] - h[min_dq[0]] > k:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            results = [(left + 1, right + 1)]  
        elif current_len == max_len:
            results.append((left + 1, right + 1))
    print(f"{max_len} {len(results)}")
    for start, end in results:
        print(f"{start} {end}")

if __name__ == '__main__':
    solve()
