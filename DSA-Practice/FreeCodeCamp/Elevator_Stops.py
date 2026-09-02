"""
Problem: Elevator Stops
Platform: FreeCodeCamp - Daily Coding Challenge (07-19)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-19
Date Solved: 2026-09-02
Difficulty: Easy-Medium
Topics: Arrays, Greedy, Simulation, Math

Approach:
Dedupe and sort the stop floors, then split them into those below,
above, and equal to the current floor. Compute total travel distance
for two strategies - go up first then down, or down first then up -
and pick whichever minimizes total distance. Serve the current-floor
stop first, then follow the chosen direction order.

Time Complexity: O(n log n) - dominated by sorting the stops
Space Complexity: O(n) - for the below/above/current lists
"""


# ----------------------- Solution ----------------------------


def elevator_stops(current_floor, stops):
    stops = sorted(set(stops))
    if not stops:
        return current_floor
    below = [floor for floor in stops if floor < current_floor]
    above = [floor for floor in stops if floor > current_floor]
    current = [floor for floor in stops if floor == current_floor]
    if above:
        highest = max(above)
    else:
        highest = current_floor
    if below:
        lowest = min(below)
    else:
        lowest = current_floor
    up_first_distance = (highest - current_floor) + (highest - lowest)
    down_first_distance = (current_floor - lowest) + (highest - lowest)
    result = current.copy()
    if up_first_distance <= down_first_distance:
        result += sorted(above)
        result += sorted(below, reverse=True)
    else:
        result += sorted(below, reverse=True)
        result += sorted(above)
    return result
