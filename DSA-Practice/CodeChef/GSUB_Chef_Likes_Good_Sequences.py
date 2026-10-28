"""
Problem   : Chef Likes Good Sequences (GSUB)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GSUB
Difficulty: 2017
Topics    : Case work, Online Queries, Algorithms
Date      : 2026-10-28

Approach:
    The answer after each query equals the number of maximal blocks of equal
    adjacent elements, i.e. 1 + (count of indices i where arr[i] != arr[i+1]).
    Compute this once in O(N). A point update at pos only affects the two
    boundaries (pos-1, pos) and (pos, pos+1), so subtract their contribution
    before the update, apply it, then add it back. Each query is O(1).

Complexity:
    Time : O(N + Q) per test case
    Space: O(N) for the array (plus O(Q) for buffered output)
"""


# ----------------------------------------- Solution ---------------------------------------------------------


import sys

def main():
    rd = sys.stdin.buffer.read().split()
    ptr = 0
    tc = int(rd[ptr]); ptr += 1
    res = []
    while tc:
        tc -= 1
        n = int(rd[ptr]); q = int(rd[ptr + 1]); ptr += 2
        arr = rd[ptr:ptr + n]
        ptr += n
        arr = list(map(int, arr))

        def edge(i):
            if i < 0 or i + 1 >= n:
                return 0
            return 1 if arr[i] != arr[i + 1] else 0
        total = 1
        for i in range(n - 1):
            total += edge(i)
        for _ in range(q):
            pos = int(rd[ptr]) - 1
            val = int(rd[ptr + 1])
            ptr += 2
            total -= edge(pos - 1) + edge(pos)
            arr[pos] = val
            total += edge(pos - 1) + edge(pos)
            res.append(total)
    sys.stdout.write("\n".join(map(str, res)) + "\n")

main()
