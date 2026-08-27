"""
Problem   : Minimum number of Flips (MINFLIPS)
Link      : https://www.codechef.com/problems/MNFLP
Date      : 2026-08-27
Difficulty: Cakewalk / ~800 (CodeChef rating)
Topics    : Basic Math, Parity, Greedy, Implementation

Approach:
Each array element is +1 or -1. One operation flips the sign of any
single element. To make the total sum 0, note that for N elements
each ±1, sum(A) always has the same parity as N. So:
  - If N is odd -> sum is always odd -> sum 0 is impossible -> -1
  - If N is even -> answer = |sum(A)| / 2
    (each flip changes the sum by exactly 2, so we need enough flips
    to cancel out the imbalance between +1s and -1s)

Time complexity : O(N) per test case (single pass to compute sum)
Space complexity: O(N) to store the array (O(1) extra beyond input)
"""


# ----------------------- Solution ----------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        A = [int(x) for x in data[idx + 1 : idx + 1 + N]]
        idx += 1 + N
        if N % 2 != 0:
            results.append("-1")
        else:
            total_sum = sum(A)
            results.append(str(abs(total_sum) // 2))
    print("\n".join(results))

if __name__ == "__main__":
    solve()
