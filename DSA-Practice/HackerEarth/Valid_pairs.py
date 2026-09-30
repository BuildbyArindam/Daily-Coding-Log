"""
Problem : Valid Pairs
Platform: HackerEarth
Link    : https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/valid-pairs-4f78e507/
Date    : 2026-09-30
Difficulty: Easy
Topics  : Data Structures, Hash Tables

Approach:
    Count pairs (i < j) whose sum is a power of 3. Precompute every power
    of 3 up to the maximum possible pair sum (2 * 3^20). While scanning the
    array, for each element x and each power p, look up the complement
    (p - x) in a hash map of previously seen values and add its count.
    Then record x in the map. One pass, so each pair is counted once.

Complexity:
    Time : O(N * K), where K = number of powers (~20), so effectively O(N)
    Space: O(N) for the frequency map
"""


# ------------------------------------ Solution ---------------------------------------


def solve(N, wealth):
    powers = []
    p = 3
    max_sum = 2 * (3 ** 20)
    while p <= max_sum:
        powers.append(p)
        p *= 3
    seen = {}
    ans = 0
    for x in wealth:
        for p in powers:
            complement = p - x
            if complement in seen:
                ans += seen[complement]
        seen[x] = seen.get(x, 0) + 1
    return ans

N = int(input())
wealth = list(map(int, input().split()))
out_ = solve(N, wealth)
print(out_)
