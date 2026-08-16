"""
Problem: Fill the Boxes
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/fill-the-boxes-922504c8/
Difficulty: Medium
Topics: Sorting, Two Pointer, Implementation
Date Solved: 2026-08-16

Approach:
    Sort boxes by capacity and balls by weight. Use two pointers to greedily
    match the smallest available ball against the smallest available box:
      - If ball weight < box capacity, the ball is too light for any
        remaining box in order -> advance ball pointer.
      - If box capacity <= ball weight <= capacity + K, it's a valid fit ->
        count it, advance both pointers.
      - Otherwise (ball weight > capacity + K), this box can't be filled by
        any ball >= current one in sorted order -> advance box pointer.
    Each pointer only moves forward, so the scan is linear after sorting.

Time Complexity:  O(N log N + M log M) for sorting, O(N + M) for the two-pointer
                   scan -> overall O(N log N + M log M) per test case.
Space Complexity: O(1) extra (excluding input storage; sort is in-place).
"""


# ----------------------- Solution --------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        boxes = [int(x) for x in data[idx:idx+N]]
        idx += N
        balls = [int(x) for x in data[idx:idx+M]]
        idx += M
        boxes.sort()
        balls.sort()
        box_ptr = 0
        ball_ptr = 0
        filled_count = 0
        while box_ptr < N and ball_ptr < M:
            capacity = boxes[box_ptr]
            weight = balls[ball_ptr]
            if weight < capacity:
                ball_ptr += 1
            elif weight <= capacity + K:
                filled_count += 1
                box_ptr += 1
                ball_ptr += 1
            else:
                box_ptr += 1 
        out.append(str(filled_count))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
