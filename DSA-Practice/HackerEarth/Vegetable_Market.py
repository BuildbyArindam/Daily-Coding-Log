"""
Problem   : Vegetable Market
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/vegetable-market-ea2b4462/
Date      : 2026-08-15
Difficulty: Medium
Topics    : Basic Programming, Implementation, Data Structures, Hash Maps

Approach:
For each query K, binary search on the minimum "cap" X such that
summing min(arr[i], X) across all stalls yields at least K vegetables.
Since the total gathered is monotonically non-decreasing in X, binary
search over X in [1, max(arr)] works. For a candidate X, use bisect_left
on the sorted array to split stalls into those below X (contribute their
full value) and those at/above X (contribute exactly X each); prefix
sums make this split's total an O(log N) lookup. If K exceeds the sum
of all elements, output -1 immediately.

Time complexity : O(N log N) for sorting + O(Q log N log(max(arr)))
                   for Q queries (binary search over X, each check O(log N))
Space complexity : O(N) for the sorted array and prefix sum array
"""


# --------------------- Solution -----------------------------


import sys
from bisect import bisect_left

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    arr = [int(x) for x in input_data[1:N + 1]]
    arr.sort()
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + arr[i]
    total_max = prefix[N]
    idx = N + 1
    Q = int(input_data[idx])
    idx += 1
    results = []
    def get_total(X):
        pos = bisect_left(arr, X)
        return prefix[pos] + (N - pos) * X
    for _ in range(Q):
        K = int(input_data[idx])
        idx += 1
        if K > total_max:
            results.append("-1")
            continue
        low = 1
        high = arr[-1]
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if get_total(mid) >= K:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        results.append(str(ans))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
  
