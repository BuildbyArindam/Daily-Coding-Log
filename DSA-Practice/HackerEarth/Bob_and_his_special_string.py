"""
Problem   : Bob and his special string (Bob and the Magical Sword)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/bob-and-the-magical-sword-6c933beb/
Date      : 2026-09-19
Difficulty: Medium
Topics    : Binary Search, Algorithms

Approach:
  Binary search on the answer x = "max group size after splitting each
  character's occurrences into equal-ish chunks of size <= x, using at
  most n total chunks/groups."
  For a candidate x, the number of groups needed for a character with
  frequency f is ceil(f / x). Sum this over all 26 letters — if the
  total groups needed <= n, x is feasible (monotonic property holds:
  larger x -> fewer groups needed), so binary search the smallest
  feasible x.

Time complexity : O(len(s) + 26 * log(max_freq))
Space complexity: O(26) for the frequency array
"""


# --------------------------------- Solution -----------------------------------------


n = int(input())
s = input().strip()
freq = [0] * 26
for ch in s:
    freq[ord(ch) - ord('a')] += 1
def possible(x):
    needed = 0
    for f in freq:
        if f > 0:
            needed += (f + x - 1) // x
            if needed > n:
                return False
    return True

lo = 1
hi = max(freq)
while lo < hi:
    mid = (lo + hi) // 2
    if possible(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)
