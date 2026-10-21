"""
Problem   : Discrepancies in the Voters List (VOTERSDI)
Platform  : CodeChef (ZCO/INOI practice course)
Link      : https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/VOTERSDI
Date      : 2026-10-21
Difficulty: Medium
Topics    : Hashing, Sets, Counting, Sorting

Approach:
    Read the three voter lists as tokens and slice them using the list sizes.
    Convert each list to a set so a repeated ID within one list counts only once.
    Feed the sets into a Counter, so each ID's count is the number of lists
    it appears in. Keep IDs with count >= 2, sort them numerically, and print
    the count followed by the IDs.

Complexity:
    Time  : O(N log N), where N = total IDs across the lists
            (O(N) for hashing and counting, plus sorting the result)
    Space : O(N) for the sets and the counter
"""


# ------------------------------------------ Solution ------------------------------------------------------


import sys
from collections import Counter

def main():
    tokens = sys.stdin.read().split()
    a, b, c = int(tokens[0]), int(tokens[1]), int(tokens[2])
    cuts = (3, 3 + a, 3 + a + b, 3 + a + b + c)
    tally = Counter()
    for lo, hi in zip(cuts, cuts[1:]):
        tally.update(set(tokens[lo:hi]))
    winners = sorted(int(k) for k, v in tally.items() if v >= 2)
    out = [str(len(winners))]
    out.extend(map(str, winners))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
