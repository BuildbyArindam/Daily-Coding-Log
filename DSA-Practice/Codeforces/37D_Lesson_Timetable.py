"""
Problem: Lesson Timetable
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/37/D
Date: 2026-09-04
Difficulty: *2300
Topics: Combinatorics, DP, Math

Approach:
Split into two independent counting problems and multiply:
  1. First-classroom assignment: labeled groups placed into classrooms
     with given sizes X[i] -> multinomial coefficient N! / (X1! X2! ... XM!).
  2. Second-classroom assignment: each group must get a DIFFERENT classroom
     from its first one, with classroom i having capacity Y[i] for second
     lessons. Process classrooms left to right, tracking dp[r] = number of
     ways so far where r groups are still waiting for a second classroom.
     At each classroom, some of the r waiting groups plus x newly-freed
     groups (j = r + x total) become eligible; choose k of them to fill
     this room's capacity y via C[j][k], leaving j - k still waiting.
     Answer's second-lesson factor is dp[0] after processing all rooms
     (everyone placed), combined via mod arithmetic (MOD = 1e9+7).

Complexity:
  Time:  O(N * max_y) for the DP transitions (binomial table precomputed
         in O(N * max_y)), N = total number of groups (sum of X).
  Space: O(N * max_y) for the Pascal's triangle table C, O(N) for dp/fact
         arrays.
"""


# ----------------------- Solution ----------------------------------------


import sys

MOD = 10**9 + 7
def solve():
    input = sys.stdin.readline
    M = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    N = sum(X)
    max_y = max(Y)
    C = [[0] * (max_y + 1) for _ in range(N + 1)]
    for n in range(N + 1):
        C[n][0] = 1
        for k in range(1, min(n, max_y) + 1):
            if k == n:
                C[n][k] = 1
            else:
                C[n][k] = (C[n - 1][k - 1] + C[n - 1][k]) % MOD
    dp = [0] * (N + 1)
    dp[0] = 1
    s = 0  
    for x, y in zip(X, Y):
        s += x
        new_dp = [0] * (N + 1)
        for r in range(s - x + 1):
            if dp[r] == 0:
                continue
            j = r + x
            upto = min(y, j)
            row = C[j]
            value = dp[r]
            for k in range(upto + 1):
                new_dp[j - k] = (
                    new_dp[j - k] + value * row[k]
                ) % MOD
        dp = new_dp
    second_lesson_ways = dp[0]
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (N + 1)
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    first_lesson_ways = fact[N]
    for x in X:
        first_lesson_ways = first_lesson_ways * inv_fact[x] % MOD
    answer = first_lesson_ways * second_lesson_ways % MOD
    print(answer)

if __name__ == "__main__":
    solve()
