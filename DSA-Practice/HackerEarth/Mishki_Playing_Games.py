"""
Problem: Mishki Playing Games
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/mishki-playing-games/
Difficulty: Easy
Topic: Ad-Hoc, Basic Programming
Date Solved: 2026-08-25

Approach:
For each element, the number of "moves" to reduce it to 0 (halving) equals
its bit_length (number of times you can right-shift before hitting 0).
Precompute a prefix sum of per-element move counts. For each query [l, r],
the total moves is prefix_moves[r] - prefix_moves[l-1]; if odd, Mishki
(who moves first) makes the last move and wins, else Hacker wins.

Time Complexity: O(N + Q) — O(1) per element for bit_length, O(1) per query
Space Complexity: O(N) for the prefix sum array
"""


# ----------------------- Solution ----------------------------


import sys

def solve():
    def token_generator():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
    tokens = token_generator()
    try:
        n = next(tokens)
        q = next(tokens)
    except StopIteration:
        return
    prefix_moves = [0] * (n + 1)
    for i in range(1, n + 1):
        a_i = next(tokens)
        moves = a_i.bit_length()
        prefix_moves[i] = prefix_moves[i - 1] + moves
    output = []
    for _ in range(q):
        l = next(tokens)
        r = next(tokens)
        
        total_moves = prefix_moves[r] - prefix_moves[l - 1]
        if total_moves % 2 == 1:
            output.append("Mishki")
        else:
            output.append("Hacker")
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
