"""
Problem   : Magic Potion
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/magic-potion-d54349f9/
Difficulty: Medium
Topics    : Algorithms, Binary Search, Searching
Date      : 2026-10-06

Approach:
    Prefix sums with a hash map. For each prefix sum P, a subarray ending
    here sums to K if (P - K) was seen earlier.
      - freq[x]  : how many times prefix sum x has occurred, which gives
                   the number of valid subarrays.
      - first[x] : earliest index where prefix sum x occurred, which gives
                   the longest valid subarray ending at i.
    Output is the total count and N - (longest valid length).

Complexity:
    Time  : O(N), one pass with O(1) average dict operations
    Space : O(N), for the freq and first dictionaries
"""


# --------------------------------------- Solution ---------------------------------------------------


N, K = map(int, input().split())
A = list(map(int, input().split()))
freq = {0: 1}
first = {0: 0}
prefix = 0
count = 0
max_length = 0
for i in range(1, N + 1):
    prefix += A[i - 1]
    needed = prefix - K
    if needed in freq:
        count += freq[needed]
        length = i - first[needed]
        max_length = max(max_length, length)
    freq[prefix] = freq.get(prefix, 0) + 1
    if prefix not in first:
        first[prefix] = i
print(count, N - max_length)
