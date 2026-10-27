"""
Problem   : Sum of sum of digits
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/sum-of-sum-of-digits-6/
Date      : 2026-10-27
Difficulty: Easy
Topics    : Sorting, Merge Sort, Implementation, Simulation

Approach  : Reduce each number to its single-digit sum (digital root) in O(1)
            with (v - 1) % 9 + 1, instead of repeatedly summing digits.
            Sort the roots once and build a prefix-sum array. Each query is
            then answered in O(1):
              type 2 -> sum of the k smallest = prefix[k]
              type 1 -> sum of the k largest  = total - prefix[n - k]

Complexity: Time  O(N log N + Q)  (sort + O(1) per query)
            Space O(N)            (roots + prefix sums)
"""


# --------------------------------------------------- Solution -------------------------------------------------------------


import sys
from itertools import accumulate

def collapse(v):
    return (v - 1) % 9 + 1

def run():
    tokens = sys.stdin.buffer.read().split()
    n, q = int(tokens[0]), int(tokens[1])
    roots = sorted(collapse(int(t)) for t in tokens[2:2 + n])
    run_sum = [0] + list(accumulate(roots))
    grand = run_sum[n]
    answers = []
    pos = 2 + n
    for _ in range(q):
        kind = tokens[pos]
        k = int(tokens[pos + 1])
        pos += 2
        if kind == b'2':
            answers.append(run_sum[k])
        else:
            answers.append(grand - run_sum[n - k])
    sys.stdout.write("\n".join(map(str, answers)) + "\n")

if __name__ == "__main__":
    run()
