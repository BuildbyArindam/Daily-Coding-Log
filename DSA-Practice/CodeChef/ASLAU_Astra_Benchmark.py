# Problem: Astra Benchmark
# Link: https://www.codechef.com/problems/ASLAU
# Date Solved: 2026-09-09
# Difficulty: Easy (Beginner)
# Topics: Basic Math, Conditional Logic, Greedy
#
# Approach:
# Sum the two given capacities (A, B) and compare against the threshold X.
# If A + B >= X, the combined capacity meets or exceeds the requirement -> "YES"
# Otherwise -> "NO". A single-pass arithmetic + comparison problem, no loops needed.
#
# Time Complexity: O(1)
# Space Complexity: O(1)


# -------------------------- Solution ----------------------------------------


A, B, X = map(int, input().split())

if A + B >= X:
    print("YES")
else:
    print("NO")
