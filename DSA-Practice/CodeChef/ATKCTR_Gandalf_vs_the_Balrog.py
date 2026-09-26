"""
Problem   : Gandalf vs the Balrog (ATKCTR)
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/ATKCTR
Date      : 2026-09-26
Difficulty: Hard
Topics    : Greedy, Constructive Algorithms

Approach:
  For each test case, build a net-effect array `change[1..n]` from the m
  directed pairs (x, y): change[x] -= 1, change[y] += 1 (i.e. accumulate
  each index's in-count minus out-count, without any range propagation).
  Then scan attack = 1..n for the point where change[attack] == attack - n,
  i.e. (n - attack) + change[attack] == 0, and answer "2 attack" there;
  if no such point exists, answer "1".

Complexity:
  Time  : O(n + m) per test case  ->  O(sum(n + m)) overall
  Space : O(n) per test case for the change array
"""


# ------------------------------------------ Solution -----------------------------------------------------


import sys
from array import array

def solve_case(n, pairs):
    change = array('i', [0]) * (n + 1)
    for x, y in pairs:
        change[x] -= 1
        change[y] += 1
    for attack in range(1, n + 1):
        if (n - attack) + change[attack] == 0:
            return f"2 {attack}"
    return "1"

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    test_cases = values[pos]
    pos += 1
    answers = []
    for _ in range(test_cases):
        n = values[pos]
        m = values[pos + 1]
        pos += 2
        pairs = []
        for _ in range(m):
            x = values[pos]
            y = values[pos + 1]
            pos += 2
            pairs.append((x, y))
        answers.append(solve_case(n, pairs))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
