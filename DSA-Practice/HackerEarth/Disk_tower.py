"""
Problem   : Disk Tower
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/disk-tower-b7cc7a50/
Difficulty: Easy
Topics    : Data Structures, Hash Maps, Priority Queue, Queue
Date      : 2026-09-29

Approach:
    Disks must be stacked in decreasing size order (largest at the bottom).
    Precompute the day each disk arrives (day[disk] = index). Keep a pointer
    `next_disk` for the largest disk not yet placed. Each day, the pointer's
    disk can only be placed once it has arrived. When it has, keep placing
    consecutive smaller disks (next_disk - 1, ...) while they have also
    already arrived. Days where the needed disk hasn't arrived print an
    empty line.

Complexity:
    Time  : O(N)  - each disk is placed exactly once, pointer only moves down
    Space : O(N)  - arrival-day array plus the output lists
"""


# --------------------------------- Solution ------------------------------------------


def Solve(arr):
    n = len(arr)
    day = [0] * (n + 1)
    for i in range(n):
        day[arr[i]] = i
    out = [[] for _ in range(n)]
    next_disk = n
    for i in range(n):
        current = arr[i]
        if current == next_disk:
            while next_disk >= 1 and day[next_disk] <= i:
                out[i].append(next_disk)
                next_disk -= 1
    return out

N = int(input())
arr = list(map(int, input().split()))
out_ = Solve(arr)
for i_out_ in out_:
    print(' '.join(map(str, i_out_)))
