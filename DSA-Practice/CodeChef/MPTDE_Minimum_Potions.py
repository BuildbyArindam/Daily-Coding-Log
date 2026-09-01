"""
Problem   : Minimum Potions
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MPTDE
Date      : 2026-09-01
Difficulty: Medium
Topics: Dynamic Programming, Greedy

Approach:
    DP over the number of potions used (0..K). For each monster (cost),
    we track, for every potion-count k, the minimum "pot" (a secondary
    priority — likely representing something like turns/rounds) and the
    maximum leftover stamina achievable with exactly k potions used so far.
    Transitions per monster:
      1. Skip fighting (carry state forward, k -> k+1 potion slot reserved)
      2. Fight without a potion (if stamina >= cost)
      3. Use a potion to refill stamina to S before fighting (if cost <= S)
    Answer is the minimum "pot" value across all potion counts after
    processing all monsters.

Time complexity : O(N * K)
Space complexity: O(K)   (rolling arrays pot[] / stamina[])
"""


# ------------------------ Solution ----------------------------------


import sys

def solve():
    input = sys.stdin.readline
    N, S, K = map(int, input().split())
    costs = list(map(int, input().split()))
    INF = 10**9
    pot = [INF] * (K + 1)
    stamina = [-1] * (K + 1)
    pot[0] = 0
    stamina[0] = S
    for cost in costs:
        new_pot = [INF] * (K + 1)
        new_stamina = [-1] * (K + 1)
        for k in range(K + 1):
            if pot[k] == INF:
                continue
            if k < K:
                p = pot[k]
                st = stamina[k]
                if p < new_pot[k + 1]:
                    new_pot[k + 1] = p
                    new_stamina[k + 1] = st
                elif p == new_pot[k + 1]:
                    new_stamina[k + 1] = max(new_stamina[k + 1], st)
            if stamina[k] >= cost:
                p = pot[k]
                st = stamina[k] - cost
                if p < new_pot[k]:
                    new_pot[k] = p
                    new_stamina[k] = st
                elif p == new_pot[k]:
                    new_stamina[k] = max(new_stamina[k], st)
            if cost <= S:
                p = pot[k] + 1
                st = S - cost
                if p < new_pot[k]:
                    new_pot[k] = p
                    new_stamina[k] = st
                elif p == new_pot[k]:
                    new_stamina[k] = max(new_stamina[k], st)
        pot = new_pot
        stamina = new_stamina
    ans = min(pot)
    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    solve()
