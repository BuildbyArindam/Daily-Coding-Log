"""
Problem   : Chef and Time Machine (CHEFTMA)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHEFTMA
Difficulty: 1717
Date      : 2026-10-01
Topics    : 1D Arrays, Multiset, Greedy, Data Structures, Arrays, Sets, Algorithms, Heap (Priority Queue)

Approach:
    Compute the remaining amount for each item as A[i] - B[i] and merge
    the two button lists C and D into one. Sort both. Sweep the remaining
    values in ascending order, pushing every button that fits the current
    capacity onto a max-heap, then apply the largest fitting button. Since
    capacities only grow, a button that fit earlier still fits later, so
    the greedy choice is safe. The answer is sum(remaining) - total saved.

Complexity:
    Time : O((N + K + M) log(N + K + M))  (sorting + heap operations)
    Space: O(N + K + M)
"""


# ------------------------------------- Solution -----------------------------------------------


import sys
import heapq

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    for _ in range(T):
        N, K, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        D = list(map(int, input().split()))
        remaining = [A[i] - B[i] for i in range(N)]
        buttons = C + D
        remaining.sort()
        buttons.sort()
        max_heap = []
        j = 0
        saved = 0
        for capacity in remaining:
            while j < len(buttons) and buttons[j] <= capacity:
                heapq.heappush(max_heap, -buttons[j])
                j += 1
            if max_heap:
                saved += -heapq.heappop(max_heap)
        total_remaining = sum(remaining) - saved
        print(total_remaining)

if __name__ == "__main__":
    solve()
