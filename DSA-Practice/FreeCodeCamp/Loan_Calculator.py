"""
Problem   : Loan Calculator
Platform  : FreeCodeCamp — Daily Coding Challenge (07-24)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/07-24
Date      : 2026-09-04
Difficulty: Easy-Medium
Topics    : Simulation, Math, Loops, Financial Computation

Approach:
Simulate the loan month-by-month. On each iteration, apply interest to
the current balance, then subtract the fixed monthly payment. Record
the running (rounded) balance after each payment into a schedule list,
stopping once the balance reaches zero or below (clamped to 0 on the
final entry so the schedule ends cleanly).

Time Complexity : O(n), where n = number of months to pay off the loan
Space Complexity: O(n), for storing the balance at each month in `schedule`
"""


# --------------------------- Solution ----------------------------------


def get_loan_schedule(loan_amount, annual_rate, monthly_payment):
    balance = loan_amount
    monthly_rate = (annual_rate / 100) / 12
    schedule = [loan_amount]
    while balance > 0:
        balance = balance + (balance * monthly_rate) - monthly_payment
        if balance <= 0:
            schedule.append(0)
            break
        schedule.append(round(balance))
    return schedule
