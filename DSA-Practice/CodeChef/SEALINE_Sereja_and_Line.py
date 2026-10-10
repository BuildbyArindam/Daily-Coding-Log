"""
Problem   : Sereja and Line (SEALINE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SEALINE
Difficulty: 1806
Topics    : Simulation, Implementation 
Date      : 2026-10-10

Approach:
    Simulate the line directly. People arrive in order 1..n. If a[i] == 0,
    person i+1 joins at the front. Otherwise they join immediately behind
    person a[i]. The cost of each arrival is min(people ahead, people behind),
    since the person can be reached from whichever end is closer.
    Find the insertion index with list.index, add the cost, then insert.

Complexity:
    Time : O(n^2) per test case (list.index and list.insert are each O(n))
    Space: O(n)
"""


# -------------------------------------------- Solution ----------------------------------------------


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    line = []
    ans = 0
    for i in range(n):
        if a[i] == 0:
            pos = 0
        else:
            pos = line.index(a[i]) + 1
        left = pos
        right = len(line) - pos
        ans += min(left, right)
        line.insert(pos, i + 1)
    print(ans)
