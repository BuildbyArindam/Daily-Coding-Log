"""
Problem   : Prefixing (FIX)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FIX
Difficulty: 1736
Topics    : Arrays, Hashing
Date      : 2026-10-09

Approach:
    Compute the global maximum of A once. Scan left to right with a set of
    values already seen. The first occurrence of a value is kept as is;
    any repeated value is replaced by the global maximum in the output.

Complexity:
    Time : O(N) per test case (one max pass + one scan, O(1) average set ops)
    Space: O(N) for the set and the output array
"""


# -------------------------------------------- Solution ---------------------------------------------------


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    mx = max(A)
    seen = set()
    B = []
    for x in A:
        if x in seen:
            B.append(mx)
        else:
            B.append(x)
            seen.add(x)
    print(*B)
