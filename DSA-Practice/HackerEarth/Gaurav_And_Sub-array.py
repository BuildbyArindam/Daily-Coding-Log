"""
Problem   : Gaurav And Sub-array
Platform  : HackerEarth (Easy)
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/gaurav-and-subarray-3-787fb90a/
Date      : 2026-10-02
Topics    : Binary Search, Two Pointer, Bit Manipulation

Approach  : Replace each element with its set-bit count (popcount). All values
            are non-negative, so for each query K a sliding window works:
            expand `right`, and while the window sum >= K, record the length
            and shrink from `left`. K == 0 returns 1 (shortest non-empty
            subarray). If no window reaches K, output -1.

Complexity: Time  O(N + Q*N)  (popcount pass + one window sweep per query)
            Space O(N)        (popcount array)
"""


# ------------------------------------ Solution -----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = [x.bit_count() for x in A]
    answers = []
    for _ in range(Q):
        K = int(input())
        if K == 0:
            answers.append(1)
            continue
        left = 0
        current = 0
        min_len = N + 1
        for right in range(N):
            current += B[right]
            while left <= right and current >= K:
                min_len = min(min_len, right - left + 1)
                current -= B[left]
                left += 1
        if min_len == N + 1:
            answers.append(-1)
        else:
            answers.append(min_len)
    sys.stdout.write("\n".join(map(str, answers)))

if __name__ == "__main__":
    solve()
