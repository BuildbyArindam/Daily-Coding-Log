"""
Problem   : Bus Seating
Platform  : CodeChef (START256D)
Link      : https://www.codechef.com/START256D/problems/BUSSEAT
Date      : 2026-09-16
Difficulty: Easy / Cakewalk
Topics    : Math, Greedy, Ad-hoc

Approach:
    For each test case, compute the surplus passengers beyond the
    available rows (passengers - rows). If there's no surplus, 0
    extra people are needed. Otherwise, each surplus passenger
    requires 2 additional seats/people (per problem's seating rule),
    so the answer is surplus * 2.

Complexity:
    Time  : O(1) per test case, O(T) overall
    Space : O(1) extra (excluding input buffering)
"""


# ---------------------------------- Solution ----------------------------------------


import sys

def bus_seating_people(rows, passengers):
    surplus = passengers - rows
    if surplus <= 0:
        return 0
    return surplus * 2

def main():
    data = sys.stdin.read().split()
    idx = 0
    total_cases = int(data[idx]); idx += 1
    output_lines = []
    for _ in range(total_cases):
        n_val = int(data[idx]); idx += 1
        k_val = int(data[idx]); idx += 1
        result = bus_seating_people(n_val, k_val)
        output_lines.append(str(result))
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
