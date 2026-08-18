# Problem: Enough Chairs
# Link: https://www.codechef.com/problems/PWTHC
# Date Solved: 2026-08-18
# Difficulty: Easy (Basic/School level)
# Topics: Math, Implementation
#
# Approach:
# There are n rooms, each with k chairs, so total available seating
# capacity is n * k. Compare this against p (number of people).
# If capacity >= people, everyone can be seated ("YES"), else ("NO").
#
# Time Complexity: O(1) - single arithmetic comparison
# Space Complexity: O(1) - only a few integer variables


# ----------------------- Solution -------------------------

def check_seating():
    values = input().split()
    n = int(values[0])
    k = int(values[1])
    p = int(values[2])
    available = n * k
    if available < p:
        print("NO")
    else:
        print("YES")

check_seating()
