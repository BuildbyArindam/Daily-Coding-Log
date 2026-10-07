"""
Problem   : Naruto's Punishment
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/subset-problem-1-ce9c4e7b/
Difficulty: Medium
Topics    : Binary Search, Bit Manipulation
Date      : 2026-10-07

Approach  : Meet in the middle.
            Split the array into two halves and generate all subset sums of each
            (2^(N/2) sums per half). Sort the right-half sums. For each left-half
            sum, binary search (bisect_left) for the first right-half sum >= K - left_sum;
            every sum from that index onward completes a valid subset, so add
            len(right_sums) - pos to the answer.

Complexity: Time  - O(N * 2^(N/2))  (sorting and binary searching 2^(N/2) sums)
            Space - O(2^(N/2))      (stored subset sums of both halves)
"""


# ------------------------------------------ Solution -------------------------------------------------


from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
K = int(input())

mid = N // 2
left = A[:mid]
right = A[mid:]

def subset_sums(arr):
    """Generate all subset sums of arr."""
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]
    return sums

right_sums = subset_sums(right)
right_sums.sort()
answer = 0
left_sums = subset_sums(left)
for left_sum in left_sums:
    needed = K - left_sum
    pos = bisect_left(right_sums, needed)
    answer += len(right_sums) - pos
print(answer)
