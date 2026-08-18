"""
Problem   : Server Queue (SQUEU)
Link      : https://www.codechef.com/problems/SQUEU
Date      : 2026-08-18
Topics    : Binary Search (on answer), Greedy, Simulation
Difficulty: Medium (assessed from approach; not scraped from CodeChef tags)

Approach:
  Binary search on the minimum number of leading requests to discard
  (`begin_at`) such that the remaining suffix of requests can be served
  by `machines` servers, each with `tank` capacity, filled greedily
  left to right. `can_finish` is monotonic in `begin_at` (dropping more
  of the prefix never makes feasibility worse), which justifies the
  binary search.

Time complexity : O(n log n)
                   - O(log n) binary search iterations
                   - O(n) per feasibility check (each request is visited
                     once; the inner while loop only advances `active_unit`,
                     which is bounded by `machines` across the whole scan)
Space complexity : O(n) for storing the requests array
"""


# --------------------- Solution ---------------------------


import sys

def can_finish(reqs, begin_at, tank, machines):
    active_unit = 0
    left_capacity = tank
    idx = begin_at
    total = len(reqs)
    while idx < total:
        need = reqs[idx]
        while left_capacity < need:
            active_unit += 1
            if active_unit == machines:
                return False
            left_capacity = tank
        left_capacity -= need
        idx += 1
    return True

def minimum_prefix_removal(reqs, machines, tank):
    n = len(reqs)
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(reqs, mid, tank, machines):
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    data = sys.stdin.read().split()
    pos = 0
    n_requests = int(data[pos]); pos += 1
    n_servers = int(data[pos]); pos += 1
    capacity = int(data[pos]); pos += 1
    requirements = [int(data[pos + i]) for i in range(n_requests)]
    result = minimum_prefix_removal(requirements, n_servers, capacity)
    print(result)

if __name__ == "__main__":
    main()
