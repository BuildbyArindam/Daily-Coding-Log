"""
Problem: 3-cycles (Bipartite Split for Maximum Triangle-Free Graph)
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/41/E
Difficulty: *1900
Date Solved: 2026-09-09
Topics: Constructive Algorithms, Graphs, Greedy

Approach:
Split n cities into two groups of sizes a = n//2 and b = n - a.
Connect every city in group A to every city in group B (complete
bipartite graph). A bipartite graph has no odd cycles, so it's
guaranteed triangle-free (no 3-cycles), and a*b is the maximum
edge count achievable under that constraint for n vertices.

Time Complexity:  O(n^2)  — nested loop prints all a*b edges
Space Complexity: O(1)    — no extra data structures beyond output
"""


# -------------------------- Solution -------------------------------------


n = int(input())
a = n // 2
b = n - a
print(a * b)
for i in range(1, a + 1):
    for j in range(a + 1, n + 1):
        print(i, j)
