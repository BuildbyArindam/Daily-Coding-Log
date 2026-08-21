"""
Problem   : Hackers with Bits
Platform  : HackerEarth
Link      : http://hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/hack-the-string-9dce7834/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-21

Approach:
Brute-force over all possible single-swap pairs (i, j) in the array.
For each pair, swap the elements, compute the longest run of consecutive
1s in the resulting array, then swap back (undo) and move to the next
pair. Track the maximum run length seen across all swaps (including the
no-op case i == j, which preserves the original array's best run).

Time complexity : O(n^3)
  - O(n^2) pairs (i, j), each requiring an O(n) scan for the longest
    run of 1s.
Space complexity: O(1) extra (in-place swaps; ignoring O(n) input storage)
"""


# ---------------------------- Solution ------------------------------


import sys

def max_consecutive_ones(arr):
    max_len = 0
    current_len = 0
    for x in arr:
        if x == 1:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    return max_len

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:1 + n]]
    ans = 0
    for i in range(n):
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            ans = max(ans, max_consecutive_ones(arr))
            arr[i], arr[j] = arr[j], arr[i]  
    print(ans)

if __name__ == '__main__':
    solve()
