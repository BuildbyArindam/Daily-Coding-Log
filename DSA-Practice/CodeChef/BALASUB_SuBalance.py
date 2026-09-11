"""
Problem   : SuBalance (BALASUB)
Link      : https://www.codechef.com/problems/BALASUB
Date      : 2026-09-11
Difficulty: Easy-Medium (~1000-1200 CF-equivalent)
Topics    : Arrays, Constructive Algorithms, Greedy, Monotonic Stack

Approach:
    A subarray [l, r] is "balanced" iff it has an equal count of prefix
    maxima and suffix maxima. Key insight: any subarray containing a local
    peak (an element strictly greater than both neighbors) is automatically
    balanced with length 3. Otherwise the array segment is "V-shaped"
    (strictly decreasing then strictly increasing), and a balanced subarray
    exists only between two equal-valued elements with no peak between them.
    This solution scans left to right, using a monotonic decreasing stack to
    track the nearest greater element to the left, and a dict to track the
    last seen index of each value. The first repeated value with no
    intervening peak, or the first local peak found, gives the answer.

Complexity:
    Time : O(N) per test case (each index pushed/popped from stack once)
    Space: O(N) for the stack and last-seen dict
"""


# ------------------------ Solution ------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        answer = None
        last = {}
        stack = []
        for i, x in enumerate(A):
            while stack and A[stack[-1]] <= x:
                stack.pop()
            prev_greater = stack[-1] if stack else -1
            if x in last and last[x] > prev_greater:
                answer = (last[x] + 1, i + 1) 
                break
            if 0 < i < N - 1:
                if A[i] > A[i - 1] and A[i] > A[i + 1]:
                    answer = (i, i + 2)
                    break
            last[x] = i
            stack.append(i)
        if answer is None:
            print(-1)
        else:
            print(answer[0], answer[1])

if __name__ == "__main__":
    solve()
