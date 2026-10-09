"""
Problem   : Penalty Shoot-Out II
Platform  : CodeChef
Link      : https://www.codechef.com/problems/PSHOT
Difficulty: 1735
Topics    : Simulation, Implementation, Greedy
Date      : 2026-10-09

Approach:
    Team A kicks at even indices and team B at odd indices of S, N kicks each.
    After each kick, count the goals scored so far and the kicks each team has
    left. The shoot-out ends as soon as one team's score exceeds the other's
    score plus the other's remaining kicks, since the trailing team can no
    longer catch up. Print the 1-based index of that kick, or 2*N if the
    result is only decided after the last kick.

Complexity:
    Time : O(N) per test case (single pass, early exit)
    Space: O(1) extra (besides storing the input string)
"""


# -------------------------------------------- Solution -------------------------------------------------------


T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()
    a = 0
    b = 0
    ans = 2 * N
    for i in range(2 * N):
        if i % 2 == 0:
            a += int(S[i])
        else:
            b += int(S[i])
        shots_a_left = N - (i + 1 + 1) // 2
        shots_b_left = N - (i + 1) // 2
        if a > b + shots_b_left or b > a + shots_a_left:
            ans = i + 1
            break
    print(ans)
