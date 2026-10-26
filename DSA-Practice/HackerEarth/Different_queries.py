"""
Problem   : Different queries (HackerEarth)
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/jumbled-queries-afb23321/
Difficulty: Easy
Topics    : Algorithms, Sorting, Merge Sort
Date      : 2026-10-26

Approach:
  - Type-1 queries (range add): recorded in difference arrays. One array holds
    all adds, a second holds only the positive adds.
  - Type-2 queries: sorted by value in ascending order and painted over their
    ranges, so on overlaps the largest value is written last and wins.
  - Prefix sums turn the difference arrays into per-index totals. Indices never
    touched by a type-2 query get arr[i] + all adds; painted indices get the
    painted value + positive adds.

Complexity:
  Time : O(N + Q log Q) for reading, sorting and prefix sums, plus the
         painting step, which is O(sum of range lengths) and O(N * Q) in the
         worst case with many large overlapping ranges.
  Space: O(N + Q)
"""


# ------------------------------------------------- Solution -------------------------------------------------------


import sys

SENTINEL = -10 ** 18

def emit(vals):
    sys.stdout.write(" ".join(map(str, vals)) + "\n")

def accumulate(diff, size):
    out = []
    run = 0
    for idx in range(size):
        run += diff[idx]
        out.append(run)
    return out

def solve():
    data = sys.stdin.buffer.read().split()
    cnt = int(data[0])
    qn = int(data[1])
    arr = [int(z) for z in data[2:2 + cnt]]
    every_add = [0] * (cnt + 2)    
    good_add = [0] * (cnt + 2)  
    assigns = []   
    cur = 2 + cnt
    for _ in range(qn):
        kind = data[cur]
        lo = int(data[cur + 1]) - 1
        hi = int(data[cur + 2])
        val = int(data[cur + 3])
        cur += 4
        if kind == b'2':
            assigns.append((val, lo, hi))
        else:
            every_add[lo] += val
            every_add[hi] -= val
            if val > 0:
                good_add[lo] += val
                good_add[hi] -= val
    assigns.sort()
    top = [SENTINEL] * cnt
    for val, lo, hi in assigns:
        top[lo:hi] = [val] * (hi - lo)
    total_sum = accumulate(every_add, cnt)
    plus_sum = accumulate(good_add, cnt)
    final = [0] * cnt
    for i in range(cnt):
        if top[i] == SENTINEL:
            final[i] = arr[i] + total_sum[i]
        else:
            final[i] = top[i] + plus_sum[i]
    emit(final)

solve()
