"""
Problem   : What Has Dirichlet Got to Do with That? (Codeforces 39E)
Link      : https://codeforces.com/problemset/problem/39/E
Date      : 2026-09-06
Difficulty: *2000
Topics    : DP, Games

Approach:
    Two players alternately multiply the current number 'a' by an integer
    in [2, b], and lose if the running product exceeds n-1 (i.e. the
    resulting box would hold >= n items on the losing move's condition).
    Precompute, for each exponent level e (number of remaining "safe"
    multiplication rounds w.r.t. root bounds), the max value A = floor(
    (n-1)^(1/e)) via integer k-th root search, then fill a Win/Lose table
    per row via backward induction: state x at level e is a Win if some
    successor state is a Lose. Row e=1 is handled with a closed-form
    parity argument once x exceeds the level-2 root threshold (pure
    Nim-like win/lose alternation), avoiding an O(n) table for the largest
    row. The special case a < 2 (a == 1) is resolved by simulating what
    happens as b decreases from max_b down to the given b, tracking
    Win/Lose/Draw transitions explicitly (a Draw ('D') indicates the game
    from a=1 never terminates within representable exponent levels).

Complexity:
    Let L = n - 1 and E = log2(L) (max useful exponent level).
    Time : O(E * sqrt(L) * log(L)) -- kth_root_leq does O(log(L)) binary
           search steps per exponent per row, and row e has O(root[e])
           entries; dominated by the e=2 row of size O(sqrt(L)).
    Space: O(sqrt(L)) -- only rows down to e=2 are materialized as dicts;
           row 1 is computed on demand via row1_value().
"""


# -------------------------- Solution --------------------------------------


import sys

def kth_root_leq(x, k):
    """Largest integer r such that r^k <= x."""
    if k == 1:
        return x
    lo, hi = 1, min(x, 31623)
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid ** k <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

def solve(a, b, n):
    limit = n - 1
    max_b = 0
    p = 1
    while p * 2 <= limit:
        p *= 2
        max_b += 1
    root = [0] * (max_b + 3)
    root[1] = limit
    for e in range(2, max_b + 3):
        root[e] = kth_root_leq(limit, e)
    rows = {}
    for e in range(max_b, 1, -1):
        A = root[e]
        arr = [None] * (A + 2)
        upper = rows.get(e + 1)
        for x in range(A, 1, -1):
            win = False
            if x < A and arr[x + 1] == 'L':
                win = True
            if not win and upper is not None:
                if x <= root[e + 1] and upper.get(x) == 'L':
                    win = True
            arr[x] = 'W' if win else 'L'
        rows[e] = {x: arr[x] for x in range(2, A + 1)}
    def row1_value(x):
        A2 = root[2] if max_b >= 2 else 1
        if x > A2:
            return 'L' if (limit - x) % 2 == 0 else 'W'
        cur = 'L' if (limit - (A2 + 1)) % 2 == 0 else 'W'
        for v in range(A2, x - 1, -1):
            win = (cur == 'L') or (rows[2][v] == 'L')
            cur = 'W' if win else 'L'
        return cur
    if a >= 2:
        if b == 1:
            result = row1_value(a)
        else:
            result = rows[b][a]
    else:
        if b > max_b + 1:
            result = 'D'
        else:
            cur = 'D'
            for e in range(max_b, b - 1, -1):
                if e == 1:
                    box_move = row1_value(2)
                else:
                    box_move = rows[e][2]
                if box_move == 'L' or cur == 'L':
                    cur = 'W'
                elif cur == 'D':
                    cur = 'D'
                else:
                    cur = 'L'
            result = cur
    if result == 'W':
        return "Masha" 
    elif result == 'L':
        return "Stas"   
    else:
        return "Missing"  

def main():
    a, b, n = map(int, sys.stdin.readline().split())
    print(solve(a, b, n))

if __name__ == "__main__":
    main()
