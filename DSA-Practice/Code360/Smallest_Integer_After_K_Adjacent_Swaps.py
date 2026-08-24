"""
Problem: Smallest Integer After K Adjacent Swaps
Platform: Code360
Link: https://www.naukri.com/code360/problems/smallest-integer-after-k-adjacent-swaps_1459125
Date Solved: 2026-08-24
Difficulty: Hard
Topics: Greedy, Arrays

Approach:
For each position i, look ahead up to k positions (bounded by k and the
remaining string length) and find the smallest digit in that window.
Bring it to position i via adjacent swaps, deducting the number of swaps
used from k. Repeat until k is exhausted or the string is exhausted.

Time Complexity: O(n * k) — for each of n positions, scanning the window
and shifting can cost up to O(k).
Space Complexity: O(n) — list conversion of the input string.
"""


# --------------------------- Solution ----------------------------


def smallestInteger(num, n, k):
    num = list(num)
    for i in range(n):
        end = min(n - 1, i + k)
        min_pos = i
        for j in range(i + 1, end + 1):
            if num[j] < num[min_pos]:
                min_pos = j
        swaps = min_pos - i
        k -= swaps
        while min_pos > i:
            num[min_pos], num[min_pos - 1] = num[min_pos - 1], num[min_pos]
            min_pos -= 1
    return ''.join(num)
