"""
Problem: Supreme Subset
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/supreme-subset-bb866a75/
Date: 2026-08-29
Difficulty: Easy
Topics: Data Structures, Math, One-dimensional, Sets

Approach:
Group array elements by their remainder mod m (num % m). Since two numbers
in the same group differ by a multiple of m, any subset formed from one
group is internally consistent per the problem's grouping constraint. Pick
the group with the maximum size; break ties by choosing the lexicographically
smaller sorted list among equally-sized groups. Print the group's size
followed by its (sorted) elements.

Time Complexity: O(n log n)  — dominated by sorting the array
Space Complexity: O(n)       — for the remainder groups
"""


# -------------------------- Solution ---------------------------------


import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    arr = sorted(int(x) for x in input_data[2:2 + n])
    groups = defaultdict(list)
    for num in arr:
        groups[num % m].append(num)
    best_group = []
    for remainder, subset in groups.items():
        if len(subset) > len(best_group):
            best_group = subset
        elif len(subset) == len(best_group):
            if subset < best_group:
                best_group = subset
    print(len(best_group))
    print(*(best_group))

if __name__ == '__main__':
    solve()
