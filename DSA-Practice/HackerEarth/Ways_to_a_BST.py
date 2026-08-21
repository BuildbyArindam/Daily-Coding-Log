"""
Problem   : Ways to a BST
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/ways-to-a-bst-54177cac/
Difficulty: Medium
Topics    : Binary Search Tree, Combinatorics, Graphs
Date      : 2026-08-21

Approach:
  Given a sequence representing BST insertion order, count how many
  distinct insertion sequences produce the *same* BST shape.
  - The first element of any (sub)array is always the root of that subtree.
  - Partition the remaining elements into left (< root) and right (> root)
    subsequences — their relative order within each side must be preserved,
    but the two sides can be freely interleaved.
  - Ways for a node = C(left_size + right_size, left_size) * ways(left) * ways(right)
  - Base case: arrays of size <= 2 have exactly 1 way (nothing to interleave).
  - Pascal's triangle is precomputed once (n_max = 1000) so each C(n, k)
    lookup is O(1), and results are taken mod 1e9+7.

Time Complexity : O(n^2) per test case worst case (skewed tree -> recursion
                   splits only one element at a time each level);
                   O(n log n) average for balanced splits.
                   Plus O(n_max^2) one-time cost for the combinatorics table.
Space Complexity: O(n_max^2) for the precomputed Pascal's triangle,
                   O(n) recursion stack per test case.
"""


# ----------------------------- Solution -----------------------------


import sys

sys.setrecursionlimit(2000)
MOD = 10**9 + 7
def precompute_combinations(n_max):
    C = [[0] * (n_max + 1) for _ in range(n_max + 1)]
    for i in range(n_max + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
    return C

def count_ways(arr, C):
    if len(arr) <= 2:
        return 1
    root = arr[0]
    left = [x for x in arr[1:] if x < root]
    right = [x for x in arr[1:] if x > root]
    left_ways = count_ways(left, C)
    right_ways = count_ways(right, C)
    total_elements = len(left) + len(right)
    interleave_ways = C[total_elements][len(left)]
    return (interleave_ways * left_ways % MOD) * right_ways % MOD

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    C = precompute_combinations(1000)
    t = int(input_data[0])
    idx = 1
    output = []
    for _ in range(t):
        n = int(input_data[idx])
        arr = [int(x) for x in input_data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        ans = count_ways(arr, C)
        output.append(str(ans))
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()
