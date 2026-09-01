"""
Problem   : Collisions
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/34/E
Difficulty: *2000
Topics    : brute force, implementation, math
Date      : 2026-09-01

Approach:
    Simulate elastic collisions between balls on a line up to time T.
    Balls are sorted by position; at each step, find the earliest
    upcoming collision among adjacent ball pairs (only pairs approaching
    each other, i.e. left ball's velocity > right ball's velocity,
    are candidates). Advance all balls to that collision time, resolve
    the 1D elastic collision (exchange velocities via mass-weighted
    formula), and repeat until no more collisions occur before T or T
    is reached. Finally, advance all balls linearly for the remaining
    time and report positions in original input order.

Complexity:
    Time : O(n^2) worst case — each of up to n-1 collisions requires an
           O(n) scan to find the next earliest adjacent collision.
    Space: O(n) for ball state.
"""


# -------------------------------- Solution ----------------------------------


import sys
EPS = 1e-10
def collide(b1, b2):
    """
    Elastic collision of two balls.
    b = [position, velocity, mass, original_index]
    """
    _, v1, m1, _ = b1
    _, v2, m2, _ = b2
    new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    b1[1] = new_v1
    b2[1] = new_v2

def solve():
    input = sys.stdin.readline
    n, T = map(int, input().split())
    balls = []
    for i in range(n):
        x, v, m = map(int, input().split())
        balls.append([float(x), float(v), float(m), i])
    balls.sort(key=lambda b: b[0])
    current_time = 0.0
    while current_time < T - EPS:
        earliest = float('inf')
        pair = -1
        for i in range(n - 1):
            x1, v1, _, _ = balls[i]
            x2, v2, _, _ = balls[i + 1]
            if v1 > v2 + EPS:
                dt = (x2 - x1) / (v1 - v2)
                if dt >= -EPS and dt < earliest:
                    dt = max(dt, 0.0)
                    earliest = dt
                    pair = i
        if pair == -1:
            break
        if current_time + earliest > T + EPS:
            break
        dt = earliest
        for b in balls:
            b[0] += b[1] * dt
        current_time += dt
        collide(balls[pair], balls[pair + 1])
    remaining = T - current_time
    for b in balls:
        b[0] += b[1] * remaining
    answer = [0.0] * n
    for b in balls:
        answer[b[3]] = b[0]
    print(*[f"{x:.10f}" for x in answer])

if __name__ == "__main__":
    solve()
