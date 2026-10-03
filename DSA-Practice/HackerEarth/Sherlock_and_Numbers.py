"""
Problem   : Sherlock and Numbers
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/sherlock-and-numbers/
Date      : 2026-10-03
Difficulty: Easy
Topics    : Binary Search, Sorting

Approach  : Sort the removed numbers. Each gap between consecutive removed
            values (starting from 0) holds a known count of remaining numbers.
            Walk the gaps, subtracting each gap size from P until P fits
            inside one; the answer is prev + P. If P > N - K, print -1.

Time      : O(K log K) per test case (dominated by sorting)
Space     : O(K) per test case (plus fast input buffer)
"""


# ----------------------------------------- Solution -------------------------------------------------


import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    T = next(it)
    answers = []
    for _ in range(T):
        N = next(it)
        K = next(it)
        P = next(it)
        removed = [next(it) for _ in range(K)]
        if P > N - K:
            answers.append("-1")
            continue
        if K == 0:
            answers.append(str(P))
            continue
        removed.sort()
        prev = 0
        for x in removed:
            gap = x - prev - 1
            if P <= gap:
                answers.append(str(prev + P))
                break
            P -= gap
            prev = x
        else:
            answers.append(str(prev + P))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
