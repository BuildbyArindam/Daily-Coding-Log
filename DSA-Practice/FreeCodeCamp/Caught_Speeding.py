"""
Problem: Caught Speeding
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-26
Date Solved: 2026-09-06
Difficulty: Easy
Topics: Arrays, Basic Math, Filtering/Aggregation, Conditional Logic

Approach:
Iterate through the speeds list once, and for every speed exceeding
the limit, record how much over the limit it was (speed - limit).
If no vehicle was speeding, return [0, 0]. Otherwise return the count
of speeding vehicles and the average amount they were over the limit.

Time Complexity: O(n) — single pass through the speeds list
Space Complexity: O(k) — where k is the number of speeding vehicles
                   (stores their overage amounts)
"""


# --------------------- Solution --------------------------------


def speeding(speeds, limit):
    speeding_vehicles = []
    for speed in speeds:
        if speed > limit:
            speeding_vehicles.append(speed - limit)
    if len(speeding_vehicles) == 0:
        return [0, 0]
    count = len(speeding_vehicles)
    average = sum(speeding_vehicles) / count
    return [count, average]
