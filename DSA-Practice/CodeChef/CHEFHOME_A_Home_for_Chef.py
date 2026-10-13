"""
Problem   : A Home for Chef (CHEFHOME)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHEFHOME
Difficulty: 1815
Date      : 2026-10-13
Topics    : Math, Sorting, Median, Manhattan Distance

Approach:
    Total Manhattan distance = sum|x - xi| + sum|y - yi|, so the x and y
    axes are independent. Each sum is minimized when the coordinate lies
    between the two middle values of the sorted array (the median range).
      - n odd : the median is unique, so 1 choice per axis.
      - n even: any integer in [a[n/2 - 1], a[n/2]] works.
    Using a[n//2] - a[(n-1)//2] + 1 handles both cases.
    Answer = (valid x choices) * (valid y choices).

Time  : O(n log n) per test case (sorting)
Space : O(n)
"""


# ------------------------------------------------- Solution ---------------------------------------------------------------


t = int(input())

for _ in range(t):
    n = int(input())
    x_coords = []
    y_coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)
    x_coords.sort()
    y_coords.sort()
    x_count = x_coords[n // 2] - x_coords[(n - 1) // 2] + 1
    y_count = y_coords[n // 2] - y_coords[(n - 1) // 2] + 1
    print(x_count * y_count)
