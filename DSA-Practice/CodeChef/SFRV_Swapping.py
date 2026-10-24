"""
Problem   : Swapping (SFRV)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SFRV
Difficulty: 2012
Topics    : DP, Arrays, Greedy
Date      : 2026-10-24

Approach:
    Let total = sum(i * A[i]) for 1-indexed i. Swapping adjacent elements
    A[k-1] and A[k] changes the total by exactly A[k-1] - A[k], independent
    of everything else. So the answer is total plus the best set of
    non-overlapping adjacent swaps, each worth max(0, A[k-1] - A[k]).
    This is a "pick non-adjacent items" DP:
        dp[k] = max(dp[k-1], dp[k-2] + gain[k])
    Only the last two DP values are kept (rolling variables).

Complexity:
    Time : O(N) per test case
    Space: O(N) for the array (O(1) extra beyond input)
"""


# --------------------------------------- Solution ------------------------------------------------


import sys

def main():
    rd = sys.stdin.buffer.read().split()
    out = []
    ptr = 1
    for _ in range(int(rd[0])):
        n = int(rd[ptr]); ptr += 1
        arr = rd[ptr:ptr + n]; ptr += n
        vals = list(map(int, arr))
        total = 0
        for idx, v in enumerate(vals, 1):
            total += v * idx
        far = 0 
        near = 0  
        for k in range(1, n):
            diff = vals[k - 1] - vals[k]
            cand = far + (diff if diff > 0 else 0)
            far = near
            if cand > near:
                near = cand
        out.append(str(total + near))
    sys.stdout.write("\n".join(out) + "\n")

main()
