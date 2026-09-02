"""
Problem   : Equal Strings
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-strings-79789662-4dbd707c/
Date      : 2026-09-02
Difficulty: Medium
Topics    : Bitmask, Bit Manipulation, Linear Search

Approach:
    For a fixed X, count how many A[i] are "supersets" of X's bits
    (i.e. (A[i] & X) == X). Then greedily try extending X bit-by-bit
    from the highest bit down: for each bit not already set in X,
    tentatively require that bit + all higher bits already fixed,
    and recount how many A[i] satisfy the stricter mask. Track the
    best count seen across all these candidate masks.

Complexity (per test case):
    Time : O(30 * N)  -> base pass O(N) + 30 bit positions each O(N)
    Space: O(N)        -> for storing the array A
Overall across T test cases: O(T * 30 * N)
"""


# ---------------------------- Solution ---------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    answers = []
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        best = 0
        cnt = 0
        for a in A:
            if (a & X) == X:
                cnt += 1
        best = cnt
        bits_above = 0
        for k in range(29, -1, -1):
            bit = 1 << k
            if X & bit:
                bits_above |= bit
            else:
                required = bits_above | bit
                cnt = 0
                for a in A:
                    if (a & required) == required:
                        cnt += 1
                if cnt > best:
                    best = cnt
        answers.append(str(best if best > 0 else -1))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
