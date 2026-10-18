"""
Problem   : Balanced Partition
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/balanced-partition-818edecd/
Date      : 2026-10-18
Difficulty: Medium
Topics    : Algorithms, Sorting, Bubble Sort, Rotation

Approach  : Each item is reduced to a key d = y - x with weight h. Weights
            sharing the same key are merged, and keys are processed in sorted
            order while tracking a running prefix sum. The answer is YES if
            either (a) some prefix sums to exactly half the total, or
            (b) one key group sits in the middle so that the weight before it
            equals the weight after it. Otherwise it is NO.

Time      : O(n log n) per test case (dominated by sorting the distinct keys)
Space     : O(n) for the key -> total-weight map
"""


# -------------------------------------------- Solution ---------------------------------------------------------


import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        groups = {}
        total = 0
        for _ in range(n):
            x = int(data[idx]); y = int(data[idx + 1]); h = int(data[idx + 2])
            idx += 3
            d = y - x
            groups[d] = groups.get(d, 0) + h
            total += h
        ok = False
        prefix = 0 
        for d in sorted(groups):
            w = groups[d]
            if prefix == total - prefix - w:
                ok = True
                break
            prefix += w
            if prefix * 2 == total:
                ok = True
                break
        out.append("YES" if ok else "NO")
    print("\n".join(out))
main()
