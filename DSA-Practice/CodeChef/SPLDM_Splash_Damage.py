"""
Problem   : Splash Damage (SPLDM)
Link      : https://www.codechef.com/problems/SPLDM
Date      : 2026-09-11
Platform  : CodeChef (START255)
Difficulty: Medium (~1400-1550, Div2/Div3)
Topics    : Greedy, Dynamic Programming, Constructive Algorithms

Approach:
    Each monster (health 1/2/3) is killed either directly or via splash
    damage from a directly-killed neighbor. Model this as choosing a
    subset of monsters to kill directly (cur=1) such that every monster's
    total incoming damage (direct + splash from left/right) meets its
    health. DP state (prev_choice, cur_choice, in_left_damage) tracks
    whether the current monster was chosen and how much splash damage it
    has already absorbed from its left neighbor, enforcing the coverage
    constraint at each transition. Maximize count of directly-killed
    monsters.

    (Note: intended editorial solution is a simpler O(N) greedy: monsters
    with health 3, or health 2 at an endpoint, are "free" and can't die
    to splash; between consecutive free monsters, you're forced to lose
    floor(k/2) monsters to splash, where k = count of health-1 monsters
    in that segment. This DP reformulation reaches the same answer via
    constrained coverage rather than the greedy segment argument.)

Time Complexity : O(N) per test case  -- bounded number of DP states, O(1) transitions
Space Complexity: O(1) extra          -- dp dict has a constant number of live states per layer
"""


# ------------------------------ Solution --------------------------------


import sys

input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        NEG = -10**9
        dp = {}
        for first in (0, 1):
            dp[(0, first, 0)] = first
        for i in range(N - 1):
            ndp = {}
            for (prev, cur, in_left), score in dp.items():
                for nxt in (0, 1):
                    if cur == 1 and nxt == 1:
                        for right_in in (0, 1):
                            if in_left + right_in > A[i] - 1:
                                continue
                            next_in_left = 1 - right_in
                            state = (cur, nxt, next_in_left)
                            new_score = score + nxt
                            if new_score > ndp.get(state, NEG):
                                ndp[state] = new_score
                    else:
                        next_in_left = 0
                        if cur == 1:
                            if in_left > A[i] - 1:
                                continue
                        else:
                            if prev + nxt < A[i]:
                                continue
                        state = (cur, nxt, next_in_left)
                        new_score = score + nxt
                        if new_score > ndp.get(state, NEG):
                            ndp[state] = new_score
            dp = ndp
        answer = NEG
        i = N - 1
        for (prev, cur, in_left), score in dp.items():
            if cur == 1:
                if in_left <= A[i] - 1:
                    answer = max(answer, score)
            else:
                if prev >= A[i]:
                    answer = max(answer, score)
        print(answer)

if __name__ == "__main__":
    solve()
