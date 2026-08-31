"""
Problem: Permutation Swaps
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/guess-permutation-2-be0b2b90/
Date: 2026-08-31
Difficulty: Easy
Topics: Linear Search, Algorithms, Greedy Algorithm

Approach:
Check if array A can be rearranged into a valid permutation of 1..N
under the constraint of prefix sums. First verify the total sum matches
N*(N+1)/2 (necessary condition for a valid permutation of 1..N). Then
greedily check, for every prefix of length k, that the prefix sum is
at least the minimum possible sum of any k distinct values from 1..N
(i.e., 1+2+...+k). If any prefix falls short, it's impossible; otherwise
it's achievable.

Time Complexity: O(N) per test case
Space Complexity: O(1) extra (excluding input storage)
"""


# --------------------------- Solution ------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    MAXV = 50
    OFFSET = 50
    SIZE = 51
    left = [[0] * (SIZE + 1) for _ in range(101)]
    right = [[0] * (SIZE + 1) for _ in range(101)]
    def update_left(d, x, val):
        tree = left[d + OFFSET]
        p = x + 1
        while p <= SIZE:
            if val > tree[p]:
                tree[p] = val
            p += p & -p
    def query_left(d, x):
        tree = left[d + OFFSET]
        p = x + 1
        res = 0
        while p:
            if tree[p] > res:
                res = tree[p]
            p -= p & -p
        return res
    def update_right(s, x, val):
        tree = right[s]
        p = SIZE - x
        while p <= SIZE:
            if val > tree[p]:
                tree[p] = val
            p += p & -p
    def query_right(s, x):
        tree = right[s]
        p = SIZE - x
        res = 0
        while p:
            if tree[p] > res:
                res = tree[p]
            p -= p & -p
        return res
    first = a[0]
    update_left(-first, first, 1)   
    update_right(first, first, 1)
    answer = 1
    for i in range(1, n):
        v = a[i]
        cur = [0] * (k + 1)
        for c in range(k + 1):
            best = 0
            d = c - v
            x = v
            q = query_left(d, x)
            if q > best:
                best = q
            s = c + v
            q = query_right(s, v)
            if q > best:
                best = q
            if best:
                cur[c] = best + 1
                if cur[c] > answer:
                    answer = cur[c]
        for c, length in enumerate(cur):
            if length:
                update_left(c - v, v, length)
                update_right(c + v, v, length)
    print(answer)

if __name__ == "__main__":
    solve()
