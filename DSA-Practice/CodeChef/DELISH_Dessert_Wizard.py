"""
Platform   : CodeChef
Problem    : Dessert Wizard (DELISH)
Link       : https://www.codechef.com/problems/DELISH
Difficulty : 1804
Topics     : Dynamic Programming, Algorithms
Date       : 2026-10-04

Approach:
    Split the array at every index i into a left part [0..i] and a right part
    [i+1..N-1]. For each part, we want one subarray, and we want to maximise
    the absolute difference between the two subarrays' sums. So the answer is
    the best of:
        (max subarray in left)  - (min subarray in right)
        (max subarray in right) - (min subarray in left)
    Kadane's algorithm gives prefix arrays (left_max / left_min) and suffix
    arrays (right_max / right_min) of the best subarray sums. We then scan
    all split points in one pass.

Complexity:
    Time  : O(N) per test case
    Space : O(N) for the four prefix/suffix arrays
"""


# ------------------------------------------- Solution --------------------------------------------


def solve():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        D = list(map(int, input().split()))
        left_max = [0] * N
        left_min = [0] * N
        cur_max = cur_min = D[0]
        left_max[0] = cur_max
        left_min[0] = cur_min
        for i in range(1, N):
            cur_max = max(D[i], cur_max + D[i])
            cur_min = min(D[i], cur_min + D[i])
            left_max[i] = max(left_max[i - 1], cur_max)
            left_min[i] = min(left_min[i - 1], cur_min)
        right_max = [0] * N
        right_min = [0] * N
        cur_max = cur_min = D[N - 1]
        right_max[N - 1] = cur_max
        right_min[N - 1] = cur_min
        for i in range(N - 2, -1, -1):
            cur_max = max(D[i], cur_max + D[i])
            cur_min = min(D[i], cur_min + D[i])
            right_max[i] = max(right_max[i + 1], cur_max)
            right_min[i] = min(right_min[i + 1], cur_min)
        ans = 0
        for i in range(N - 1):
            ans = max(ans, left_max[i] - right_min[i + 1])
            ans = max(ans, right_max[i + 1] - left_min[i])
        print(ans)

if __name__ == "__main__":
    solve()
