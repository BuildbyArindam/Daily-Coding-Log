"""
Problem   : Equal Sum Partition
Platform  : CodeChef (DSAMONDAY026)
Link      : https://www.codechef.com/DSAMONDAY026/problems/ACCOLITE06
Date      : 2026-10-26
Difficulty: Hard
Topics    : Dynamic Programming, Subset Sum, Bitmask

Approach:
    The array can be split into two equal-sum parts only if the total is
    even and some subset sums to total/2. Subset-sum reachability is kept in
    a single Python big integer used as a bitset: bit i is set if sum i is
    reachable. For each value v, `reach |= reach << v` adds v to every
    reachable sum. The answer is YES if bit (total/2) is set.

Complexity (per test case, S = sum of nums, n = len(nums)):
    Time  : O(n * S / w), w = machine word size (bitset shifts are word-parallel)
    Space : O(S / w) words, i.e. O(S) bits
"""


# --------------------------------------------- Solution --------------------------------------------------------


import sys

def solve():
    tokens = sys.stdin.read().split()
    ptr = 0
    cases = int(tokens[ptr]); ptr += 1
    answers = []
    for _ in range(cases):
        size = int(tokens[ptr]); ptr += 1
        nums = [int(x) for x in tokens[ptr:ptr + size]]
        ptr += size
        total = sum(nums)
        if size < 2 or total & 1:
            answers.append("NO")
            continue
        goal = total >> 1
        reach = 1    
        for v in nums:
            reach |= reach << v
        answers.append("YES" if (reach >> goal) & 1 else "NO")
    sys.stdout.write("\n".join(answers) + "\n")

solve()
