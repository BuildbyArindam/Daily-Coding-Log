"""
Problem   : Troubling Triple
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/troubling-triple/
Difficulty: Medium
Topics    : Algorithms, Binary Search, Sorting
Date      : 2026-10-09

Approach  : Count triplets (i < j < k) whose product is <= K.
            Sort the array, then fix the smallest element at index i and use
            two pointers (left = i+1, right = N-1) on the remaining suffix.
            - If product <= K, every index between left and right works with
              `left` (the array is sorted), so add (right - left) and move
              left forward.
            - Otherwise the product is too large, so move right backward.

Complexity: Time  - O(N log N) for the sort + O(N^2) for the two-pointer scan
                    = O(N^2) overall
            Space - O(1) extra (in-place sort)

Note      : The two-pointer monotonicity relies on values being non-negative.
"""


# ----------------------------------------- Solution -------------------------------------------------


name = input()    
N, K = map(int, name.split())
values = list(map(int, input().split()))
values.sort()
count = 0
for i in range(N - 2):
    left = i + 1
    right = N - 1
    while left < right:
        product = values[i] * values[left] * values[right]
        if product <= K:
            count += right - left
            left += 1
        else:
            right -= 1
print(count)    
