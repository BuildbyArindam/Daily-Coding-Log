"""
Problem: Holidays
Link: https://codeforces.com/problemset/problem/44/C
Difficulty: *1300
Topic: Implementation
Date Solved: 2026-09-11

Approach:
Track how many business trips cover each day using a difference/counting
array. For each trip [a, b], increment days[day] for every day in range.
Then scan days 1..n; the first day with count != 1 is either uncovered
(0) or double-booked (>1), and gets printed with its count. If every day
has exactly one trip, print "OK".

Time Complexity: O(n*m) worst case — each of m trips can span up to n days.
Space Complexity: O(n) for the days array.
"""


# --------------------------- Solution ------------------------------------


n, m = map(int, input().split())
days = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    for day in range(a, b + 1):
        days[day] += 1
for day in range(1, n + 1):
    if days[day] != 1:
        print(day, days[day])
        break
else:
    print("OK")
