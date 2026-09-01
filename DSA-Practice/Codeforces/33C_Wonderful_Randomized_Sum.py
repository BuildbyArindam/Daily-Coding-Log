"""
Problem: Wonderful Randomized Sum
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/33/C
Difficulty: *1800
Topic: Greedy
Date solved: 2026-09-01

Approach:
Flipping a chosen prefix and suffix (equivalently, negating a contiguous
subarray) means the final sum = total - 2*subarray_sum. To maximize this,
we want to minimize subarray_sum, i.e. find the most negative contiguous
subarray sum (Kadane's algorithm run for minimum, with empty subarray
allowed). Equivalently here we track the maximum subarray sum of the
same array treated for the "best segment to flip" — best = max subarray
sum (Kadane, non-negative floor), and answer = 2*best - total.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# ----------------------- Solution ---------------------------------


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    best = 0
    current = 0
    for x in a:
        current = max(0, current + x)
        best = max(best, current)
    answer = 2 * best - total
    print(answer)

if __name__ == "__main__":
    solve()
