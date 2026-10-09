"""
Problem   : The Resonance Gallery Walk
Platform  : Unstop
Link      : https://unstop.com/code/practice/661683
Difficulty: Medium
Topics    : Array, Sliding Window, Monotonic Queue, Hashing, Deque
Date      : 2026-10-09

Approach:
    For every window of size W, print the maximum value and how many
    times it occurs in that window.
    - A monotonic decreasing deque (storing indices) gives the window
      maximum in amortized O(1): pop smaller elements from the back on
      insert, pop expired indices from the front.
    - A frequency hashmap tracks counts of values currently in the
      window: increment on entry, decrement (and delete at zero) on exit.
    - The answer for each window is (arr[dq[0]], freq[arr[dq[0]]]).

Complexity:
    Time : O(N), each index is pushed and popped from the deque at most once,
           and each hashmap update is O(1) on average.
    Space: O(W), for the deque and the frequency map.
"""



# --------------------------------------------- Solution ---------------------------------------------------


from collections import deque
import sys

def solve():
    input = sys.stdin.readline
    N, W = map(int, input().split())
    arr = list(map(int, input().split()))
    dq = deque()
    freq = {}
    for i in range(N):
        if i >= W:
            outgoing = arr[i - W]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        while dq and dq[0] <= i - W:
            dq.popleft()
        if i >= W - 1:
            maximum = arr[dq[0]]
            print(maximum, freq[maximum])

if __name__ == "__main__":
    solve()
