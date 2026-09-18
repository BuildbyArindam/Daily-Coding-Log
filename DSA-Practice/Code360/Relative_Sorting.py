"""
Problem: Relative Sorting
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118822/offering/1382141
Date Solved: 2026-09-18
Difficulty: Medium
Topics: Hashing, Sorting, Arrays

Approach:
Build a frequency map of arr. Iterate through brr, appending each element
to the result as many times as it appears in arr (using the freq map),
then removing it from the map. Any elements left in the map (not present
in brr) are collected, sorted normally, and appended at the end.

Time Complexity: O(n log n) — dominated by sorting the leftover elements
Space Complexity: O(n) — for the frequency map and result array
"""


# ------------------------------- Solution ------------------------------------------


def relativeSorting(arr, brr, n, m):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    result = []
    for num in brr:
        if num in freq:
            result.extend([num] * freq[num])
            del freq[num]
    remaining = []
    for num, count in freq.items():
        remaining.extend([num] * count)
    remaining.sort()
    result.extend(remaining)
    return result
