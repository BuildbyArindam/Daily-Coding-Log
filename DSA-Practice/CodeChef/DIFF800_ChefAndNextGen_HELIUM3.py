"""
Problem: Chef and NextGen (HELIUM3)
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/HELIUM3
Date: 2026-08-15
Difficulty: 800 (Beginner)
Topic: Math / Basic Programming

Approach:
Chefland needs A units of power/year for B years -> total power needed = A * B.
The moon has X grams of Helium-3, each gram yielding Y units of power
-> total power available = X * Y.
Funding is granted if available_power >= required_power.
Just compare the two products directly - no loops or algorithms needed.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# ----------------------- Solution ----------------------------


T = int(input())
for _ in range(T):
    A, B, X, Y = map(int, input().split())
    required_power = A * B
    available_power = X * Y
    if available_power >= required_power:
        print("Yes")
    else:
        print("No")
