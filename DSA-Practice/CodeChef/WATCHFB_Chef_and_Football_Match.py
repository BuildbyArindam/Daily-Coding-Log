"""
Platform   : CodeChef
Problem    : Chef and Football Match (WATCHFB)
Link       : https://www.codechef.com/problems/WATCHFB
Difficulty : 1700
Date       : 2026-09-24
Topics     : Ad-hoc, Implementation, Simulation, State tracking

Approach:
    Each update is either an exact score (A, B) or an unordered pair,
    which gives at most two candidates: (A, B) or (B, A). Scores never
    decrease, so a candidate is kept only if some candidate from the
    previous update is <= it in both coordinates. After each update,
    print YES if all surviving candidates agree on the first team's
    score, else NO.

Complexity:
    Time  : O(N) per test case (at most 2 x 2 comparisons per update)
    Space : O(1) (at most 2 candidate states are stored)
"""


# ---------------------------------------- Solution --------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        possible = []
        for i in range(N):
            typ, A, B = map(int, input().split())
            if typ == 1:
                current = [(A, B)]
            else:
                if A == B:
                    current = [(A, B)]
                else:
                    current = [(A, B), (B, A)]
            if i == 0:
                possible = current
            else:
                next_possible = []
                for cf, co in current:
                    for pf, po in possible:
                        if cf >= pf and co >= po:
                            next_possible.append((cf, co))
                            break
                possible = next_possible
            if len({f for f, o in possible}) == 1:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()
