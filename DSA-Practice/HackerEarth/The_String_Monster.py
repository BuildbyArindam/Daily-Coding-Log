"""
Problem   : The String Monster
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/the-string-monster-july-easy/
Difficulty: Medium
Topics    : Algorithms, Meet in the Middle, Hashing
Date      : 2026-10-08

Approach:
    Each string is reduced to a 26-length letter-count vector. The question is
    whether some subset of strings has a combined count equal to the target's.
    Brute force over 2^N subsets is too slow, so use meet in the middle:
      1. Split the strings into two halves.
      2. For each half, build the set of all reachable subset-sum vectors,
         pruning any vector that exceeds the target in any letter.
      3. For every vector r in the right set, check whether (target - r)
         exists in the left set (O(1) tuple hash lookup).

Complexity (N strings, alphabet size 26):
    Time  : O(2^(N/2) * 26) per test case (pruning usually cuts this down)
    Space : O(2^(N/2) * 26)
"""


# --------------------------------------------- Solution ------------------------------------------------------------


from collections import Counter

def get_counts(s):
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - ord('a')] += 1
    return tuple(cnt)

def solve_case(strings, target):
    n = len(strings)
    target_count = get_counts(target)
    mid = n // 2
    left = strings[:mid]
    right = strings[mid:]
    left_sums = set()
    left_sums.add((0,) * 26)
    for s in left:
        c = get_counts(s)
        new_sums = []
        for old in left_sums:
            new_vec = tuple(old[i] + c[i] for i in range(26))
            if all(new_vec[i] <= target_count[i] for i in range(26)):
                new_sums.append(new_vec)
        left_sums.update(new_sums)
    right_sums = {(0,) * 26}
    for s in right:
        c = get_counts(s)
        new_sums = []
        for old in right_sums:
            new_vec = tuple(old[i] + c[i] for i in range(26))
            if all(new_vec[i] <= target_count[i] for i in range(26)):
                new_sums.append(new_vec)
        right_sums.update(new_sums)
    for r in right_sums:
        need = tuple(target_count[i] - r[i] for i in range(26))
        if need in left_sums:
            return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    strings = []
    for _ in range(N):
        strings.append(input().strip())
    target = input().strip()
    if solve_case(strings, target):
        print("YES")
    else:
        print("NO")
