# Problem: Bath in Winters
# Platform: CodeChef
# Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BATH
# Date Solved: 2026-09-18
# Difficulty: 643
# Topics: Math, Implementation
#
# Approach:
# Each bath needs Y liters of hot water mixed with an equal amount of cold
# water (so 2*Y liters of water total per person). With X liters of water
# available, the number of people who can bathe is simply the integer
# division X // (2*Y).
#
# Time Complexity: O(1) per test case, O(T) overall
# Space Complexity: O(1)


# ------------------------------- Solution ------------------------------------------------


T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    water_needed = 2 * Y
    people = X // water_needed
    print(people)
