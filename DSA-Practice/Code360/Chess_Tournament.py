"""
Problem   : Chess Tournament
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/chess-tournament_981299?kunjiRedirection=true
Difficulty: Easy
Topic     : Binary Search on Answer (aggressive-cows pattern), Greedy, Arrays
Date      : 2026-09-02

Approach:
    Binary search on the answer (aggressive-cows pattern).
    Sort player positions, then binary search over the possible minimum
    distance `d` between any two placed players. For each candidate `d`,
    greedily walk the sorted positions and place a player whenever the
    gap from the last placed player is >= d, checking if all `c` players
    can be placed. The largest feasible `d` is the answer.

Time complexity : O(n log n) for sorting + O(n log(range)) for the binary
                   search (each feasibility check is O(n)) = O(n log(range)).
Space complexity: O(1) auxiliary (ignoring sort's internal space).
"""


# ------------------------- Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *

def chessTournament(positions, n, c):
    positions.sort()
    def canPlace(dist):
        players = 1
        last_position = positions[0]
        for i in range(1, n):
            if positions[i] - last_position >= dist:
                players += 1
                last_position = positions[i]
                if players == c:
                    return True
        return False
    low = 0
    high = positions[-1] - positions[0]
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if canPlace(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer
