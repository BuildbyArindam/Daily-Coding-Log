"""
Problem   : Sherlock and Dates
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sherlock-and-dates/
Difficulty: Easy
Topics    : Ad-Hoc, Algorithms, Implementation

Approach:
  A "lucky" date exists only when the 2-digit year (YY = year % 100)
  falls in [3, 13]; for such YY, the lucky date is month=YY-1, day=YY-2.
  So each century has exactly 11 lucky dates, one per qualifying year.
  count_lucky_years(y) gives a closed-form count of lucky dates in
  years [1, y] using divmod, avoiding a year-by-year loop.
  For each query range [D1:M1:Y1, D2:M2:Y2], the answer is
  count_upto(end) - count_before(start), i.e. a prefix-count difference.

Complexity:
  Time : O(1) per query (closed-form year counting) -> O(T) overall
  Space: O(1) extra
"""


# --------------------------- Solution --------------------------------


name = input()
T = int(name)

def count_lucky_years(y):
    """
    Number of lucky years from year 1 through year y.

    A lucky year must have:
        03 <= year % 100 <= 13

    So every block of 100 years has 11 lucky years.
    """
    if y <= 0:
        return 0
    full_blocks, remainder = divmod(y, 100)
    count = full_blocks * 11
    if remainder >= 3:
        count += min(remainder, 13) - 2
    return count

def lucky_date_in_year(year):
    """
    Return (month, day) of the lucky date for this year,
    or None if the year has no lucky date.
    """
    x = year % 100
    if 3 <= x <= 13:
        month = x - 1
        day = x - 2
        return month, day
    return None

def count_upto(day, month, year):
    """
    Number of lucky dates <= DD:MM:YYYY.
    """
    ans = count_lucky_years(year - 1)
    lucky = lucky_date_in_year(year)
    if lucky is not None:
        lucky_month, lucky_day = lucky
        if (lucky_month, lucky_day) <= (month, day):
            ans += 1
    return ans

def count_before(day, month, year):
    """
    Number of lucky dates < DD:MM:YYYY.
    """
    ans = count_lucky_years(year - 1)
    lucky = lucky_date_in_year(year)
    if lucky is not None:
        lucky_month, lucky_day = lucky
        if (lucky_month, lucky_day) < (month, day):
            ans += 1
    return ans

for _ in range(T):
    d1, d2 = input().split()
    day1, month1, year1 = map(int, d1.split(':'))
    day2, month2, year2 = map(int, d2.split(':'))
    answer = (
        count_upto(day2, month2, year2)
        - count_before(day1, month1, year1)
    )
    print(answer)
