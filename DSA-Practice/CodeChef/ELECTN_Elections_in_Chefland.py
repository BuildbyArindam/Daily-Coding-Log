"""
Problem   : Elections in Chefland
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/ELECTN
Difficulty: 604
Topics    : Arrays, Counting, Basic Programming / Implementation
Date      : 2026-09-14

Approach:
For each test case, read N voters' ages and a threshold X (minimum
voting age). Iterate through the ages array once, incrementing a
counter whenever an age is >= X. Print the count — this represents
the number of eligible voters.

Time Complexity : O(N) per test case
Space Complexity: O(N) for storing the ages array (O(1) extra if
                  processed while reading input)
"""


# -------------------------- Solution ----------------------------------


T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    ages = list(map(int, input().split()))

    count = 0
    for age in ages:
        if age >= X:
            count += 1

    print(count)
