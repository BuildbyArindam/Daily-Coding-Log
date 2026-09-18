"""
Problem: Bus Seat Numbering
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SEATNUMBER
Date: 2026-09-18
Difficulty: 613
Topics: Implementation, Conditional Logic, Ad-Hoc, Simulation

Approach:
Each seat number N falls into one of four fixed ranges corresponding to
a bus seating layout (Lower Double / Lower Single / Upper Double / Upper
Single). Just check which range N lands in and print the label — no
computation needed beyond simple conditionals.

Time Complexity: O(1) per query, O(T) overall
Space Complexity: O(1)
"""


# ---------------------------------- Solution -----------------------------------------


T = int(input())

for _ in range(T):
    N = int(input())

    if 1 <= N <= 10:
        print("Lower Double")
    elif 11 <= N <= 15:
        print("Lower Single")
    elif 16 <= N <= 25:
        print("Upper Double")
    else:
        print("Upper Single")
