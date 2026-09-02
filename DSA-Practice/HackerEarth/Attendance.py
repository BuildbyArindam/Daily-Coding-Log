"""
Problem   : Attendance
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/attendance-72-5c241efb/
Difficulty: Medium
Topics    : Linear Search, Algorithms, Real World
Date      : 2026-09-02

Approach:
    - Convert HH:MM:SS times to seconds; clip every student's raw
      intervals to the [start, end] class window.
    - Merge each student's own overlapping intervals first (so a
      student isn't double-counted for re-entering during overlap).
    - Build a sweep-line: at each interval boundary, record a delta
      to total-students-present and a separate delta for SID 1.
    - Sweep left to right, tracking current attendance and current
      SID-1 presence in each gap between consecutive event times.
    - Track the minimum attendance value seen and accumulate total
      seconds at that minimum, plus seconds at that minimum where
      SID 1 was present.
    - Answer = (SID1 seconds at min attendance) / (total seconds at
      min attendance), reduced via GCD; print 0 if SID 1 never hits
      the minimum.

Time complexity : O(N log N) — dominated by sorting each student's
                   intervals and sorting the event times.
Space complexity: O(N) — one interval list and one event dict keyed
                   by boundary time.
"""


# ------------------------ Solution ---------------------------------


name = input()                 
N = int(name)
StartTime, EndTime = input().split()

def to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

start = to_seconds(StartTime)
end = to_seconds(EndTime)
student_intervals = {}
for _ in range(N):
    parts = input().split()
    sid = int(parts[0])
    m = int(parts[1])
    if sid not in student_intervals:
        student_intervals[sid] = []
    for i in range(m):
        l = to_seconds(parts[2 + 2 * i])
        r = to_seconds(parts[3 + 2 * i]).
        l = max(l, start)
        r = min(r, end)
        if l < r:
            student_intervals[sid].append((l, r))
events = {}
sid1_exists = False
for sid, intervals in student_intervals.items():
    intervals.sort()
    merged = []
    for l, r in intervals:
        if not merged or l > merged[-1][1]:
            merged.append([l, r])
        else:
            merged[-1][1] = max(merged[-1][1], r)
    if sid == 1:
        sid1_exists = True
    for l, r in merged:
        if l not in events:
            events[l] = [0, 0]
        if r not in events:
            events[r] = [0, 0]
        events[l][0] += 1
        events[r][0] -= 1
        if sid == 1:
            events[l][1] += 1
            events[r][1] -= 1
if start not in events:
    events[start] = [0, 0]
if end not in events:
    events[end] = [0, 0]
times = sorted(events.keys())
current_students = 0
sid1_present = 0
previous_time = start
minimum_students = 10**9
total_min_seconds = 0
sid1_min_seconds = 0
for t in times:
    if t > previous_time:
        duration = t - previous_time
        if current_students < minimum_students:
            minimum_students = current_students
            total_min_seconds = duration
            if sid1_present:
                sid1_min_seconds = duration
            else:
                sid1_min_seconds = 0
        elif current_students == minimum_students:
            total_min_seconds += duration
            if sid1_present:
                sid1_min_seconds += duration
    current_students += events[t][0]
    sid1_present += events[t][1]
    previous_time = t
if sid1_min_seconds == 0:
    print(0)
else:
    import math
    g = math.gcd(sid1_min_seconds, total_min_seconds)
    p = sid1_min_seconds // g
    q = total_min_seconds // g
    print(f"{p}/{q}")
