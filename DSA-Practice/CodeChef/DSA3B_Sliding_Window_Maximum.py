"""
Problem   : Sliding Window Maximum
Platform  : CodeChef (DSA3B)
Link      : https://www.codechef.com/problems/DSA3B
Difficulty: 1600
Date      : 2026-10-19
Topics    : Sliding Window, Monotonic Deque, Arrays

Approach:
    Maintain a monotonic deque of indices whose values are in decreasing
    order, implemented as an array `buf` with `front`/`back` pointers.
    For each new element, pop smaller elements from the back, then push
    the current index. If the front index has slid out of the window
    (<= i - k), pop it from the front. The front of the deque is always
    the maximum of the current window.

Complexity:
    Time : O(N) per test case, since each index is pushed and popped at most once.
    Space: O(N) for the index buffer and the result list.
"""


# ----------------------------------------------- Solution ----------------------------------------------------------------


def max_sum_subarray_k(arr, n, k):
    buf = [0] * n
    front = 0
    back = 0

    for i in range(k):
        while back > front and arr[buf[back - 1]] <= arr[i]:
            back -= 1
        buf[back] = i
        back += 1
    result = [arr[buf[front]]]
    for i in range(k, n):
        while back > front and arr[buf[back - 1]] <= arr[i]:
            back -= 1
        buf[back] = i
        back += 1
        if buf[front] <= i - k:
            front += 1

        result.append(arr[buf[front]])

    return result


# -- Input handling (Dont edit below code) --

T = int(input())
    
for _ in range(T):
    N, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res=max_sum_subarray_k(arr, len(arr), k)
    print(*res)
