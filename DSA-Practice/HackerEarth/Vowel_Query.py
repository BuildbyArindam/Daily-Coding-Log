"""
Problem   : Vowel Query
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/vowel-query-51648a6c/
Difficulty: Medium
Topics    : Algorithms, Binary Search, Implementation, Searching
Date      : 2026-10-06

Approach:
    - Store the indices of all vowels in S in a sorted list.
    - Each value x in val selects a part of S: the prefix up to index x if
      x >= 0, otherwise the suffix starting at index |x|.
    - A bisect on the vowel-index list gives the vowel count of each part.
      Prefix sums of these counts form a running total across all parts.
    - For each query K, bisect the prefix sums to find which part holds the
      K-th vowel (-1 if K exceeds the total). A second bisect on the vowel
      list then locates the exact vowel inside that part.

Complexity:
    Time  : O(|S| + (N + Q) log |S| + Q log N)
    Space : O(|S| + N + Q)
"""


# ---------------------------------------- Solution ----------------------------------------------------


from bisect import bisect_left

S = input().strip()
N = int(input())
val = list(map(int, input().split()))
Q = int(input())
queries = list(map(int, input().split()))
vowels = [i for i, ch in enumerate(S) if ch in "aeiou"]
prefix_vowels = []
total = 0
for x in val:
    pos = abs(x)
    if x >= 0:
        cnt = bisect_left(vowels, pos + 1)
    else:
        before = bisect_left(vowels, pos)
        cnt = len(vowels) - before
    total += cnt
    prefix_vowels.append(total)
answers = []
for K in queries:
    if K > total:
        answers.append("-1")
        continue
    idx = bisect_left(prefix_vowels, K)
    previous = prefix_vowels[idx - 1] if idx > 0 else 0
    kth_in_part = K - previous
    x = val[idx]
    pos = abs(x)
    if x >= 0:
        vowel_index = kth_in_part - 1
    else:
        first = bisect_left(vowels, pos)
        vowel_index = first + kth_in_part - 1
    answers.append(S[vowels[vowel_index]])
print("\n".join(answers))
