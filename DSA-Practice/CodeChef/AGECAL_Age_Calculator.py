"""
Problem   : Age Calculator (AGECAL)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/AGECAL
Difficulty: 1724
Topics    : Implementation, Math, Prefix Sums
Date      : 2026-10-02

Approach  : Convert each date to an absolute day number in a custom calendar.
            Build a prefix sum over the month lengths so the days elapsed
            before any month come from a single lookup. Day number =
            full years * days per year + leap days from earlier years
            (every 4th year) + days in earlier months + (day - 1).
            The age in days is current - birth + 1 (inclusive count).

Time      : O(N) per test case (prefix sum build; each date conversion is O(1))
Space     : O(N) for the prefix array
"""


# ---------------------------------------- Solution ----------------------------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    answers = []
    for _ in range(T):
        N = int(input())
        a = list(map(int, input().split()))
        pref = [0] * (N + 1)
        for i in range(N):
            pref[i + 1] = pref[i] + a[i]
        year_days = pref[N]
        yb, mb, db = map(int, input().split())
        yc, mc, dc = map(int, input().split())
        def day_number(y, m, d):
            days = (y - 1) * year_days
            days += (y - 1) // 4
            days += pref[m - 1]
            days += d - 1
            return days
        birth = day_number(yb, mb, db)
        current = day_number(yc, mc, dc)
        answers.append(str(current - birth + 1))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
