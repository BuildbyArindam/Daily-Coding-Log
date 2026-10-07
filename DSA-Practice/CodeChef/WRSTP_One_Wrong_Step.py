"""
Problem   : One Wrong Step (WRSTP)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/WRSTP
Date      : 2026-10-07
Difficulty: Medium
Topics    : Implementation, Simulation

Approach  : Track the final (x, y) position and the count of each move in one pass.
            Reversing a single step changes one coordinate by exactly 2. So the
            answer is YES only if the final position is (±2, 0) or (0, ±2) and
            at least one step was taken in that direction (e.g. y == 2 needs a
            'U' that can be flipped to 'D'). Otherwise the answer is NO.

Time      : O(N) per test case
Space     : O(1) extra (four counters plus two coordinates)
"""


# ---------------------------------------------- Solution ------------------------------------------------


import sys

def _tally(seq):
    cnt = {'U':0,'D':0,'L':0,'R':0}
    px = py = 0
    for ch in seq:
        if ch == 'U':
            py += 1
            cnt['U'] += 1
        elif ch == 'D':
            py -= 1
            cnt['D'] += 1
        elif ch == 'L':
            px -= 1
            cnt['L'] += 1
        else:
            px += 1
            cnt['R'] += 1
    return px, py, cnt

def _check(px, py, cnt):
    verdict = False
    if px == 0:
        if py == 2 and cnt['U'] > 0:
            verdict = True
        elif py == -2 and cnt['D'] > 0:
            verdict = True
    if not verdict and py == 0:
        if px == 2 and cnt['R'] > 0:
            verdict = True
        elif px == -2 and cnt['L'] > 0:
            verdict = True
    return verdict

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        moves = data[idx]; idx += 1
        x_final, y_final, counter = _tally(moves)
        ans = _check(x_final, y_final, counter)
        results.append("YES" if ans else "NO")
    print("\n".join(results))

if __name__ == "__main__":
    main()
