"""
Problem   : Odd Even (ODDEVEN7)
Link      : https://www.codechef.com/problems/ODDEVEN7
Date      : 2026-08-20
Platform  : CodeChef

Approach  :
    A subsequence is "good" if parities alternate (odd, even, odd, ... or
    even, odd, even, ...). To maximize length, interleave the smaller-count
    parity group between elements of the larger-count group. This gives at
    most 2*min(odd_count, even_count) + 1 elements, further capped by N
    (handles the already-balanced case). No sorting/reordering of the array
    is actually needed — only the counts matter.

Complexity:
    Time  : O(N) per test case
    Space : O(1) extra (excluding input storage)
"""


# -------------------------- Solution ---------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd = sum(x % 2 for x in A)
    even = N - odd
    answer = min(N, 2 * min(odd, even) + 1)
    print(answer)
