"""
Problem: Team Formation
Platform: CodeChef
Link: https://www.codechef.com/problems/TEAMFOR
Date: 2026-09-29
Difficulty: 1715
Topic: Greedy

Approach:
Classify each person into 00, 01, 10, or 11 based on programming/English skills.
Greedily form as many (10, 01) pairs as possible first.
Then pair remaining people with 11 candidates, since 11 can satisfy both
required skills. Finally, pair the remaining 11 candidates among themselves.

Time Complexity: O(N) per test case
Space Complexity: O(1)
"""


---------------------------------- Solution ---------------------------------------------


Q = int(input())
for _ in range(Q):
    N = int(input())
    S = input().strip()
    T = input().strip()
    a = b = c = d = 0
    for i in range(N):
        if S[i] == '1' and T[i] == '1':
            b += 1
        elif S[i] == '1' and T[i] == '0':
            a += 1
        elif S[i] == '0' and T[i] == '1':
            c += 1
        else:
            d += 1
    teams = 0
    x = min(b, d)
    teams += x
    b -= x
    d -= x
    x = min(a, c)
    teams += x
    a -= x
    c -= x
    remaining = a + c
    x = min(b, remaining)
    teams += x
    b -= x
    remaining -= x
    teams += b // 2
    print(teams)
