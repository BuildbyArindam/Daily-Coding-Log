"""
Problem   : Palindromic Grid
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/palindromic-grid-e55f3027/
Difficulty: Easy
Topics    : Basic Programming, Implementation, String Manipulation
Date      : 2026-08-16

Approach:
- Count frequency of every character across the grid.
- To make each row and column a palindrome, the grid's cells can be
  grouped into symmetric "quadruples" (4-way mirrored cells), "pairs"
  (cells mirrored along one axis only, for odd N or odd M), and
  possibly a lone center cell (when both N and M are odd).
- quads_needed  = (N//2) * (M//2)
- pairs_needed  = M//2 (if N is odd) + N//2 (if M is odd)
- For each character, count//4 gives usable quadruples and
  (count%4)//2 gives usable pairs.
- Any surplus quadruples beyond quads_needed can be broken down into
  2 pairs each, to help meet pairs_needed.
- If available quadruples and (converted) pairs cover the requirements,
  answer is YES, else NO.

Time complexity : O(N*M) per test case (frequency count + grid scan)
Space complexity: O(K) where K = number of distinct characters (≤ 62)
"""


# --------------------- Solution -----------------------

import sys
from collections import Counter

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        freq = Counter()
        for _ in range(N):
            row = data[idx]
            idx += 1
            freq.update(row)
        quads_needed = (N // 2) * (M // 2)
        pairs_needed = 0
        if N % 2 == 1:
            pairs_needed += M // 2
        if M % 2 == 1:
            pairs_needed += N // 2
        available_quads = 0
        available_pairs = 0
        for count in freq.values():
            available_quads += count // 4
            available_pairs += (count % 4) // 2
        if available_quads >= quads_needed:
            remaining_quads = available_quads - quads_needed
            total_pairs = available_pairs + (remaining_quads * 2)
            if total_pairs >= pairs_needed:
                out.append("YES")
            else:
                out.append("NO")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
