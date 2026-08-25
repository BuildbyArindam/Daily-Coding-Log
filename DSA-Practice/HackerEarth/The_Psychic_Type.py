"""
Problem   : The Psychic Type
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-psychic-type/
Date      : 2026-08-25
Difficulty: Easy
Topics    : Ad-Hoc, Basic Programming, Implementation

Approach:
    Model the array A as a functional graph where each index i points to A[i].
    Starting from s, follow the chain of pointers. If we ever land exactly on
    e, print "Yes". If we revisit a node before reaching e, we've entered a
    cycle without hitting e, so print "No".

Time Complexity : O(n) — each node visited at most once before a repeat/cycle.
Space Complexity: O(n) — visited set + array storage.
"""


# ----------------------- Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    A = [0] + [int(x) for x in input_data[1:n+1]]
    s = int(input_data[n+1])
    e = int(input_data[n+2])
    visited = set()
    curr = s
    while curr not in visited:
        if curr == e:
            print("Yes")
            return
        visited.add(curr)
        curr = A[curr]
    print("No")

if __name__ == '__main__':
    solve()
