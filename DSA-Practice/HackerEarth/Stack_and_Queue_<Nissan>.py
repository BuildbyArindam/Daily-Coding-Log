"""
Problem   : Stack and Queue <Nissan>
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/staque-1-e790a29f/
Date      : 2026-09-28
Difficulty: Easy
Topics    : Arrays, Data Structures, Implementation, Queue, Stacks

Approach:
    Take x elements from the front of the array (prefix) and K - x from
    the back (suffix), and maximize the combined sum over x. Start with the
    suffix sum of the last K-1 elements. For each x from 1 to K, add A[x-1]
    to the prefix sum and record the total. Then drop the suffix's leftmost
    element, A[N-K+x], so the sums update in O(1) each step (sliding window).

Time  : O(K)
Space : O(1) extra (O(N) to store the input)
"""


# ---------------------------------- Solution -------------------------------------------------


N, K = map(int, input().split())
A = list(map(int, input().split()))
suffix_sum = sum(A[N - (K - 1):]) if K > 1 else 0
top_sum = 0
ans = 0
for x in range(1, K + 1):
    top_sum += A[x - 1]
    current_sum = top_sum + suffix_sum
    ans = max(ans, current_sum)
    if x < K:
        suffix_sum -= A[N - K + x]
print(ans)
