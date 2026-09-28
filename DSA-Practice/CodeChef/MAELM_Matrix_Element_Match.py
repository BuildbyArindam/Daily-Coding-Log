"""
Platform   : CodeChef (DSAMONDAY022)
Problem    : Matrix Element Match (MAELM)
Link       : https://www.codechef.com/DSAMONDAY022/problems/MAELM
Date       : 2026-09-28
Difficulty : Hard
Topics     : Arrays, Sorting, Two Pointers

Approach   : Read the n x n matrix A and the m x m matrix B as flat lists.
             Sort both, then walk them with a two-pointer scan to check that
             every element of B (with multiplicity) can be matched to a
             distinct equal element of A. Print TRUE if all match, else FALSE.
             Early exit if B has more elements than A.

Complexity : Let N = n^2, M = m^2.
             Time  : O(N log N + M log M) for sorting, O(N + M) for the scan
             Space : O(N + M) for the flattened lists
"""


# ---------------------------------- Solution ---------------------------------------------------


import sys

def _load():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    m = int(raw[1])
    total_a = n * n
    total_b = m * m
    left = 2
    mid = left + total_a
    right = mid + total_b
    pool = list(map(int, raw[left:mid]))
    need = list(map(int, raw[mid:right]))
    return pool, need

def _covers(pool, need):
    if len(need) > len(pool):
        return False
    pool.sort()
    need.sort()
    cursor = 0
    limit = len(pool)
    for target in need:
        while cursor < limit and pool[cursor] < target:
            cursor += 1
        if cursor == limit or pool[cursor] != target:
            return False
        cursor += 1
    return True

def _run():
    pool, need = _load()
    verdict = _covers(pool, need)
    sys.stdout.write("TRUE" if verdict else "FALSE")
    sys.stdout.write("\n")

if __name__ == "__main__":
    _run()
