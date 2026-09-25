"""
Problem: Fredo and Large Numbers
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/fredo-and-large-numbers/
Difficulty: Medium
Topics: Ad-Hoc, Data Structures, One-dimensional, Data Compression
Date Solved: 2026-09-25

Approach:
Count each element's frequency and record the order in which distinct
values first appear. For every frequency value f, store the earliest
(by first-appearance order) element whose frequency is exactly f
(earliest_by_freq). Then sweep f from n down to 1, keeping a running
"best" (smallest first-appearance slot) so far, to build atleast_value[f]
- the earliest-appearing element whose frequency is >= f.
  - Query type 1 (exact frequency f): answer = earliest_by_freq[f]
  - Query type 2 (at least frequency f): answer = atleast_value[f]
Both answered in O(1) after O(n) preprocessing.

Time Complexity: O(n + q)
Space Complexity: O(n)
"""


# ---------------------------------------- Solution ----------------------------------------------


import sys

def resolve_queries():
    data = sys.stdin.buffer.read().split()
    ptr = 0
    n = int(data[ptr]); ptr += 1
    arr = data[ptr:ptr + n]
    ptr += n
    occurrence_count = {}
    appearance_order = []
    for token in arr:
        if token in occurrence_count:
            occurrence_count[token] += 1
        else:
            occurrence_count[token] = 1
            appearance_order.append(token)
    distinct_total = len(appearance_order)
    earliest_by_freq = [None] * (n + 2)
    earliest_slot = [None] * (n + 2)
    for slot in range(distinct_total):
        val = appearance_order[slot]
        f = occurrence_count[val]
        if earliest_by_freq[f] is None:
            earliest_by_freq[f] = val
            earliest_slot[f] = slot
    atleast_value = [None] * (n + 2)
    running_best_slot = None
    running_best_val = None
    for f in range(n, 0, -1):
        slot_here = earliest_slot[f]
        if slot_here is not None and (running_best_slot is None or slot_here < running_best_slot):
            running_best_slot = slot_here
            running_best_val = earliest_by_freq[f]
        atleast_value[f] = running_best_val
    q = int(data[ptr]); ptr += 1
    out_lines = []
    for _ in range(q):
        qtype = data[ptr]; freq_target = data[ptr + 1]; ptr += 2
        f_val = int(freq_target)
        if f_val > n:
            out_lines.append(b"0")
            continue
        if qtype == b"1":
            ans = earliest_by_freq[f_val]
        else:
            ans = atleast_value[f_val]
        out_lines.append(ans if ans is not None else b"0")
    sys.stdout.buffer.write(b"\n".join(out_lines) + b"\n")

if __name__ == "__main__":
    resolve_queries()
