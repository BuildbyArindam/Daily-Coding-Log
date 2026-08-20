"""
Problem   : Mirror Swap (MRSWAP)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MRSWAP
Date      : 2026-08-20
Difficulty: Easy (Div 3/4, ~800-1000 rated)
Topics    : Greedy, Arrays

Approach:
Array has length 2N; the only allowed operation swaps A[i] with its
mirror A[2N-1-i]. This means position i can only ever end up holding
either A[i] or A[2N-1-i] — nothing else. So to maximize the sum of the
first N elements, independently pick the larger of each mirror pair
(A[i], A[2N-1-i]) for i = 0..N-1 and sum them.

Time Complexity : O(N) per test case
Space Complexity: O(N) for storing the array (O(1) extra beyond input)
"""


# ------------------------ Solution --------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i], A[2 * N - 1 - i])
    print(ans)
