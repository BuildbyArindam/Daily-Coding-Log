"""
Problem   : Sum at Even Indices (SAEVI)
Link      : https://www.codechef.com/problems/SAEVI
Date      : 2026-09-09
Platform  : CodeChef
Difficulty: Easy / Cakewalk
Topics    : Arrays, Basic Iteration, Conditional Aggregation

Approach:
    Read array 'a' of size n and threshold 'k'. Compute limit = 2*k.
    Traverse only even indices (0, 2, 4, ...); for each element greater
    than 'limit', add it to a running total. Print the total.

Complexity:
    Time  : O(n)  -> single pass over even indices
    Space : O(n)  -> storage for input array (O(1) extra beyond input)
"""


# -------------------------- Solution -------------------------


n, k = map(int, input().split())
a = list(map(int, input().split()))
limit = 2 * k
total = 0
for i in range(0, n, 2):
    if a[i] > limit:
        total += a[i]
print(total)
