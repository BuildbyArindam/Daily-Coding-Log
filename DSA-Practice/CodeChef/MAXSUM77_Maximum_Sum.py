"""
Problem   : Maximum Sum
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MAXSUM77
Date      : 2026-09-04
Difficulty: Easy
Topic     : Arrays, Sliding Window.

Approach  :
    We need to choose a contiguous subarray of length (N - K) that has the
    maximum possible sum. Start by computing the sum of the first window of
    size (N - K), then slide the window one element at a time across the
    array — add the incoming element, remove the outgoing element, and track
    the running maximum. This avoids recomputing the window sum from scratch
    at each position.

Time complexity  : O(N) per test case  -> O(sum(N)) overall
Space complexity : O(N) for storing the array (O(1) extra beyond input)
"""





T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    length = N - K
    current_sum = sum(A[:length])
    maximum_sum = current_sum
    for i in range(length, N):
        current_sum += A[i]
        current_sum -= A[i - length]
        maximum_sum = max(maximum_sum, current_sum)
    print(maximum_sum)
