"""
Problem: The Perfect Road (Bob & Alice and the Perfect Road - 1)
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bobalice-and-the-perfect-road-1-3f60abdf/
Date Solved: 2026-08-20
Difficulty: Easy
Topic: Ad-Hoc, Basic Programming / Implementation

Approach:
    Single left-to-right scan tracking the running maximum speed, its index,
    and a tie counter. Reset the tie counter whenever a strictly greater
    speed is found; increment it on ties with the current max. If more than
    one road shares the max speed, output "Many Roads"; otherwise output the
    1-indexed position of the unique fastest road.

Time Complexity:  O(N) per test case, O(sum of N) overall
Space Complexity: O(N) to store speeds (O(1) extra beyond input storage)
"""


# -------------------------- Solutiom ---------------------------------


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
        S = int(data[idx])
        X = int(data[idx + 1])
        N = int(data[idx + 2])
        idx += 3
        speeds = [int(x) for x in data[idx : idx + N]]
        idx += N
        max_speed = -1
        max_index = -1
        count = 0
        for i, speed in enumerate(speeds, start=1):
            if speed > max_speed:
                max_speed = speed
                max_index = i
                count = 1
            elif speed == max_speed:
                count += 1
        if count > 1:
            out.append("Many Roads")
        else:
            out.append(str(max_index))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
