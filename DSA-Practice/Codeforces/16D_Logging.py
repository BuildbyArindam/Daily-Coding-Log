"""
Problem: Logging
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/16/D
Difficulty: *1900
Topics: implementation, strings
Date Solved: 2026-08-23

Approach:
Parse each 12-hour timestamp into minutes-since-midnight (0-1439).
Walk through log entries tracking the previous entry's time and how many
consecutive entries share that exact time. A new "day" (server reboot)
starts whenever the current time is strictly less than the previous time,
or when 10 consecutive entries share the same time (server can't log more
than 10 identical timestamps per day per problem constraints).

Time Complexity: O(N) - single pass over N log lines
Space Complexity: O(N) - storing all input lines (O(1) extra beyond input)
"""


# ------------------------- Solution -----------------------------


import sys

def parse_time(line):
    time_str = line[1:10]
    hh = int(time_str[0:2])
    mm = int(time_str[3:5])
    period = time_str[6]  
    if period == 'a':
        if hh == 12:
            hh = 0
    else:  # 'p'
        if hh != 12:
            hh += 12
    return hh * 60 + mm
def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0])
    lines = input_data[1:n+1]
    days = 1
    prev_time = -1
    same_time_count = 0
    for line in lines:
        curr_time = parse_time(line)
        if curr_time < prev_time:
            days += 1
            same_time_count = 1
        elif curr_time == prev_time:
            if same_time_count == 10:
                days += 1
                same_time_count = 1
            else:
                same_time_count += 1
        else:
            same_time_count = 1
        prev_time = curr_time
    print(days)

if __name__ == "__main__":
    main()
