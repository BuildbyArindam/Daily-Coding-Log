"""
Problem   : Countries Grouping
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/countries-grouping-1-5b13620a/
Difficulty: Easy
Topics    : Arrays, Implementation, Math, Recursion
Date      : 2026-08-19

Approach:
    Greedily scan the array left to right. At each position i, the value
    a[i] declares the size of the current "country group." Validate that
    the next `group_size` elements are all equal to `group_size` itself
    (i.e., the group is internally consistent) and that the group doesn't
    run past the end of the array. If every group checks out, advance the
    pointer past the group and increment the country count; otherwise mark
    the data as invalid and stop early.

Time Complexity : O(n) per test case — single left-to-right pass, each
                   index visited exactly once across the outer while/inner for.
Space Complexity: O(n) for storing the input array (O(1) extra beyond input).
"""


# ------------------------- Solution ----------------------------

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        a = list(map(int, input_data[idx + 1 : idx + 1 + n]))
        idx += 1 + n
        country_count = 0
        valid = True
        i = 0
        while i < n:
            group_size = a[i]
            if i + group_size > n:
                valid = False
                break
            for j in range(i, i + group_size):
                if a[j] != group_size:
                    valid = False
                    break
            if not valid:
                break
            country_count += 1
            i += group_size 
        if valid:
            print(country_count)
        else:
            print("Invalid Data")

if __name__ == '__main__':
    solve()
