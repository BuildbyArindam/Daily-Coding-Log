"""
Problem   : Alice, Bob and Chocolate
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/6/C
Difficulty: *1200
Topics    : Greedy, Two Pointers
Date      : 2026-08-17

Approach:
Sort chocolates by weight (input is already given in increasing order
per problem constraints). Use two pointers from both ends — Alice eats
from the lightest end, Bob from the heaviest end. At each step, whichever
of the two has spent less total time picks up the next chocolate on
their side. This greedily keeps their eating times as balanced as
possible, which is exactly what minimizes the number of chocolates left
over (the problem's actual objective, achieved by this balancing rule).

Time Complexity : O(n)      -> single pass with two pointers
Space Complexity: O(1)      -> excluding input storage, only counters used
"""


# --------------------------- SOlution -------------------------


import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    t = [int(x) for x in data[1:]]
    left, right = 0, n - 1
    time_alice = time_bob = 0
    alice_count = bob_count = 0
    while left <= right:
        if time_alice <= time_bob:
            time_alice += t[left]
            alice_count += 1
            left += 1
        else:
            time_bob += t[right]
            bob_count += 1
            right -= 1
    print(f"{alice_count} {bob_count}")

if __name__ == "__main__":
    solve()
