"""
Problem   : Elevator Overload
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/lift-trouble-7e3bc27d/
Date      : 2026-08-18
Difficulty: Easy
Topic     : Basic Programming, Implementation

Approach:
Simulate the elevator floor by floor (1 to n-1). At each floor, first remove
passengers who exit at that floor (tracked via exiting_count/exiting_weight
arrays indexed by destination floor), then add passengers who board at that
floor, updating running totals of people count and weight. After boarding at
a floor, check if the running count exceeds capacity P or running weight
exceeds limit W — if so, the elevator overloads and stops at that floor.
If no floor causes an overload, the elevator successfully reaches floor n.

Time Complexity : O(N + M) per test case, where N is the number of floors
                   and M is the total number of passengers across all floors
                   (each passenger is processed once when boarding and once
                   when marked to exit).
Space Complexity: O(N + M) for storing per-floor passenger lists and the
                   exiting_count/exiting_weight arrays.
"""


# -------------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    t = int(next(iterator))
    for _ in range(t):
        n = int(next(iterator))
        P = int(next(iterator))
        W = int(next(iterator))
        waiting_counts = [int(next(iterator)) for _ in range(n - 1)]
        floor_passengers = []
        for i in range(n - 1):
            count = waiting_counts[i]
            destinations = [int(next(iterator)) for _ in range(count)]
            weights = [int(next(iterator)) for _ in range(count)]
            floor_passengers.append(list(zip(destinations, weights)))
        exiting_weight = [0] * (n + 1)
        exiting_count = [0] * (n + 1)
        curr_people = 0
        curr_weight = 0
        stopped_floor = n 
        for f in range(1, n):
            curr_people -= exiting_count[f]
            curr_weight -= exiting_weight[f]
            for dest, w in floor_passengers[f - 1]:
                curr_people += 1
                curr_weight += w
                exiting_count[dest] += 1
                exiting_weight[dest] += w
            if curr_people > P or curr_weight > W:
                stopped_floor = f
                break
        print(stopped_floor)

if __name__ == '__main__':
    solve()
