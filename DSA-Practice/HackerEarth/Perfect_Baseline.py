"""
Problem: Perfect Baseline
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/perfect-baseline/
Difficulty: Easy
Topics: Ad-Hoc, Approved, Implementation, Open, Ready, Sorting
Date Solved: 2026-09-05

Approach:
For each test case, and for each of the K character positions independently,
count the frequency of each of the 26 lowercase letters across all N names
at that position. Then walk through letters 'a' to 'z' accumulating a running
(cumulative) count, and pick the first letter c such that the cumulative
frequency exceeds floor((N-1)/2) — i.e., the "lower-median" letter at that
position. Concatenating the chosen letter for each of the K positions gives
the answer string for that test case.

Time Complexity: O(T * K * (N + 26)) — for each of K positions we scan all
N names once (O(N)) and then scan the 26-letter cumulative count (O(26)).
Space Complexity: O(N) per test case for storing names, plus O(26) for the
count array (dropped/reset each position).
"""


# ---------------------- Solution ---------------------------------


name = input() 
T = int(name)
answers = []
for _ in range(T):
    N, K = map(int, input().split())
    names = [input().strip() for _ in range(N)]
    result = []
    target = (N - 1) // 2
    for j in range(K):
        count = [0] * 26
        for s in names:
            count[ord(s[j]) - ord('a')] += 1
        cumulative = 0
        for c in range(26):
            cumulative += count[c]
            if cumulative > target:
                result.append(chr(ord('a') + c))
                break
    answers.append(''.join(result))
print('\n'.join(answers))
