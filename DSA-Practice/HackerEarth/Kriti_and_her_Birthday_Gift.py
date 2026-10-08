"""
Problem   : Kriti and her Birthday Gift
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/kriti-and-her-birthday-gift/
Date      : 2026-10-08
Difficulty: Medium
Topics    : Binary Search, Hash Map, Sorting, Sqrt Decomposition

Approach  :
  Each query asks how many times string s appears in positions [l, r].
  1. Encode each string as an exact base-27 integer (length folded in, so
     it is collision-free) and map it to a compact id via a hash map.
  2. Build CSR-style storage: for every id, a sorted list of the positions
     where it occurs, packed into one flat array (`positions`) with
     `start[id]..start[id+1]` marking its slice.
  3. For each query, look up the id, then use two binary searches
     (bisect_left on l, bisect_right on r) within that slice; the answer
     is the difference of the indices.

Complexity:
  Time  : O(total characters + Q * (|s| + log N))
  Space : O(N)
"""


# ------------------------------------------- Solution ------------------------------------------------


import sys
from array import array
from bisect import bisect_left, bisect_right
input = sys.stdin.buffer.readline

def encode(s):
    code = len(s)
    for c in s:
        code = code * 27 + (c - 96)
    return code

N = int(input())
string_id = {}
count = array('I')
ids = array('I')
for _ in range(N):
    s = input().strip()
    code = encode(s)
    idx = string_id.get(code)
    if idx is None:
        idx = len(count)
        string_id[code] = idx
        count.append(1)
    else:
        count[idx] += 1
    ids.append(idx)

start = array('I', [0])
for c in count:
    start.append(start[-1] + c)

positions = array('I', [0]) * N
current = array('I', start[:-1])
for position in range(N):
    idx = ids[position]
    p = current[idx]
    positions[p] = position + 1
    current[idx] = p + 1

Q = int(input())
output = []
for _ in range(Q):
    parts = input().split()
    l = int(parts[0])
    r = int(parts[1])
    s = parts[2]
    code = encode(s)
    idx = string_id.get(code)
    if idx is None:
        output.append("0")
        continue
    left = start[idx]
    right = start[idx + 1]
    a = bisect_left(positions, l, left, right)
    b = bisect_right(positions, r, left, right)
    output.append(str(b - a))

sys.stdout.write("\n".join(output))
