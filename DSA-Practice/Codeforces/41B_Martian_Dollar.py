"""
Problem: Martian Dollar
Link: https://codeforces.com/problemset/problem/41/B
Platform: Codeforces
Difficulty: *1400
Date solved: 2026-09-09
Topic: Brute Force

Approach:
For each possible "buy day" i, convert all Bs (Martian dollars) into As
(the exchange rate on day i), keeping the leftover Bs that don't divide
evenly. Then try selling on every later day j > i, converting the As
back into Bs at day j's rate. Track the maximum Bs obtainable across
all (i, j) pairs, including doing nothing (just holding the original b).

Time Complexity:  O(n^2)  -- nested loop over all (buy day, sell day) pairs
Space Complexity: O(n)    -- storing the array of exchange rates (O(1) extra)
"""


# ----------------------- Solution ------------------------------


n, b = map(int, input().split())
a = list(map(int, input().split()))
ans = b
for i in range(n):
    dollars = b // a[i]
    remaining = b % a[i]
    for j in range(i + 1, n):
        money = remaining + dollars * a[j]
        ans = max(ans, money)
print(ans)
