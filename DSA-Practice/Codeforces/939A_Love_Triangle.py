"""
Problem: Love Triangle
Platform: Codeforces
Link: https://codeforces.com/contest/939/problem/A
Date Solved: 2026-08-15
Difficulty: 800 (Div. 2 A)
Topic: Graphs / Functional Graphs (Permutation Cycles)

Approach:
f[i] represents a directed edge i -> f[i] (i "loves" f[i]).
Since f is a permutation, the functional graph decomposes entirely
into disjoint cycles. A "love triangle" exists iff some cycle has
length exactly 3, i.e., f(f(f(i))) == i for some i.
It's enough to check this condition starting from ANY single node
in a cycle — no need to trace the whole cycle explicitly, since if
i belongs to a 3-cycle, i itself will satisfy f[f[f[i]]] == i.

Time Complexity:  O(n)  — single pass over all nodes
Space Complexity: O(n)  — storing the permutation array
"""


# ---------------------- Solution ------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    f = [0] + [int(x) for x in input_data[1:]]
    for i in range(1, n + 1):
        if f[f[f[i]]] == i:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()
