"""
Problem: Saruman of Many Colours (CBLOCKS)
Link: https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/CBLOCKS
Date Solved: 2026-09-26
Difficulty: Hard
Topics: Greedy, String Processing (Run-Length Encoding), Math (Ceiling Division)

Approach:
    - Compress the string into runs of consecutive equal characters (run-length encoding).
    - Feasibility check: if the longest run is shorter than k, it's impossible -> return -1.
    - Otherwise, greedily split each run into ceil(length / k) pieces and sum these
      counts across all runs to get the minimum total pieces.

Time Complexity:  O(n) per test case, where n = len(s) — single pass to build runs,
                   single pass over runs to sum ceil-divisions.
Space Complexity:  O(n) worst case for storing run lengths (all-distinct-adjacent case
                   gives up to n runs of length 1 each).
"""


# ---------------------------------- Solution -------------------------------------------------


import sys

def solve_case(k, s):
    pieces = []
    longest = 0
    start = 0
    n = len(s)
    for i in range(1, n + 1):
        if i == n or s[i] != s[start]:
            length = i - start
            pieces.append(length)
            if length > longest:
                longest = length
            start = i
    if longest < k:
        return -1
    result = 0
    for length in pieces:
        result += (length + k - 1) // k
    return result

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    pos = 0
    tests = int(tokens[pos])
    pos += 1
    out = []
    for _ in range(tests):
        n = int(tokens[pos])
        k = int(tokens[pos + 1])
        s = tokens[pos + 2].decode()
        pos += 3
        out.append(str(solve_case(k, s)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
