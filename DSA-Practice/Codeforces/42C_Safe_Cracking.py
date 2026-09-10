"""
Problem: Safe Cracking
Link: https://codeforces.com/problemset/problem/42/C
Platform: Codeforces
Difficulty: *2200
Topics: brute force, constructive algorithms
Date solved: 2026-09-10

Approach:
Greedily pick the largest of the 4 values each round. If it's already
equal to 1 (and thus all values are 1), stop. Otherwise use +i / /i
operations (add 1 to positions i and i+1 mod 4, or halve them) to drive
the largest value down, choosing which pair to operate on based on the
parity of the largest element and its neighbors, so the max value keeps
shrinking. Repeats until all four values equal 1.

Time complexity: O(log(max(a)) * C) - each round roughly halves the
current maximum, bounded by a small constant number of operations
per round (each op appends to `ans`); total output length is bounded
per problem constraints.
Space complexity: O(number of operations) for storing `ans`.
"""


# ---------------------------- Solution --------------------------------


a = list(map(int, input().split()))
ans = []

def add(i):
    """Increase positions i and (i+1)%4."""
    a[i] += 1
    a[(i + 1) % 4] += 1
    ans.append("+" + str(i + 1))

def div(i):
    """Divide positions i and (i+1)%4 by 2."""
    a[i] //= 2
    a[(i + 1) % 4] //= 2
    ans.append("/" + str(i + 1))
while True:
    p = 0
    for i in range(1, 4):
        if a[i] > a[p]:
            p = i
    if a[p] == 1:
        break
    l = (p - 1) % 4
    r = (p + 1) % 4
    if a[p] % 2 == 1:
        if a[l] % 2 == 1:
            add(l)
            div(l)
        elif a[r] % 2 == 1:
            add(p)
            div(p)
        else:
            add(p)
            div(l)
    else:
        if a[l] % 2 == 0:
            div(l)
        elif a[r] % 2 == 0:
            div(p)
        else:
            add(l)
            add(p)
            div(l)
for x in ans:
    print(x)`
