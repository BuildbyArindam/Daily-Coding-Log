"""
Problem   : Red and Blue Elements (REDBLUE7)
Contest   : CodeChef START256D
Link      : https://www.codechef.com/START256D/problems/REDBLUE7
Solved on : 2026-09-16
Difficulty: Medium
Topics    : Sorting, Prefix Sums, Greedy, Math

Approach:
  Sort the array. For each possible count of "red" elements (0..n),
  the remaining "blue" balance = n - 2*reds. Depending on the sign of
  the balance, pick the extreme (largest or smallest) `reds` elements
  as the red-sum contribution via prefix sums, then score them as
  red_sum * balance + grand_total * reds. Track the maximum candidate
  score across all values of `reds`.

Time complexity : O(n log n) per test case (dominated by the sort)
Space complexity: O(n) for the prefix sum array
"""


# ---------------------------- Solution -------------------------------------


import sys
from itertools import accumulate

def compute_best(values):
    count = len(values)
    values.sort()
    prefix = [0] * (count + 1)
    running = 0
    for pos, num in enumerate(values):
        running += num
        prefix[pos + 1] = running
    grand_total = running
    top_score = 0
    for reds in range(count + 1):
        balance = count - 2 * reds
        if balance >= 0:
            red_sum = grand_total - prefix[count - reds]
        else:
            red_sum = prefix[reds]
        candidate = red_sum * balance + grand_total * reds
        if candidate > top_score:
            top_score = candidate
    return top_score

def run():
    raw = sys.stdin.buffer.read().split()
    ptr = 0
    tests = int(raw[ptr]); ptr += 1
    results = []
    for _ in range(tests):
        size = int(raw[ptr]); ptr += 1
        nums = [int(x) for x in raw[ptr:ptr + size]]
        ptr += size
        results.append(str(compute_best(nums)))
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    run()
