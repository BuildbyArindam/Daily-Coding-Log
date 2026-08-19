"""
Problem: Techfest and Group Photo
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/techfest-and-group-photo-06dfebc0/
Date: 2026-08-19
Difficulty: Easy
Topic: Basic Programming, Sorting

Approach:
    For each person removed, the photo area = (total_width - their_width) * (max_height_among_remaining).
    Instead of recomputing max height per removal (O(n) each -> O(n^2) total), precompute the
    largest (max_h1) and second-largest (max_h2) heights in a single pass.
    - If the removed person's height == max_h1, the remaining max height is max_h2.
    - Otherwise, it's still max_h1.
    This correctly handles duplicate max heights since the second occurrence of the max value
    gets captured into max_h2 during the scan.

Time Complexity: O(n)  -- one pass to find max_h1/max_h2, one pass to build the answer
Space Complexity: O(n) -- for the dim list and output list
"""


# ---------------------------- Solution --------------------------------


import sys

def solve (dim):
    # Write your code here
    n = len(dim)
    total_width = sum(w for w, h in dim)
    max_h1, max_h2 = 0, 0
    for _, h in dim:
        if h > max_h1:
            max_h2 = max_h1
            max_h1 = h
        elif h > max_h2:
            max_h2 = h   
    ans = []
    for w, h in dim:
        current_w = total_width - w
        current_h = max_h2 if h == max_h1 else max_h1
        ans.append(current_w * current_h)
    return ans

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        dim = []
        idx = 1
        for _ in range(n):
            w = int(input_data[idx])
            h = int(input_data[idx + 1])
            dim.append((w, h))
            idx += 2
        out_ = solve(dim)
        print(' '.join(map(str, out_)))
