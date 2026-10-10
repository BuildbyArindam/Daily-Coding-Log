"""
Platform   : CodeChef
Problem    : Maximize Subarray Difference (MXSBDF)
Link       : https://www.codechef.com/problems/MXSBDF
Difficulty : 1804
Topics     : Kadane's Algorithm, Prefix/Suffix DP
Date       : 2026-10-10

Approach:
  Pick two non-overlapping subarrays and maximize |sum1 - sum2|.
  1. Run Kadane from the left and right to get the max/min subarray sum
     ending (or starting) at each index.
  2. Take prefix best-of-max/min for the left side and suffix
     best-of-max/min for the right side.
  3. For each split point i, the answer candidates are
     |left_max[i] - right_min[i+1]| and |left_min[i] - right_max[i+1]|.
     Take the maximum over all splits.

Time  : O(N) per test case
Space : O(N)
"""


# ------------------------------------------- Solution -------------------------------------------------------


def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        max_end = [0] * N
        min_end = [0] * N
        max_start = [0] * N
        min_start = [0] * N
        max_end[0] = min_end[0] = A[0]
        for i in range(1, N):
            max_end[i] = max(A[i], max_end[i - 1] + A[i])
            min_end[i] = min(A[i], min_end[i - 1] + A[i])
        max_start[N - 1] = min_start[N - 1] = A[N - 1]
        for i in range(N - 2, -1, -1):
            max_start[i] = max(A[i], A[i] + max_start[i + 1])
            min_start[i] = min(A[i], A[i] + min_start[i + 1])
        left_max = [0] * N
        left_min = [0] * N
        right_max = [0] * N
        right_min = [0] * N
        left_max[0] = max_end[0]
        left_min[0] = min_end[0]
        for i in range(1, N):
            left_max[i] = max(left_max[i - 1], max_end[i])
            left_min[i] = min(left_min[i - 1], min_end[i])
        right_max[N - 1] = max_start[N - 1]
        right_min[N - 1] = min_start[N - 1]
        for i in range(N - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], max_start[i])
            right_min[i] = min(right_min[i + 1], min_start[i])
        ans = 0
        for i in range(N - 1):
            ans = max(
                ans,
                abs(left_max[i] - right_min[i + 1]),
                abs(left_min[i] - right_max[i + 1])
            )
        print(ans)

if __name__ == "__main__":
    solve()
