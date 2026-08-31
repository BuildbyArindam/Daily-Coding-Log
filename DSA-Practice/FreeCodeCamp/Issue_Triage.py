"""
Problem: Issue Triage
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-08
Date Solved: 2026-08-31
Difficulty: Easy
Topics: Conditional Statements, String Manipulation, Time-based Logic

Approach:
Compare the issue's age (ms) against a 7-day threshold (604,800,000 ms).
If it's younger than a week, leave it. If it's older and the message
contains "bump" (case-insensitive), close it. Otherwise, bump it.

Time Complexity: O(n) — n = length of message (due to .lower() and substring search)
Space Complexity: O(n) — .lower() creates a new string
"""


# -------------------------- Solution ------------------------------


def triage_issue(ms, message):
    if ms < 604800000:
        return "leave it"
    elif "bump" in message.lower():
        return "close it"
    else:
        return "bump it"
