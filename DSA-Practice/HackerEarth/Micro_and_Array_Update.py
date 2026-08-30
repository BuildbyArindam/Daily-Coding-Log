"""
Problem   : Micro and Array Update
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/
Difficulty: Easy
Topics    : Ad-Hoc, Data Structures, One-dimensional

Approach:
    For each element to reach at least K, it can only be incremented
    by 1 each "second" (one update per second, per problem statement).
    The bottleneck is the array's minimum value, since every other
    element is already >= min_val. So the minimum number of seconds
    needed is max(0, K - min(arr)).

Time Complexity : O(N) per test case (single pass to find min)
Space Complexity: O(N) to store the array (O(1) extra beyond input)
"""


# ----------------------- Solution -------------------------


def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        min_val = min(arr)
        time_needed = max(0, K - min_val)
        print(time_needed)

if __name__ == '__main__':
    solve()
