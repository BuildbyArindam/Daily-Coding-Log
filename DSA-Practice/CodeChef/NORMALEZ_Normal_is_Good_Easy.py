"""
Platform   : CodeChef
Problem    : Normal is Good (Easy) [NORMALEZ]
Link       : https://www.codechef.com/problems/NORMALEZ
Difficulty : 1714
Date       : 2026-09-29
Topics     : Arrays, Run-Length Encoding, Counting

Approach:
    Split the array into maximal runs of equal consecutive elements.
    A run of length k contributes k*(k+1)/2 subarrays consisting of a
    single repeated value. Scan once, tracking the current run length,
    and add its contribution whenever the run ends (and once more after
    the loop for the final run).

Complexity:
    Time  : O(N) per test case
    Space : O(N) for the input array (O(1) extra beyond it)
"""


# ----------------------------------- Solution ----------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = 0
        run = 1
        for i in range(1, N):
            if A[i] == A[i - 1]:
                run += 1
            else:
                ans += run * (run + 1) // 2
                run = 1
        ans += run * (run + 1) // 2
        print(ans)

if __name__ == "__main__":
    solve()
