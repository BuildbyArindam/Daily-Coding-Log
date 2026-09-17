"""
Problem: Breakup App
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/breakup-app/
Date Solved: 2026-09-17
Difficulty: Easy
Topics: Ad-Hoc

Approach:
Track a "weight" score for each day of the month (1-30). Each statement
is either from a girl ("G:") or a boy ("B:"), and mentions one or more
day numbers. A girl's mention adds weight 2 to that day, a boy's
mention adds weight 1. After processing all statements, find the day(s)
with the maximum weight. If there's a unique day with max weight and
that day is the 19th or 20th, print "Date"; otherwise print "No Date".

Time Complexity:  O(N * L) where N = number of statements, L = average
                   number of tokens per line (effectively O(N) for
                   typical inputs).
Space Complexity: O(1) — fixed-size weight array of 31 elements.
"""


# -------------------------------- Solution ---------------------------------------------


N = int(input())
weight = [0] * 31  
for _ in range(N):
    line = input().split()
    if line[0] == "G:":
        w = 2
    else:
        w = 1
    for word in line[1:]:
        if word.isdigit():
            day = int(word)
            if 1 <= day <= 30:
                weight[day] += w
max_weight = max(weight)
if max_weight == 0:
    print("No Date")
else:
    days_with_max = [day for day in range(1, 31) if weight[day] == max_weight]
    if len(days_with_max) != 1:
        print("No Date")
    elif days_with_max[0] in (19, 20):
        print("Date")
    else:
        print("No Date")
