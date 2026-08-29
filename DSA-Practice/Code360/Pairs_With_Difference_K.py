"""
Problem: Pairs with difference K
Link: https://www.naukri.com/code360/problems/pairs-with-difference-k_5393
Platform: Code360
Date: 2026-08-29
Difficulty: Medium
Topic: Hashing / Frequency Counting

Approach:
Count frequency of each element in a hash map. For k == 0, count pairs of
equal elements within each frequency group using nC2 = f*(f-1)/2. For k != 0,
for each distinct num, check if num+k exists in the map and add
freq[num] * freq[num+k] to the count (avoids double counting since each
pair (num, num+k) is only checked once from the smaller side).

Time Complexity: O(n) — one pass to build freq map, one pass over distinct keys
Space Complexity: O(n) — hash map storing up to n distinct elements
"""


# ------------------------ Solution ---------------------------------


def printPairDiffK(l, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    freq = {}
    for num in l:
        freq[num] = freq.get(num, 0) + 1
    count = 0
    if k == 0:
        for f in freq.values():
            count += f * (f - 1) // 2
    else:
        for num in freq:
            if num + k in freq:
                count += freq[num] * freq[num + k]
    return count

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
