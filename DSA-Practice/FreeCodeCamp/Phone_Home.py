"""
Problem: Phone Home
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-06
Date Solved: 2026-09-09
Difficulty: Easy
Topics: Arrays, Math, Simulation

Approach:
Sum all hop distances in the route to get total distance, then compute
travel time using a fixed signal speed (300,000 km/s). Each hop after
the first adds a fixed 0.5s transmission/relay delay. Total time is
travel time + cumulative transmission delay, rounded to 4 decimals.

Time Complexity: O(n) — single pass to sum the route list
Space Complexity: O(1) — only scalar accumulators used
"""


# ------------------------------ Solution ------------------------------------


def send_message(route):
    distance = sum(route)
    travel_time = distance / 300000
    transmission_delay = (len(route) - 1) * 0.5
    return round(travel_time + transmission_delay, 4)
