"""
Problem   : Reversal Maximize (REVMX)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/REVMX
Date      : 2026-10-14
Difficulty: Medium
Topics    : Prefix Sums, Sorting, Math

Approach  :
  Reversing a subarray [l, r] sends position i to l + r - i, so an element
  val at index idx becomes a fixed point iff l + r == idx + val and both
  idx and val lie inside [l, r]. Group elements by s = idx + val. For each
  group, sort by low = min(idx, val) descending. When l = low, the
  elements seen so far all fit in [l, s - l], so a running count gives the
  fixed points gained. Subtract the fixed points already inside [l, r]
  (prefix sums) and take the best over all candidates, including no
  reversal.
  Each (s, low) pair is packed into one integer to sort quickly without
  tuples.

Time      : O(N log N) per test case (dominated by sorting)
Space     : O(N)
"""


# ------------------------------------------- Solution --------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    cases = int(tokens[0])
    ptr = 1
    answers = []
    for _ in range(cases):
        n = int(tokens[ptr]); ptr += 1
        arr = tokens[ptr:ptr + n]; ptr += n
        mod = n + 2
        prefix = [0] * (n + 1)
        packed = []
        for idx in range(1, n + 1):
            val = int(arr[idx - 1])
            prefix[idx] = prefix[idx - 1] + (1 if val == idx else 0)
            low = idx if idx < val else val
            packed.append((idx + val) * mod + (mod - low))
        packed.sort()
        total_fixed = prefix[n]
        top = total_fixed
        last_sum = -1
        run = 0
        for item in packed:
            s, rem = divmod(item, mod)
            low = mod - rem
            if s != last_sum:
                last_sum = s
                run = 0
            run += 1
            cand = total_fixed - (prefix[s - low] - prefix[low - 1]) + run
            if cand > top:
                top = cand
        answers.append(top)
    sys.stdout.write("\n".join(map(str, answers)) + "\n")

main()
