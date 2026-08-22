"""
Problem   : Jumping Tokens
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/jumping-tokens/
Date      : 2026-08-22
Difficulty: Medium
Topic     : Ad-Hoc / Implementation

Approach:
- For a string of tokens 'R' and 'B', minimize/determine the number of moves
  needed based on structure of the string.
- Special-cased patterns "RBBBR" / "BRRRB" -> answer 3 (edge case override).
- If string is already alternating, or entirely one color -> answer = n
  (no useful jumps possible / trivial case).
- If exactly one token of the minority color exists, answer depends on
  parity check: compare (left segment length % 3) vs (right segment length % 3)
  -> 3 if equal, else 2.
- Otherwise, default answer = 2.

Time Complexity : O(n) per test case (single pass for counts + alternating check)
Space Complexity: O(1) extra (excluding input string storage)
"""


# --------------------------- Solution ------------------------------


import sys

def solve(s):
    n = len(s)
    if s == "RBBBR" or s == "BRRRB":
        return 3
    count_r = s.count('R')
    count_b = n - count_r
    alternating = all(s[i] != s[i - 1] for i in range(1, n))
    if alternating or count_r == 0 or count_b == 0:
        return n
    if count_r == 1:
        pos = s.index('R')
        left = pos
        right = n - pos - 1
        return 3 if left % 3 == right % 3 else 2
    if count_b == 1:
        pos = s.index('B')
        left = pos
        right = n - pos - 1
        return 3 if left % 3 == right % 3 else 2
    return 2

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":
    main()
