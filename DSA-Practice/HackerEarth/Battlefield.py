"""
Problem   : Battlefield
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/battlefield-13/
Date      : 2026-08-29
Difficulty: Medium (site) / Easy (personal rating)
Topics    : Sliding Window, Circular Array, String Manipulation, Frequency Counting

Approach:
- Count k = number of 'K' characters in the string (this fixes the window size,
  since every soldier must occupy a contiguous block once rearranged).
- Duplicate the string (s + s) to simulate wrap-around / circular positions.
- Slide a fixed-size window of length k across the doubled string, maintaining
  a running count of 'D' characters inside the window via add/remove at the
  boundaries (no recomputation from scratch each shift).
- The minimum 'D' count over all n valid window positions is the answer,
  since each 'D' inside the window represents one swap needed to convert it
  to 'K'.

Time complexity : O(n) per test case (each character enters/leaves window once)
Space complexity: O(n) for the doubled string
"""


# --------------------------- Solution ---------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx + 1]
        idx += 2
        k_count = s.count('K')
        if k_count <= 1:
            out.append(0)
            continue
        s_double = s + s
        current_d_count = 0
        for i in range(k_count):
            if s_double[i] == 'D':
                current_d_count += 1
        min_swaps = current_d_count
        for i in range(1, n):
            if s_double[i - 1] == 'D':
                current_d_count -= 1
            if s_double[i + k_count - 1] == 'D':
                current_d_count += 1
            if current_d_count < min_swaps:
                min_swaps = current_d_count
        out.append(min_swaps)
    print('\n'.join(map(str, out)))

if __name__ == '__main__':
    solve()
