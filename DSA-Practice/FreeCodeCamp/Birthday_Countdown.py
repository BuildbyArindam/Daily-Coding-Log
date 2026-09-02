"""
Problem: Birthday Countdown
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-17
Date Solved: 2026-09-02
Difficulty: Easy-Medium
Topics: Date/Time Manipulation, Math, Conditional Logic

Approach:
    Parse today's date and the birthday (month/day). Starting from the
    current year, try to construct the birthday date for that year,
    skipping years where the date is invalid (handles Feb 29 on
    non-leap years). If the constructed date is strictly after today,
    that's the next birthday — return the day difference. Otherwise
    advance to the next year and retry.

Time Complexity: O(1) amortized — the loop advances at most a few
    years in the worst case (bounded by leap-year cycle), so it's
    effectively constant.
Space Complexity: O(1) — only a few date objects held at once.
"""


# ------------------------ Solution ---------------------------------


from datetime import date

def days_until_birthday(today, birthday):
    year, month, day = map(int, today.split("-"))
    today_date = date(year, month, day)
    birth_month, birth_day = map(int, birthday.split("/"))
    birthday_year = year
    while True:
        try:
            next_birthday = date(birthday_year, birth_month, birth_day)
        except ValueError:
            birthday_year += 1
            continue
        if next_birthday > today_date:
            return (next_birthday - today_date).days
        birthday_year += 1
