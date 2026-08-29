"""
Problem: Permute the Array
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/equal-sum-5b547fc2/
Date: 2026-08-29
Difficulty: Easy
Topics: Arrays, Data Structures, Hash Maps, Implementation, One-dimensional

Approach:
    For each test case, compute the required frequency (n // k) each
    element must appear if the array is to be split into k groups of
    equal sum size/count. Count frequencies with Counter, and check
    that every element's count is divisible by required_freq — if any
    isn't, an equal split isn't possible.

Time Complexity:  O(n) per test case (single pass to count + single pass to verify)
Space Complexity: O(n) per test case (Counter storage)
"""


# ----------------------------- Solution ----------------------------------


from collections import Counter
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        arr = data[idx : idx + n]
        idx += n
        required_freq = n // k
        counts = Counter(arr)
        possible = True
        for count in counts.values():
            if count % required_freq != 0:
                possible = False
                break
        if possible:
            out.append("YES")
        else:
            out.append("NO")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
