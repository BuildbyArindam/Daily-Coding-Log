"""
Problem: Deletion of Repeats
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/19/C
Difficulty: *2200
Topics: Greedy, Hashing, String Suffix Structures
Date: 2026-08-28

Approach:
Find the earliest occurring repeated adjacent block (a[i..i+x-1] == a[i+x..i+2x-1])
using double-hashing (two mod values) for O(1) substring comparison after O(n)
prefix-hash precomputation. Repeated blocks are grouped by length x in a
bucket-per-length structure; a min-heap over lengths lets us always fetch the
smallest length whose earliest still-valid start (>= current pointer p) exists.
Each time a repeat is found at position i with length x, advance the pointer
p = i + x (skip the duplicated half) and re-check the heap, since removing a
block can only be done in increasing order of x per Codeforces model-solution
logic (ties broken by earliest start). Continue until no valid repeats remain;
the answer is the array from the final pointer p onward.

Time Complexity:  O(n^2) worst case for collecting candidate repeats
                   across all (i, j) equal-value pairs, each O(1) hash check
                   -> O(n^2) precomputation, O(n log n) heap processing
Space Complexity: O(n^2) worst case for `starts` buckets (bounded by number of
                   matching value pairs), O(n) for hash arrays
"""


# ---------------------------------- Solution --------------------------------------------


import sys
import heapq

def solve():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    positions = {}
    for i, v in enumerate(a):
        positions.setdefault(v, []).append(i)
    MOD1 = 1_000_000_007
    MOD2 = 1_000_000_009
    BASE = 911382323
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    for i, v in enumerate(a):
        val = v + 1
        pow1[i + 1] = pow1[i] * BASE % MOD1
        pow2[i + 1] = pow2[i] * BASE % MOD2
        h1[i + 1] = (h1[i] * BASE + val) % MOD1
        h2[i + 1] = (h2[i] * BASE + val) % MOD2
    def equal_substrings(i, j, length):
        """Check a[i:i+length] == a[j:j+length]."""
        x1 = (h1[i + length] - h1[i] * pow1[length]) % MOD1
        y1 = (h1[j + length] - h1[j] * pow1[length]) % MOD1
        if x1 != y1:
            return False
        x2 = (h2[i + length] - h2[i] * pow2[length]) % MOD2
        y2 = (h2[j + length] - h2[j] * pow2[length]) % MOD2
        return x2 == y2
    starts = [[] for _ in range(n + 1)]
    for arr in positions.values():
        m = len(arr)
        for p in range(m):
            i = arr[p]
            for q in range(p + 1, m):
                j = arr[q]
                x = j - i
                if i + 2 * x <= n and equal_substrings(i, j, x):
                    starts[x].append(i)
    heap = []
    for x in range(1, n + 1):
        if starts[x]:
            starts[x].sort()
            heap.append(x)
    heapq.heapify(heap)
    ptr = [0] * (n + 1)
    p = 0
    while heap:
        x = heap[0]
        lst = starts[x]
        k = ptr[x]
        while k < len(lst) and lst[k] < p:
            k += 1
        ptr[x] = k
        if k == len(lst):
            heapq.heappop(heap)
            continue
        i = lst[k]
        p = i + x
    result = a[p:]
    print(len(result))
    print(*result)

if __name__ == "__main__":
    solve()
