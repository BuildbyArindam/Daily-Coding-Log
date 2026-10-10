"""
Problem   : Weighted String
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/weighted-string/
Date      : 2026-10-10
Difficulty: Medium
Topics    : Binary Search, Sorting, Prefix Sum, Hashing

Approach  : Each character's weight is its alphabet position (a=1 ... z=26).
            Count substrings whose total weight equals K using running prefix
            sums. A substring ending at index i has weight K exactly when some
            earlier prefix sum equals (prefix_sum[i] - K). A hash map stores how
            often each prefix sum has occurred, so every position is handled in
            O(1). Weights are positive, so prefix sums strictly increase and
            this could also be done with binary search or two pointers, but the
            hash map is simpler.

Complexity: Time  O(N) per test case
            Space O(N) for the prefix-sum frequency map
"""


# ------------------------------------------- Solution --------------------------------------------------


T = int(input())

for _ in range(T):
    K = int(input())
    S = input().strip()
    count = 0
    prefix_sum = 0
    freq = {0: 1}
    for ch in S:
        prefix_sum += ord(ch) - ord('a') + 1
        count += freq.get(prefix_sum - K, 0)
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    print(count)
