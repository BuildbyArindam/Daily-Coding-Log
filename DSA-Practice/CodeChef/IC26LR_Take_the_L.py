"""
Problem   : Take the L (IC26LR)
Platform  : CodeChef (ICPC Onsite Mirror 2026 - Post Contest)
Link      : https://www.codechef.com/ICPCOL26POST/problems/IC26LR
Date      : 2026-10-06
Difficulty: ~2000-2200 (Hard)
Topics    : Sorting, Permutations, Greedy, Prefix/Suffix Arrays

Approach  :
  1. Sort the points by x, then coordinate-compress the y values so the
     input becomes a permutation p of 1..n.
  2. Use prefix-max and suffix-min arrays to reject permutations that
     contain a forbidden pattern (a larger earlier element with a smaller
     later element that straddles the current prefix max).
  3. Split p into independent blocks wherever prefix max == index. More
     than one non-trivial block means NO; zero means YES.
  4. For the single non-trivial block, try both assignments of the two
     types (prefix-max elements vs. the rest) and greedily verify that
     the "min of type A" never conflicts with a later element.
     If either assignment holds, the answer is YES.

Complexity:
  Time  : O(n log n) per test case (sorting and ranking dominate;
          every other pass is linear)
  Space : O(n)
"""


# --------------------------------------------- Solution -----------------------------------------------------------


import sys

def _solve_one(pts):
    pts.sort()
    seq = [b for _, b in pts]
    n = len(seq)
    order = sorted(seq)
    rk = {v: i + 1 for i, v in enumerate(order)}
    p = [rk[v] for v in seq]
    suf = [n + 1] * (n + 1)
    for j in range(n - 1, -1, -1):
        suf[j] = p[j] if p[j] < suf[j + 1] else suf[j + 1]
    pre = 0
    for j in range(n):
        if pre > p[j] and suf[j + 1] < p[j]:
            return False
        if p[j] > pre:
            pre = p[j]
    big = []
    mx = 0
    s = 0
    for j in range(n):
        if p[j] > mx:
            mx = p[j]
        if mx == j + 1:
            if j > s:
                big.append((s, j))
            s = j + 1
    if not big:
        return True
    if len(big) > 1:
        return False
    l, r = big[0]
    for flip in (1, 0):
        best = n + 5
        cur = 0
        good = True
        for j in range(l, r + 1):
            is_max = p[j] > cur
            if is_max:
                cur = p[j]
            a_type = is_max if flip == 0 else (not is_max)
            if a_type:
                if p[j] < best:
                    best = p[j]
            elif best < p[j]:
                good = False
                break
        if good:
            return True
    return False

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ptr = 1
    res = []
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        pts = []
        for i in range(n):
            pts.append((int(data[ptr]), int(data[ptr + 1])))
            ptr += 2
        res.append("YES" if _solve_one(pts) else "NO")
    sys.stdout.write("\n".join(res) + "\n")

main()
