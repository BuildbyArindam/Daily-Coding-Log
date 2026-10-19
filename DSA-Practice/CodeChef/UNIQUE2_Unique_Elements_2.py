"""
Platform   : CodeChef
Problem    : Unique Elements 2 (UNIQUE2)
Link       : https://www.codechef.com/problems/UNIQUE2
Date       : 2026-10-19
Difficulty : Easy
Topics     : Arrays, Hashing

Approach:
    Read the whole input at once and walk the array left to right, keeping a
    presence array (bytearray) indexed by value. The first time a value is
    seen, mark it and append it to the output; later occurrences are skipped.
    This keeps only the first occurrence of each element, in original order.

Complexity:
    Time  : O(N), one pass with O(1) lookups
    Space : O(N + V), V = max value (~1e5) for the flag array, plus the output
"""


# ---------------------------------------------- Solution -----------------------------------------------------


import sys

def solve():
    tokens = sys.stdin.buffer.read().split()
    total = int(tokens[0])
    flag = bytearray(100002)
    answer = []
    idx = 1
    limit = total + 1
    while idx < limit:
        val = int(tokens[idx])
        idx += 1
        if flag[val] == 0:
            flag[val] = 1
            answer.append(str(val))
    sys.stdout.write(" ".join(answer) + "\n")

if __name__ == "__main__":
    solve()
