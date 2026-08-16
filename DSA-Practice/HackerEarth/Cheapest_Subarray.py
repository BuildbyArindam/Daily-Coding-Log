"""
Problem   : Cheapest Subarray
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/cheapest-subarray-d628cb65/
Difficulty: Easy
Topics    : Arrays, Basic Programming, Implementation, Looping Statements
Date      : 2026-08-16

Approach:
    For each test case, slide over the array and compute the sum of every
    pair of adjacent elements (i.e. every contiguous subarray of length 2).
    Track the minimum such sum. Answer is that minimum ("cheapest subarray").

Complexity (per test case, N = array size):
    Time  : O(N)      -> single pass over the array
    Space : O(N)      -> storing the array itself (O(1) extra beyond input)
"""


# ----------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(input_data[idx])
        idx += 1
        arr = [int(x) for x in input_data[idx:idx + N]]
        idx += N
        min_cost = float('inf')
        for i in range(N - 1):
            cost = arr[i] + arr[i + 1]
            if cost < min_cost:
                min_cost = cost
        out.append(str(min_cost))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
