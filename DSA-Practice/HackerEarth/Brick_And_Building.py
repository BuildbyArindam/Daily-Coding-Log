"""
Problem   : Brick and Building
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/brick-and-building-26cc28f2/
Difficulty: Easy
Topic     : Arrays, Math

Approach:
    Build a frequency array `freq` over all possible heights (1..1e5).
    For each query K, count how many bricks have a height that is a
    multiple of K by summing freq[K], freq[2K], freq[3K], ... up to
    max_val (a divisor-sieve style walk). Results are memoized in
    `ans[K]` so repeated K values in the query list are O(1) after
    the first computation.

Time Complexity : O(max_val log(max_val)) amortized overall
                   -> each distinct K is processed once via its
                      multiples (harmonic series bound), O(N + Q)
                      for I/O and lookups otherwise.
Space Complexity : O(max_val) for the freq/ans arrays.

Date Solved: 2026-08-20
"""


# ------------------------ Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    idx = 1
    max_val = 100000
    freq = [0] * (max_val + 1)
    for _ in range(N):
        height = int(input_data[idx])
        freq[height] += 1
        idx += 1
    Q = int(input_data[idx])
    idx += 1
    ans = [-1] * (max_val + 1)
    out = []
    for _ in range(Q):
        K = int(input_data[idx])
        idx += 1
        if K > max_val:
            out.append("0")
            continue
        if ans[K] != -1:
            out.append(str(ans[K]))
            continue
        count = 0
        for multiple in range(K, max_val + 1, K):
            count += freq[multiple]
        ans[K] = count
        out.append(str(count))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
