"""
Problem   : The Momentum Ledger
Platform  : Unstop (Hard)
Link      : https://unstop.com/code/practice/661278
Date      : 2026-10-02
Topics    : Monotonic Stack, Hashing, Sorting / Top-K

Approach
--------
1. Group entry indices by team using a hash map, so each team's entries
   keep their original order.
2. For each team, scan its positions right to left with a monotonic stack
   (pop while stack top rating <= current). The stack top is then the next
   strictly greater rating, and wait = next_idx - idx. Otherwise wait = -1.
3. Keep only entries with a finite wait, sort by (wait desc, index asc),
   and take the first K as 1-based positions for the leaderboard.

Complexity
----------
Time  : O(n + m log m), where m = entries with a finite wait (m <= n).
        Grouping and the stack passes are O(n) total; the sort is the bottleneck.
        (A heap-based top-K would give O(n + m log K).)
Space : O(n) for the team map, wait array and stacks.
"""


# --------------------------------------- Solution ----------------------------------------------------


def user_logic(n, K, entries):
    teams = {}
    for i, (team, rating) in enumerate(entries):
        teams.setdefault(team, []).append(i)
    wait_values = [-1] * n
    for positions in teams.values():
        stack = []
        for idx in reversed(positions):
            rating = entries[idx][1]
            while stack and entries[stack[-1]][1] <= rating:
                stack.pop()
            if stack:
                next_idx = stack[-1]
                wait_values[idx] = next_idx - idx
            stack.append(idx)
    finite_positions = [i for i, w in enumerate(wait_values) if w != -1]
    finite_positions.sort(key=lambda i: (-wait_values[i], i))
    leaderboard_positions = [i + 1 for i in finite_positions[:K]]
    return wait_values, leaderboard_positions

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    K = int(data[1])
    entries = [
        (int(data[i * 2 + 2]), int(data[i * 2 + 3]))
        for i in range(n)
    ]
    wait_values, leaderboard_positions = user_logic(n, K, entries)
    print(" ".join(map(str, wait_values)))
    print(" ".join(map(str, leaderboard_positions)))

if __name__ == "__main__":
    main()
