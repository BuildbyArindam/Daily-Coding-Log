"""
Problem   : Mobile Selection
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/mobile-selection-acc2cf2b/
Difficulty: Medium
Topics    : Binary Search, Searching, Sorting, Hiring
Date      : 2026-10-06

Approach:
    Each phone falls into one of 18 categories (3 OS x 3 RAM x 2 storage),
    so each category gets its own group. Within a group, phones are sorted
    by price and a prefix-max of rating is stored. Each query finds, via
    binary search, the last phone with price <= budget and reads its
    prefix-max rating, or prints -1 if none exists.

    Price and rating are bit-packed into one int ((price << 30) | rating)
    to save memory and speed up sorting and bisect.

Complexity:
    Time  : O(N log N + Q log N)
    Space : O(N)
"""


# ---------------------------------------- Solution -------------------------------------------------


import sys
from bisect import bisect_left
input = sys.stdin.buffer.readline
N = int(input())
s = []
a = []
b = []
c = []
d = []
for _ in range(N):
    tokens = input().split()
    s.append(tokens[0])
    a.append(int(tokens[1]))
    b.append(int(tokens[2]))
    c.append(int(tokens[3]))
    d.append(int(tokens[4]))

os_map = {
    b"windows": 0,
    b"android": 1,
    b"ios": 2
}
ram_map = {
    2: 0,
    4: 1,
    8: 2
}
mem_map = {
    32: 0,
    64: 1
}
groups = [[] for _ in range(18)]
SHIFT = 30
MASK = (1 << SHIFT) - 1
for i in range(N):
    os_id = os_map[s[i]]
    ram_id = ram_map[a[i]]
    mem_id = mem_map[b[i]]
    key = (os_id * 3 + ram_id) * 2 + mem_id
    encoded = (c[i] << SHIFT) | d[i]
    groups[key].append(encoded)
del s, a, b, c, d
for group in groups:
    group.sort()
    best = 0
    for i in range(len(group)):
        price = group[i] >> SHIFT
        rating = group[i] & MASK
        if rating > best:
            best = rating
        group[i] = (price << SHIFT) | best
Q = int(input())
output = []
for _ in range(Q):
    tokens = input().split()
    h = tokens[0]
    e = int(tokens[1])
    f = int(tokens[2])
    g = int(tokens[3])
    os_id = os_map[h]
    ram_id = ram_map[e]
    mem_id = mem_map[f]
    key = (os_id * 3 + ram_id) * 2 + mem_id
    group = groups[key]
    if not group:
        output.append("-1")
        continue
    pos = bisect_left(group, (g + 1) << SHIFT)
    if pos == 0:
        output.append("-1")
    else:
        best_rating = group[pos - 1] & MASK
        output.append(str(best_rating))
sys.stdout.write("\n".join(output))
