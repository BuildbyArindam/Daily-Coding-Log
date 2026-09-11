"""
Problem   : Roy and Trains
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roy-and-trains-2/
Date      : 2026-09-11
Difficulty: Easy
Topics    : Implementation, Math

Approach:
    For each test case, Roy can only catch a train that departs at or
    after his arrival time (T0). For each of the two trains whose
    departure time (T1/T2) is >= T0, compute the travel time needed to
    cover distance D at that train's speed, rounding UP since partial
    minutes still take a full minute:
        travel = ceil((D * 60) / V)
    The arrival time is departure_time + travel. Take the minimum
    arrival time across both feasible trains; if neither train is
    catchable, output -1.

Complexity:
    Time  : O(1) per test case  -> O(T) overall
    Space : O(1) extra (excluding input buffer and output list)
"""


# ------------------------- Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    pos = 1
    answers = []
    for _ in range(T):
        T0 = int(input_data[pos])
        T1 = int(input_data[pos + 1])
        T2 = int(input_data[pos + 2])
        V1 = int(input_data[pos + 3])
        V2 = int(input_data[pos + 4])
        D = int(input_data[pos + 5])
        pos += 6
        ans = float("inf")
        if T0 <= T1:
            travel1 = (D * 60 + V1 - 1) // V1
            ans = min(ans, T1 + travel1)
        if T0 <= T2:
            travel2 = (D * 60 + V2 - 1) // V2
            ans = min(ans, T2 + travel2)
        if ans == float("inf"):
            answers.append("-1")
        else:
            answers.append(str(ans))
    print("\n".join(answers))

if __name__ == "__main__":
    solve()
