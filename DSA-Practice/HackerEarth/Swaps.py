"""
Problem   : Swaps
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/swaps-e4a6b638/
Difficulty: Easy
Topics    : Mathematics, Sliding Window
Date      : 2026-10-03

Approach:
    Let `good` be the number of elements >= K. In the final arrangement these
    must form one contiguous block of length `good`. Slide a window of size
    `good` across the array and count the "bad" elements (< K) inside it.
    Each bad element in the window needs one swap with a good element outside
    it, so the answer is the minimum bad count over all windows.
    If good == 0 or good == N, nothing needs to move, so the answer is 0.

Complexity:
    Time : O(N)  - one pass to count good elements, one pass to slide the window
    Space: O(N)  - input array (O(1) extra beyond that)
"""


# ------------------------------------- Solution -------------------------------------------------


N, K = map(int, input().split())
arr = list(map(int, input().split()))
good = sum(1 for x in arr if x >= K)
if good == 0 or good == N:
    print(0)
else:
    bad = sum(1 for x in arr[:good] if x < K)
    ans = bad
    for i in range(good, N):
        if arr[i - good] < K:
            bad -= 1
        if arr[i] < K:
            bad += 1
        ans = min(ans, bad)
    print(ans)
