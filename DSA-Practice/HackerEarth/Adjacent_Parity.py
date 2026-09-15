"""
Problem: Adjacent Parity
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/adjacent-parity-10c93d7a/
Platform: HackerEarth
Date Solved: 2026-09-15
Difficulty: Easy
Topic: Linear Search, Algorithms, Greedy

Approach:
Count even and odd elements in the array. If either count is 0, or the
counts differ by at most 1, it's possible to arrange the array so no two
adjacent elements have the same parity (alternate evens and odds). Otherwise
it's impossible — greedy/counting argument, no actual arrangement needed.

Time Complexity:  O(N) per test case (single pass to count parities)
Space Complexity: O(1) extra (excluding input storage)
"""


# ------------------------- Solution -----------------------------------------


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    even = sum(1 for x in A if x % 2 == 0)
    odd = N - even
    if even == 0 or odd == 0 or abs(even - odd) <= 1:
        print("YES")
    else:
        print("NO")
