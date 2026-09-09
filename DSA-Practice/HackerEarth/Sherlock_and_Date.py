"""
Problem   : Sherlock and Date
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sherlock-and-date/
Date      : 2026-09-09
Difficulty: Easy
Topic     : Basic Programming, Implementation

Approach:
    Parse the input date string using datetime.strptime with format
    "%d %B %Y" (day, full month name, year). Subtract one day using
    timedelta(days=1) to get the previous date, then format it back
    into "day Month year" form for output.

Time Complexity : O(1) per test case (date arithmetic is constant time)
                   -> O(T) overall
Space Complexity : O(1) extra space (excluding input storage)
"""


# --------------------------- Solution --------------------------------------


from datetime import datetime, timedelta
T = int(input())
for _ in range(T):
    date_str = input().strip()
    date = datetime.strptime(date_str, "%d %B %Y")
    previous_day = date - timedelta(days=1)
    print(f"{previous_day.day} {previous_day.strftime('%B')} {previous_day.year}")
