"""
Problem   : Exun Leaderboard
Platform  : CodeChef (START261A, code: BETWEEN)
Link      : https://www.codechef.com/START261A/problems/BETWEEN
Date      : 2026-10-21
Difficulty: Medium
Topics    : Math, Implementation 

Approach  : Sort the two values so the larger comes first. The positions
            strictly between them number (high - low - 1).

Time      : O(1)
Space     : O(1)
"""


# -------------------------------------------- Solution --------------------------------------------------------------


def solve():
    raw = input().strip().split()
    pair = list(map(int, raw))
    pair.sort(reverse=True)
    high, low = pair[0], pair[1]
    gap = high - low
    return gap - 1

if __name__ == "__main__":
    print(solve())
