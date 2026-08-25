"""
Problem   : Little Shino and the tournament
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/little-shino-and-the-tournament/
Date      : 2026-08-25
Difficulty: Easy
Topic     : Basic Programming / Implementation / Simulation

Approach:
  Simulate the single-elimination knockout tournament round by round.
  Each round, pair up adjacent players in the current list; the one with
  higher strength wins and advances, both participants get their fight
  count incremented. A leftover unpaired player (odd count) gets a bye
  and advances without a fight. Repeat until one player remains.
  Answer each query by looking up the precomputed fight_count array.

Time Complexity : O(N + Q) — each player fights O(log N) times across
                   all rounds, but total fights across all rounds sum to
                   O(N), so simulation is linear; queries are O(1) each.
Space Complexity: O(N) — for strengths, fight_count, and round lists.
"""


# ---------------------------- Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    strengths = [int(x) for x in input_data[2:n+2]]
    queries = [int(x) for x in input_data[n+2:n+2+q]]
    fight_count = [0] * (n + 1)
    current_round = [(strengths[i], i + 1) for i in range(n)]
    while len(current_round) > 1:
        next_round = []
        i = 0
        while i < len(current_round):
            if i + 1 < len(current_round):
                f1_strength, f1_idx = current_round[i]
                f2_strength, f2_idx = current_round[i+1]
                fight_count[f1_idx] += 1
                fight_count[f2_idx] += 1
                if f1_strength > f2_strength:
                    next_round.append((f1_strength, f1_idx))
                else:
                    next_round.append((f2_strength, f2_idx))
                i += 2
            else:
                next_round.append(current_round[i])
                i += 1
        current_round = next_round
    out = []
    for query in queries:
        out.append(str(fight_count[query]))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
