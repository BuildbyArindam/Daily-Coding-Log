"""
Problem   : Equal Strings
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-strings-79789662-4dbd707c/
Date      : 2026-09-02
Difficulty: Medium
Topic     : Algorithms, Linear Search, Dynamic Programming

Approach:
    1. Scan s and t once to collect all indices `pos[]` where s[i] != t[i].
    2. If the mismatch count `m` is odd, it's impossible to equalize -> answer -1.
    3. If m == 0, strings are already equal -> answer 0.
    4. Otherwise, mismatches must be resolved in pairs. Use a rolling DP
       (prev2, prev1) over pos[] where, for each new mismatch i, we choose
       the cheaper of:
           - pairing it with the immediately preceding unpaired mismatch
             using a fixed-cost operation `x`, or
           - pairing it with the mismatch two steps back, at cost
             2 * (pos[i-1] - pos[i-2]) (distance-based cost).
       This is a classic "minimum cost to pair up points on a line" DP.
    5. Final answer is dp[m] // 2 (cost normalized after pairing).

Time complexity : O(n) per test case (scan + O(m) DP, m <= n)
Space complexity: O(m) for storing mismatch positions (O(1) extra for the DP itself)
"""


# ---------------------------- Solution ---------------------------------


import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    tc = int(next(it))
    ans = []
    for _ in range(tc):
        n = int(next(it))
        x = int(next(it))
        s = next(it).decode()
        t = next(it).decode()
        pos = []
        for i in range(n):
            if s[i] != t[i]:
                pos.append(i)
        m = len(pos)
        if m % 2 == 1:
            ans.append("-1")
            continue
        if m == 0:
            ans.append("0")
            continue
        prev2 = 0    
        prev1 = x   
        for i in range(2, m + 1):
            d = pos[i - 1] - pos[i - 2]
            cur = min(
                prev1 + x,
                prev2 + 2 * d
            )
            prev2 = prev1
            prev1 = cur
        ans.append(str(prev1 // 2))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
