"""
Problem   : Coins
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/bags-of-coins-7b1d612c/
Difficulty: Easy
Topics    : Algorithms, Binary Search, Searching, Two Pointer
Date      : 2026-10-02

Approach:
    Build a frequency array over coin values (values are bounded by 1e5).
    Sweep the candidate threshold X from 1 to MAX_VAL, maintaining the sum
    and count of coins with value < X (low side). The high side is derived
    from the totals: total - low - equal. If both sides are non-empty and
    their sums match, print YES; if no X works, print NO.

Complexity:
    Time : O(N + M), where M = max coin value (1e5)
    Space: O(M) for the frequency array
"""


# --------------------------------------- Solution ---------------------------------------------------


N = int(input())
A = list(map(int, input().split()))
MAX_VAL = 100000
freq = [0] * (MAX_VAL + 1)
total_sum = 0
for x in A:
    freq[x] += 1
    total_sum += x
low_sum = 0
low_count = 0
for X in range(1, MAX_VAL + 1):
    count_equal = freq[X]
    equal_sum = X * count_equal
    high_sum = total_sum - low_sum - equal_sum
    high_count = N - low_count - count_equal
    if low_count > 0 and high_count > 0 and low_sum == high_sum:
        print("YES")
        break
    low_sum += equal_sum
    low_count += count_equal
else:
    print("NO")
