"""
Problem   : Chef and String (WENOTI)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/WENOTI
Difficulty: 1712
Topics    : Strings, Greedy/Constructive Algorithms, Pattern Recognition (periodicity/repetition)

Approach:
    T = S repeated K times (length N*K). Build B = S with all 'I' characters
    stripped out. 'I' acts as a wildcard that can be matched to either
    neighbor, so any adjacent pair touching an 'I' can always be made equal.
    The only pairs that are forced unequal are adjacent pairs of two
    surviving (non-'I') characters that differ -- computed once within one
    copy of B ('inside') and once across the K-1 seams where copies of B
    join back-to-back ('boundary'). Scale by K and (K-1) respectively to
    get the total forced-unequal count over the full repeated string, then
    subtract from (N*K - 1) total adjacent pairs to get the answer.

Time complexity : O(N) per test case (building B and scanning it once)
Space complexity: O(N) per test case (storing B)
"""


# ---------------------------------- Solution ---------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        S = input().strip()
        B = S.replace('I', '')
        total_length = N * K
        if not B:
            print(total_length - 1)
            continue
        inside = 0
        for i in range(1, len(B)):
            if B[i] != B[i - 1]:
                inside += 1
        boundary = 1 if B[0] != B[-1] else 0
        unequal = K * inside + (K - 1) * boundary
        answer = total_length - 1 - unequal
        print(answer)

if __name__ == "__main__":
    solve()
