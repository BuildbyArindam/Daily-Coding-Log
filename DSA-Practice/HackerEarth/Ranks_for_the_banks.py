"""
Problem   : Ranks for the banks!
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/problem/algorithm/ranks-for-the-banks-dd9692ee/
Date      : 2026-10-13
Difficulty: Medium
Topics    : Sorting, Stable Sort

Approach  :
  - Pack each candidate's (total, d, g, o) into one integer key in base 101,
    so a single integer comparison gives the overall ordering.
  - Sort by roll id first, then stable-sort by key descending. Ties on the
    overall score therefore resolve by roll id ascending.
  - Derive the three section rankings (d, g, o) by stable-sorting a copy of the
    overall order on that section's marks. Ties fall back to overall rank.
  - Each query is then an O(1) lookup into the matching rank list.
  - Input is read in 64 KB chunks through a token generator, with compact
    array('B')/array('I') storage to keep memory low on large inputs.

Time      : O(n log n) per test case for sorting + O(q) for queries
Space     : O(n) per test case
"""


# --------------------------------------------- Solution ----------------------------------------------------------


import sys
from array import array

def token_stream():
    read = sys.stdin.buffer.read
    carry = b''
    while True:
        chunk = read(1 << 16)
        if not chunk:
            if carry:
                yield carry
            break
        data = carry + chunk
        parts = data.split()
        if data[-1:].isspace():
            carry = b''
        else:
            carry = parts.pop()
        yield from parts
it = iter(token_stream())
try:
    T = int(next(it))
except StopIteration:
    sys.exit()
BASE = 101
for _ in range(T):
    n = int(next(it))
    roll_ids = []
    ds = array('B')
    gt = array('B')
    os = array('B')
    scores = array('I')
    for i in range(n):
        roll_id = next(it)
        d = int(next(it))
        g = int(next(it))
        o = int(next(it))
        roll_ids.append(roll_id)
        ds.append(d)
        gt.append(g)
        os.append(o)
        total = d + g + o
        score_key = (
            total * BASE**3
            + d * BASE**2
            + g * BASE
            + o
        )
        scores.append(score_key)
    grand = list(range(n))
    grand.sort(key=roll_ids.__getitem__)
    grand.sort(key=scores.__getitem__, reverse=True)
    ds_rank = grand.copy()
    ds_rank.sort(key=ds.__getitem__, reverse=True)
    gt_rank = grand.copy()
    gt_rank.sort(key=gt.__getitem__, reverse=True)
    os_rank = grand.copy()
    os_rank.sort(key=os.__getitem__, reverse=True)
    q = int(next(it))
    answers = []
    for _ in range(q):
        a = int(next(it))
        b = int(next(it)) - 1
        if a == 1:
            idx = grand[b]
        elif a == 2:
            idx = ds_rank[b]
        elif a == 3:
            idx = gt_rank[b]
        else:
            idx = os_rank[b]
        answers.append(roll_ids[idx])
    sys.stdout.buffer.write(b'\n'.join(answers) + b'\n')
    del roll_ids, ds, gt, os, scores
    del grand, ds_rank, gt_rank, os_rank, answers
