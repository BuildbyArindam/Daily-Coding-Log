"""
Problem: A Plane Journey
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/people-carrying-6dd467ed/
Date Solved: 2026-09-22
Difficulty: Medium
Topics: Algorithms, Binary Search

Approach:
    Binary search on the answer (the group size 'k' of people boarding 
    together per plane). For a given k, greedily check feasibility: sort 
    passenger weights (A) and plane capacities (B) in descending order, 
    and try to seat groups of size k into planes in order of decreasing 
    capacity, ensuring the heaviest unseated passenger never exceeds the 
    current plane's capacity. Binary search finds the minimum feasible k, 
    and the final answer is derived as (2*k - 1) based on the problem's 
    boarding-order constraint.

Time Complexity:  O(N log N) for the binary search over feasibility checks, 
                   each O(N), giving O(N log N) overall.
Space Complexity: O(N) for storing and sorting A and B.
"""


# --------------------------------------- Solution -------------------------------------------


import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if max(A) > max(B):
        print(-1)
        return
    A.sort(reverse=True)
    B.sort(reverse=True)
    def possible(k):
        i = 0 
        for capacity in B:
            if i == N:
                return True
            if A[i] > capacity:
                return False
            take = min(k, N - i)
            i += take
        return i == N
    low, high = 1, N
    while low < high:
        mid = (low + high) // 2
        if possible(mid):
            high = mid
        else:
            low = mid + 1
    answer = 2 * low - 1
    print(answer)

if __name__ == "__main__":
    main()
