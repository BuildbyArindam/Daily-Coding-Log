"""
Problem   : Largest Substring
Platform  : HackerEarth (Easy)
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/flipping-the-string-831bbbbe/
Date      : 2026-10-02
Topics    : Strings, Prefix Sum, Monotonic Stack

Approach:
    Map '0' -> +1 and '1' -> -1 and build a prefix-sum array. A substring
    (i, j] has more 0s than 1s exactly when prefix[j] > prefix[i], so the
    task becomes finding the maximum j - i with prefix[j] > prefix[i].
    1. Left to right, keep a stack of indices whose prefix values are strictly
       decreasing. Only these can be the best left endpoint.
    2. Right to left, while prefix[j] > prefix[stack top], pop i and update
       answer = max(answer, j - i). A popped i is never needed again, since
       any smaller j would give a shorter length.

Complexity:
    Time  : O(N), each index is pushed and popped at most once
    Space : O(N) for the prefix array and the stack
"""


# ------------------------------- Solution -------------------------------------------------------


N = int(input())
S = input().strip()
prefix = [0] * (N + 1)
for i in range(N):
    if S[i] == '0':
        prefix[i + 1] = prefix[i] + 1
    else:
        prefix[i + 1] = prefix[i] - 1
stack = []
for i in range(N + 1):
    if not stack or prefix[i] < prefix[stack[-1]]:
        stack.append(i)
answer = 0
for j in range(N, -1, -1):
    while stack and prefix[j] > prefix[stack[-1]]:
        i = stack.pop()
        answer = max(answer, j - i)
print(answer)
