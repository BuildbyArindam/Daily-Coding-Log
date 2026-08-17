"""
Problem   : Bob and K - Subset
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bob-and-subset-23f0729c/
Date      : 2026-08-17
Difficulty: Medium
Topics    : Basic Programming, Hash Maps, Implementation, Bitwise OR, Closure/BFS

Approach:
Build the set of all values reachable by OR-ing together 1 to K elements
from the array (using a distinct-element version of the array to avoid
redundant work). Start with reach = {0} and repeatedly OR every element
in `arr` with every value currently in `reach`, growing the set over K
rounds. Stop early if the set stops growing (fixed point reached — no
need to run all K rounds since OR-closure saturates quickly). Discard 0
at the end (empty subset) and the answer is the count of distinct
OR-values achievable using at most K elements.

Time complexity : O(K * |reach| * n)  worst case (bounded by early-exit
                   on saturation, since |reach| <= 2^(bits in max value))
Space complexity : O(|reach|)  for the current/next reachable-value sets
"""


# ----------------------- Solution -------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    arr = list(set(map(int, input_data[2:n+2]))) 
    reach = {0}
    for _ in range(k):
        next_reach = set(reach)
        for prev in reach:
            for num in arr:
                next_reach.add(prev | num)
        if len(next_reach) == len(reach):
            break
        reach = next_reach
    reach.discard(0)
    print(len(reach))

if __name__ == '__main__':
    solve()
