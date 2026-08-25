"""
Problem: The Great Kian
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-great-kian/
Platform: HackerEarth
Date Solved: 2026-08-25
Difficulty: Easy
Topic: Brute-force search / Implementation

Approach:
Split the array into 3 groups based on index position mod 3
(indices 0,3,6,... | 1,4,7,... | 2,5,8,...) and print the sum
of each group.

Time Complexity: O(N)  — single pass over the array (3 slices, each element visited once)
Space Complexity: O(N) — storing the input array
"""


# ---------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    sum1 = sum(arr[i] for i in range(0, n, 3))
    sum2 = sum(arr[i] for i in range(1, n, 3))
    sum3 = sum(arr[i] for i in range(2, n, 3))
    print(f"{sum1} {sum2} {sum3}")

if __name__ == '__main__':
    solve()
