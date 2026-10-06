"""
Problem   : Zero Xor
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/zero-xor-e3085486/
Difficulty: Medium
Topics    : Arrays, Binary Search, Meet in the Middle, Searching
Date      : 2026-10-06

Approach:
    Meet in the middle. Split the array into two halves and generate the XOR
    of every subset of each half (2^(n/2) values each, including the empty
    subset). A subset of the full array has XOR 0 exactly when its left part
    and right part have equal XORs. Store the right-half XORs in a Counter,
    then for each left-half XOR add its count in the Counter. Subtract 1 at
    the end to remove the empty-empty pair (the empty subset overall).

Complexity:
    Time  : O(2^(n/2)) expected (subset generation + hash lookups)
    Space : O(2^(n/2)) for the two XOR lists and the Counter
"""


# -------------------------------------- Solution ------------------------------------------------


from collections import Counter

n = int(input())
a = list(map(int, input().split()))
mid = n // 2
left = a[:mid]
right = a[mid:]

def get_xors(arr):
    """Generate XOR of every subset, including the empty subset."""
    xors = [0]
    for num in arr:
        xors += [x ^ num for x in xors]
    return xors
left_xors = get_xors(left)
right_xors = get_xors(right)
right_count = Counter(right_xors)
answer = 0
for x in left_xors:
    answer += right_count.get(x, 0)
answer -= 1
print(answer)
