"""
Problem   : The Glittering Caves of Aglarond
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/LIGHTS
Date      : 2026-09-26
Difficulty: Hard
Topics    : Greedy, Sorting, Parity/Bit Manipulation, Prefix Sums, Constructive Algorithms

Approach:
  - For each row, compute its "lit" count and the net gain in lit
    lights if that row is flipped: gain = width - 2*lit.
  - A row can be flipped multiple times, but flipping it twice cancels
    out, so effectively we choose p rows to actually flip (p <= k),
    where p must have the same parity as k (remaining k-p flips get
    "wasted" in pairs on already-processed rows).
  - Sort gains descending, build a prefix-sum array, then scan all
    valid p (0..min(n,k)) with matching parity to (k) and take the
    max of base_lit + prefix[p].

Time Complexity : O(n log n) per test case (sorting the gains array)
Space Complexity: O(n) per test case (gains array + prefix sums)
"""


# ---------------------------------- Solution -----------------------------------------------


import sys

def read_ints(it):
    return int(next(it)), int(next(it)), int(next(it))

def row_gain(row_str, width):
    lit = row_str.count('*')
    return width - 2 * lit, lit

def best_for_case(gains, base_lit, k, rows):
    limit = min(rows, k)
    gains_sorted = sorted(gains, reverse=True)
    running = 0
    prefix = [0]
    for g in gains_sorted:
        running += g
        prefix.append(running)
    top = None
    p = limit
    while p >= 0:
        if (k - p) % 2 == 0:
            candidate = base_lit + prefix[p]
            if top is None or candidate > top:
                top = candidate
        p -= 1
    return top

def solve():
    data = sys.stdin.read().split()
    ptr = iter(data)
    total_cases = int(next(ptr))
    outputs = []
    for _ in range(total_cases):
        n, m, k = read_ints(ptr)
        gains = []
        base_lit = 0
        for _ in range(n):
            grid_row = next(ptr)
            g, lit = row_gain(grid_row, m)
            gains.append(g)
            base_lit += lit
        outputs.append(str(best_for_case(gains, base_lit, k, n)))
    sys.stdout.write("\n".join(outputs) + "\n")

if __name__ == "__main__":
    solve()
