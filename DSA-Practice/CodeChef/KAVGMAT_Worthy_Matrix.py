"""
Problem   : Worthy Matrix (KAVGMAT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/KAVGMAT
Difficulty: 1817
Date      : 2026-10-13
Topics    : Binary Search, 2D Prefix Sum

Approach:
    Count square submatrices whose average is >= K. The matrix is sorted
    (non-decreasing along rows and columns), so for a fixed top-left corner,
    growing the square down-right only adds larger values and the average never
    decreases. The valid sizes therefore form a suffix [first, max_len].
    Build a 2D prefix-sum array for O(1) square sums, then binary search the
    smallest valid side length for each top-left corner. Each corner adds
    (max_len - first + 1) squares to the answer.
    Condition checked: square_sum >= K * side^2 (integer math, no floats).

Complexity:
    Time  : O(N * M * log(min(N, M)))
    Space : O(N * M)
"""


# --------------------------------------------- Solution ------------------------------------------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())
        P = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            values = map(int, input().split())
            current = P[i]
            previous = P[i - 1]
            row_sum = 0
            for j, value in enumerate(values, 1):
                row_sum += value
                current[j] = previous[j] + row_sum
        ans = 0
        for i in range(N):
            for j in range(M):
                max_len = min(N - i, M - j)
                lo, hi = 1, max_len
                first = max_len + 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    total = (
                        P[i + mid][j + mid]
                        - P[i][j + mid]
                        - P[i + mid][j]
                        + P[i][j]
                    )
                    if total >= K * mid * mid:
                        first = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1
                if first <= max_len:
                    ans += max_len - first + 1
        print(ans)

if __name__ == "__main__":
    solve()
