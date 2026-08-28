"""
Problem: Shil and Survival Game
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/shil-and-survival-game/
Date: 2026-08-28
Difficulty: Easy
Topics: Ad-Hoc, Math, Implementation

Approach:
Scan left-to-right, tracking the running max; whenever an element beats it,
mark its 1-indexed position as a "left-leader". Then scan right-to-left the
same way to mark "right-leaders". The answer is the sorted union of both sets
— survivors are exactly the strength values that are a new maximum from at
least one direction.

Time Complexity: O(n) — two linear passes
Space Complexity: O(n) — for the result set
"""


# --------------------------- Solution -------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    s = [int(x) for x in input_data[1:]]
    ans = set()
    max_so_far = -1
    for i in range(n):
        if s[i] > max_so_far:
            ans.add(i + 1)
            max_so_far = s[i]
    max_so_far = -1
    for i in range(n - 1, -1, -1):
        if s[i] > max_so_far:
            ans.add(i + 1)
            max_so_far = s[i]
    print(*(sorted(ans)))

if __name__ == "__main__":
    solve()
