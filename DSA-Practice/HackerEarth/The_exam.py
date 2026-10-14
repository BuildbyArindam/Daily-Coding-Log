"""
Problem   : The Exam
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/the-exam/
Difficulty: Easy
Topics    : Searching
Date      : 2026-10-14

Approach:
    Read all test cases at once. For each (X, L, N), handle the trivial cases
    (X == 0 or N == 0 -> 0, L == 0 -> X). Otherwise cap the usable range
    M = min(L, X * 2^(N-1)), then use bit-length arithmetic on Z = M - 1
    (quotient/remainder by 2^N) to compute the best achievable reduction
    directly, instead of searching for it. The answer is min(X, X + N - 2 - best).

Complexity:
    Time  : O(T) overall, O(1) per test case (a few shifts and bit_length calls)
    Space : O(T) for the stored input and answers
"""


# ------------------------------------------------- Solution --------------------------------------------------------------


import sys

name = input()  
data = list(map(int, (name + " " + sys.stdin.read()).split()))
T = data[0]
pos = 1
answers = []
for _ in range(T):
    X = data[pos]
    L = data[pos + 1]
    N = data[pos + 2]
    pos += 3
    if N == 0 or X == 0:
        answers.append(0)
        continue
    if L == 0:
        answers.append(X)
        continue
    if N - 1 >= 60:
        M = L
    else:
        M = min(L, X << (N - 1))
    Z = M - 1
    if N >= Z.bit_length():
        Q = 0
        R = Z
    else:
        Q = Z >> N
        R = Z - (Q << N)
    H = (R + 1).bit_length() - 1
    if Q > 0:
        best = 2 * Q + max(H, N - 2)
    else:
        best = H
    cost = X + N - 2 - best
    answers.append(min(X, cost))
print("\n".join(map(str, answers)))
