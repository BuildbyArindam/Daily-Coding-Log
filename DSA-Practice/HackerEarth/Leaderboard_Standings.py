"""
Problem   : Leaderboard Standings
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/leaderboard-standings-863c4cc2/
Difficulty: Easy
Topic     : Algorithms, Hash Maps, Sorting
Date      : 2026-08-16

Approach:
    Read all (username, time_taken) submission pairs. For each user, track
    total solve count and cumulative time using two hash maps (defaultdict).
    Build a list of (-solve_count, total_time, username) tuples per user and
    sort it: this ranks by highest solve count first (negated for ascending
    sort), then lowest total time as tiebreaker. Assign ranks 1..N in that
    sorted order.

Time complexity : O(N log N)  -> N submissions read in O(N), then sorting the
                                  distinct-user list dominates.
Space complexity: O(U)        -> U = number of distinct usernames, for the
                                  two hash maps and the contestants list.
"""


# ------------------------- Solution --------------------------


from collections import defaultdict
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    solve_count = defaultdict(int)
    total_time = defaultdict(int)
    idx = 1
    for _ in range(n):
        username = input_data[idx]
        time_taken = int(input_data[idx + 1])
        idx += 2
        solve_count[username] += 1
        total_time[username] += time_taken
    contestants = []
    for username in solve_count:
        contestants.append((-solve_count[username], total_time[username], username))
    contestants.sort()
    results = []
    for rank, (_, _, username) in enumerate(contestants, start=1):
        results.append(f"{rank} {username}")
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
