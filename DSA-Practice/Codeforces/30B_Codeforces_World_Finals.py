"""
Problem: Codeforces World Finals
Link:    https://codeforces.com/problemset/problem/30/B
Date:    2026-08-30
Difficulty: *1700
Topic:   Implementation

Approach:
    Bob's passport shows three numbers (day, month, year) in unknown order.
    Try all 6 permutations of these numbers as (day, month, year); for each,
    check if it forms a valid calendar date (using divisibility-by-4 for leap
    years, per problem statement). For every valid interpretation, compute
    Bob's age as of the Finals date by comparing (final_month, final_day) to
    (birth_month, birth_day) rather than constructing a literal "N years
    earlier" date (which breaks on edge cases like 29 Feb). If any valid
    interpretation gives age >= 18, answer YES; otherwise NO.

Complexity:
    Time:  O(1) — at most 6 permutations, each checked in O(1)
    Space: O(1)
"""


# --------------------------------- Solution ----------------------------------------


from itertools import permutations

def is_leap(year):
    return year % 4 == 0

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

def valid_date(day, month, year):
    if month < 1 or month > 12:
        return False
    return 1 <= day <= days_in_month(month, year)

def solve():
    d, m, y = map(int, input().split('.'))
    final_day = d
    final_month = m
    final_year = 2000 + y
    birth = list(map(int, input().split('.')))
    for day, month, yy in permutations(birth):
        birth_year = 2000 + yy
        if not valid_date(day, month, birth_year):
            continue
        age = final_year - birth_year
        if (final_month, final_day) < (month, day):
            age -= 1
        if age >= 18:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()
