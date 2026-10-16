"""
Platform   : CodeChef
Problem    : Chef and Line (CARRAY)
Link       : https://www.codechef.com/problems/CARRAY
Difficulty : 2005
Topics     : Greedy, Sorting
Date       : 2026-10-16

Approach:
    Sort the array, then greedily build the longest valid chain. Always
    start from the smallest element, since a smaller "last" value only
    makes the threshold (last * k + b) easier to meet. Scan left to right
    and take the next element v whenever v >= last * k + b, then update
    last = v. Taking the earliest eligible element keeps the threshold as
    low as possible for what follows.

Complexity:
    Time  : O(N log N) per test case (sorting dominates; the scan is O(N))
    Space : O(N) for the sorted array
"""


# ------------------------------------------- Solution ----------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    pos = 0
    t = int(tokens[pos]); pos += 1
    out = []
    for _ in range(t):
        n = int(tokens[pos]); k = int(tokens[pos + 1]); b = int(tokens[pos + 2])
        pos += 3
        arr = sorted(map(int, tokens[pos:pos + n]))
        pos += n
        taken = 1
        last = arr[0]
        for idx in range(1, n):
            v = arr[idx]
            if v >= last * k + b:
                taken += 1
                last = v
        out.append(str(taken))
    sys.stdout.write("\n".join(out) + "\n")

main()
