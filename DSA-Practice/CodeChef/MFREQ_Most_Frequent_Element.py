"""
Problem   : Most Frequent Element (MFREQ)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MFREQ
Difficulty: 2001
Topics    : Arrays, Precomputation 
Date      : 2026-10-15

Approach:
    Equal values form contiguous runs, so the only candidate for a query
    [lo, hi] is the element at the midpoint of the range. Precompute, for
    every index, where its run begins and ends. For each query, take the
    run containing mid, clip it to [lo, hi], and compare its length with
    the required frequency. Print the element if it is long enough, else -1.

Complexity:
    Time  : O(N + M) -- O(N) precomputation, O(1) per query
    Space : O(N)
"""


# ------------------------------------------------- Solution -------------------------------------------------------


import sys

def main():
    inp = sys.stdin.buffer.read().split()
    n, m = int(inp[0]), int(inp[1])
    arr = [0] + [int(t) for t in inp[2:2 + n]] 
    end_of_run = [0] * (n + 2)
    end_of_run[n] = n
    for i in range(n - 1, 0, -1):
        end_of_run[i] = end_of_run[i + 1] if arr[i] == arr[i + 1] else i
    begin_of_run = [0] * (n + 2)
    begin_of_run[1] = 1
    for i in range(2, n + 1):
        begin_of_run[i] = begin_of_run[i - 1] if arr[i] == arr[i - 1] else i
    res = []
    pos = 2 + n
    for _ in range(m):
        lo = int(inp[pos]); hi = int(inp[pos + 1]); need = int(inp[pos + 2])
        pos += 3
        mid = lo + (hi - lo + 1) // 2
        right = end_of_run[mid]
        left = begin_of_run[mid]
        if right > hi:
            right = hi
        if left < lo:
            left = lo
        res.append(arr[mid] if right - left + 1 >= need else -1)
    sys.stdout.write("\n".join(map(str, res)) + "\n")

main()
