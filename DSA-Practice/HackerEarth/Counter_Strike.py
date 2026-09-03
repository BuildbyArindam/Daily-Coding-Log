"""
Problem   : Counter Strike
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/counter-strike-12/
Difficulty: Easy
Topics    : Senior, Array, Math

Date      : 2026-09-04

Approach:
    For each test case, read N shooter locations and M target locations.
    For every shooter, scan all not-yet-reached targets and mark a target
    as "reached" if the Manhattan distance to the shooter is <= D.
    After processing all shooters, count how many targets were reached;
    output "YES" if more than half the targets (M // 2) were hit,
    else "NO".

Complexity:
    Time : O(N * M) per test case
    Space: O(N + M) for storing locations and the reached array
"""


# ----------------------------- Solution -------------------------------


T = int(input())
for _ in range(T):
    N, M, D = map(int, input().split())
    locations = []
    for _ in range(N):
        x, y = map(int, input().split())
        locations.append((x, y))
    targets = []
    for _ in range(M):
        x, y = map(int, input().split())
        targets.append((x, y))
    reached = [False] * M
    for i in range(N):
        lx, ly = locations[i]
        for j in range(M):
            if not reached[j]:
                tx, ty = targets[j]
                distance = abs(lx - tx) + abs(ly - ty)
                if distance <= D:
                    reached[j] = True
    count = sum(reached)
    if count > M // 2:
        print("YES")
    else:
        print("NO")
