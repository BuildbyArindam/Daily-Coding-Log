"""
Problem   : Query on Queues
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/codemonk/4/1505282/
Date      : 2026-09-09
Difficulty: Hard
Topics    : Monotonic Stack, Arrays, Range Queries

Approach:
    For each index i, find the length of the maximal subarray in which
    A[i] is the maximum element (ties broken by treating equal values as
    "not greater", via a "<=" pop condition so each value's span excludes
    other elements equal to it that lie further away).
    - Left pass: monotonic decreasing stack -> distance to previous
      element >= A[i] (exclusive), boundary at -1 if none.
    - Right pass: same idea in reverse -> distance to next element >= A[i].
    - ans[i] = (i - left) + (right - i - 1) = size of the window where
      A[i] is the max.
    Each query just looks up ans[x] in O(1).

Complexity (per test case):
    Time : O(N + K)   -- two linear monotonic-stack passes + O(1) per query
    Space: O(N)        -- stack + answer array
"""


# ------------------------- Solution ---------------------------------


import sys
from array import array

def solve():
    input = sys.stdin.buffer.readline
    write = sys.stdout.buffer.write
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = array('i', map(int, input().split()))
        ans = array('i', [0]) * N
        stack = array('i')
        for i in range(N):
            ai = A[i]
            while stack and A[stack[-1]] <= ai:
                stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1
            ans[i] = i - left
            stack.append(i)
        stack = array('i')
        for i in range(N - 1, -1, -1):
            ai = A[i]
            while stack and A[stack[-1]] <= ai:
                stack.pop()
            if stack:
                right = stack[-1]
            else:
                right = N
            ans[i] += right - i - 1
            stack.append(i)
        out = []
        for _ in range(K):
            x = int(input()) - 1
            out.append(str(ans[x]))
            if len(out) >= 4096:
                write(("\n".join(out) + "\n").encode())
                out.clear()
        if out:
            write(("\n".join(out) + "\n").encode())

if __name__ == "__main__":
    solve()
