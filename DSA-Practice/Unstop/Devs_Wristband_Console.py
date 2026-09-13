"""
Problem   : Dev's Wristband Console
Platform  : Unstop
Link      : https://unstop.com/code/practice/659453
Difficulty: Medium
Topics    : Hashing, Heap/Priority Queue, Array, Sorting, Frequency Counting
Date      : 2026-09-13

Approach:
    Track net count (+1/-1) per wristband ID and remember the first
    position at which each ID was seen. After processing all N ops,
    filter IDs with a positive net count, then sort by
    (count desc, first_seen asc) to break ties by earliest appearance.
    Output the top K entries.

Time complexity : O(N + M log M)  -> N to process ops, M = distinct IDs
                   with positive count, log M for the sort.
Space complexity : O(M) for the count and first_seen dictionaries.
"""


# ----------------------------- Solution ------------------------------


import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    count = {}
    first_seen = {}
    for pos in range(1, N + 1):
        op, id_ = input().split()
        id_ = int(id_)
        if op == '+':
            count[id_] = count.get(id_, 0) + 1
            if id_ not in first_seen:
                first_seen[id_] = pos
        else: 
            count[id_] -= 1
    qualified = [
        (id_, count[id_], first_seen[id_])
        for id_ in count
        if count[id_] > 0
    ]
    qualified.sort(key=lambda x: (-x[1], x[2]))
    output = []
    for id_, net, _ in qualified[:K]:
        output.append(f"{id_} {net}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
