"""
Problem   : Far Swapping (Ver 2)
Platform  : CodeChef (START256D)
Link      : https://www.codechef.com/START256D/problems/FARSWAP
Solved on : 2026-09-16
Difficulty: Hard
Topics: Combinatorics, Dynamic Programming, Permutations, Prefix Sums, Descent/Ascent-pattern counting

Approach:
  For each value v in [1, n-1], determine whether position(v) < position(v+1)
  in the given permutation (an "ascent" in value space). This ascent/descent
  signature is the invariant preserved by far-swap operations. Count the
  number of permutations of [1..n] matching this exact signature using an
  O(n) rank-array + prefix-sum DP per step (classic descent-pattern counting).

Time complexity  : O(n^2)   -- n steps, each doing an O(n) prefix-sum pass
Space complexity : O(n)     -- rank array grows up to size n
"""


# ------------------------------ Solution --------------------------------------


import sys
from itertools import accumulate
MOD = 998244353

def count_reachable(n, perm):
    location = [0] * (n + 1)
    for idx, value in enumerate(perm, start=1):
        location[value] = idx
    ranks = [1]
    for v in range(1, n):
        goes_up = location[v] < location[v + 1]
        running = list(accumulate(ranks))
        grand_total = running[-1] if running else 0
        extended = [0] + running
        if goes_up:
            ranks = extended
        else:
            ranks = [grand_total - piece for piece in extended]
        ranks = [piece % MOD for piece in ranks]
    return sum(ranks) % MOD

def main():
    raw = sys.stdin.buffer.read().split()
    pointer = 0
    cases = int(raw[pointer]); pointer += 1
    answers = []
    for _ in range(cases):
        n = int(raw[pointer]); pointer += 1
        perm = raw[pointer:pointer + n]; pointer += n
        perm = list(map(int, perm))
        answers.append(str(count_reachable(n, perm)))
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    main()
