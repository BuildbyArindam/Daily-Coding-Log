"""
Problem   : Race (Codeforces 43E)
Link      : https://codeforces.com/problemset/problem/43/E
Date      : 2026-09-11
Difficulty: *2300
Topics    : Brute Force, Implementation, Two Pointers

Approach:
    For every pair of cars, walk through both cars' speed segments in
    lockstep (two-pointer merge on segment boundaries) up to the time
    the earlier car finishes. On each merged sub-interval the relative
    position (x1 - x2) is linear in time, so a lead-change either:
      (a) happens strictly inside the interval (sign of relative
          position flips from start to end), or
      (b) happens exactly at a segment boundary where the relative
          position hits zero and the sign differs immediately before
          vs. immediately after.
    Sum these lead-change counts over all pairs. Meetings at the
    finish line are excluded by stopping at end_time = min(finish1, finish2).

Complexity:
    Let K = max total number of speed segments across the two cars
    in a pair, and n = number of cars.
    Time : O(n^2 * K)   -- each pair processed in O(K) via two pointers
    Space: O(K) per pair for the intervals list (O(1) extra if you
           drop the list and track only the previous sign/segment)
"""


# -------------------------- Solution --------------------------------------


import sys

def count_leads(car1, car2):
    """
    Count the number of times the relative order of car1 and car2 changes.

    Each car is represented as:
        [(speed, duration), ...]

    We only consider the time interval until the first car reaches
    the finish, because meetings at the finish are not leads.
    """
    finish1 = sum(t for v, t in car1)
    finish2 = sum(t for v, t in car2)
    end_time = min(finish1, finish2)
    i = j = 0
    v1, rem1 = car1[0]
    v2, rem2 = car2[0]
    x1 = x2 = 0
    current_time = 0
    intervals = []
    while current_time < end_time:
        dt = min(rem1, rem2, end_time - current_time)
        d0 = x1 - x2
        x1 += v1 * dt
        x2 += v2 * dt
        d1 = x1 - x2
        intervals.append((current_time, current_time + dt, d0, d1))
        current_time += dt
        rem1 -= dt
        rem2 -= dt
        if rem1 == 0 and current_time < end_time:
            i += 1
            v1, rem1 = car1[i]
        if rem2 == 0 and current_time < end_time:
            j += 1
            v2, rem2 = car2[j]
    def sign(x):
        if x > 0:
            return 1
        if x < 0:
            return -1
        return 0
    answer = 0
    for k in range(len(intervals)):
        _, t1, d0, d1 = intervals[k]
        if d0 * d1 < 0:
            answer += 1
        if k + 1 < len(intervals) and d1 == 0:
            left_sign = sign(d0)
            right_sign = sign(intervals[k + 1][3])
            if left_sign != right_sign:
                answer += 1
    return answer

def main():
    input = sys.stdin.readline
    n, s = map(int, input().split())
    cars = []
    for _ in range(n):
        data = list(map(int, input().split()))
        k = data[0]
        car = []
        pos = 1
        for _ in range(k):
            v = data[pos]
            t = data[pos + 1]
            pos += 2
            car.append((v, t))
        cars.append(car)
    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            answer += count_leads(cars[i], cars[j])
    print(answer)

if __name__ == "__main__":
    main()
