"""
Problem: Strange Town
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/42/D
Difficulty: *2300
Topics: constructive algorithms, math
Date solved: 2026-09-10

Approach:
    Build a Sidon set (a set of n integers where all pairwise sums
    a[i] + a[j], i < j, are distinct) greedily: try candidates
    1, 2, 3, ... and accept a candidate only if adding it to the
    set does not create a duplicate pairwise sum. Use the resulting
    values as edge weights ans[i][j] = a[i] + a[j] for a complete
    graph on n vertices — this guarantees every vertex's set of
    incident edge weights is distinct, and more importantly all
    n*(n-1)/2 edge weights across the graph are pairwise distinct,
    satisfying the "strange town" degree/weight uniqueness constraint.

Complexity:
    Time:  O(n^2) amortized for Sidon set construction (candidates
           needed grow roughly O(n^2), each checked against O(n)
           existing sums) + O(n^2) to build/print the adjacency
           matrix -> overall O(n^2).
    Space: O(n) for the Sidon set, O(n^2) for the output matrix.
"""


# ------------------------- Solution --------------------------------


import sys

def build_sidon_set(n):
    """
    Build n positive integers such that
    a[i] + a[j] are all distinct for i < j.
    """
    a = []
    used_sums = set()
    candidate = 1
    while len(a) < n:
        new_sums = []
        for x in a:
            s = candidate + x
            if s in used_sums or s in new_sums:
                break
            new_sums.append(s)
        else:
            a.append(candidate)
            used_sums.update(new_sums)
        candidate += 1
    return a

def solve():
    n = int(sys.stdin.readline())
    a = build_sidon_set(n)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            ans[i][j] = ans[j][i] = a[i] + a[j]
    for row in ans:
        print(*row)

if __name__ == "__main__":
    solve()
