"""
Problem   : Alice and String Game (String Game)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/alice-and-string-game-dbd6adc3/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-19

Approach:
    For each test string, count the number of distinct characters.
    If the distinct-character count is odd, Player1 wins; if even, Player2 wins.
    (Game-theory result reduces to a simple parity check on set size.)

Time Complexity : O(N) per test case, where N = length of string
                   (building the set is O(N); overall O(sum of N) across T cases)
Space Complexity: O(K) per test case, where K = number of distinct characters (≤ 26 for lowercase)
"""


# ---------------------- Solution ---------------------------


import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        s = data[i]
        distinct_chars = len(set(s))
        results.append("Player1" if distinct_chars % 2 != 0 else "Player2")
    print("\n".join(results))

if __name__ == '__main__':
    solve()
