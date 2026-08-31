"""
Problem   : Permutation Swaps
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/guess-permutation-2-be0b2b90/
Difficulty: Easy
Topics    : Linear Search, Algorithms, Greedy Algorithm
Date      : 2026-08-31

Approach:
Check if array A can be rearranged into a valid permutation of 1..N using
only prefix operations (interpreted from the "guess permutation" swap
constraints). First reject early if sum(A) != N*(N+1)/2, since any valid
answer must match the target sum. Then greedily verify that every prefix
sum of A is at least as large as the minimum possible prefix sum of a
valid permutation (1+2+...+k for the first k elements) — if any prefix
falls short, it's impossible to fix via allowed swaps, so answer "NO".

Time complexity : O(N) per test case  ->  O(sum(N)) overall
Space complexity: O(N) for storing the array (O(1) extra beyond input)
"""


# --------------------------- Solution ------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        target_sum = N * (N + 1) // 2
        if sum(A) != target_sum:
            ans.append("NO")
            continue
        prefix_sum = 0
        possible = True
        for k in range(1, N + 1):
            prefix_sum += A[k - 1]
            minimum_prefix = k * (k + 1) // 2
            if prefix_sum < minimum_prefix:
                possible = False
                break
        ans.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
