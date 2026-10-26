"""
Problem   : Maximum Sum of Building Speed
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/maximum-sum-of-building-speed-00ab8996/
Date      : 2026-10-26
Difficulty: Easy
Topics    : Algorithms, Sorting, Merge Sort

Approach  : Pairing 2n speeds to maximize the sum of pair minimums means
            sorting and taking the elements at even indices (0, 2, 4, ...).
            Instead of a comparison sort, I use a counting sort over the
            speed range. For each speed value with count `cnt`, a flag
            `shifted` tracks whether the elements before it have odd parity,
            which decides if this group starts on an even or odd index:
              - not shifted: (cnt + 1) // 2 of them land on even indices
              - shifted:     cnt // 2 of them land on even indices
            The flag flips whenever cnt is odd.

Time      : O(n + K), where K = 10^4 is the max speed value
Space     : O(K) for the frequency buckets
"""


# ----------------------------------------------------- Solution ------------------------------------------------------


import sys

LIMIT = 10 ** 4

def best_total(n, speeds):
    bucket = [0] * (LIMIT + 1)
    for s in speeds:
        bucket[s] += 1
    answer = 0
    shifted = False 
    for speed in range(1, LIMIT + 1):
        cnt = bucket[speed]
        if cnt == 0:
            continue
        mins = cnt // 2 if shifted else (cnt + 1) // 2
        answer += mins * speed
        if cnt & 1:
            shifted = not shifted
    return answer

def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    speeds = list(map(int, tokens[1:1 + 2 * n]))
    print(best_total(n, speeds))

main()
