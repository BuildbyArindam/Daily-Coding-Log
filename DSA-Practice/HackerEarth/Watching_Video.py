"""
Problem   : Watching Video
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/video-watching-8c6cbee6/
Difficulty: Medium
Topics    : Binary Search, Greedy, Searching
Date      : 2026-10-07

Approach:
  - Video length L = total_data // d seconds.
  - Starting playback at second t is valid if, for every k in 1..L, the data
    received by second t+k (capped at N) is >= k*d.
  - Define A[i] = prefix[i] - i*d. The check for each start t becomes
    "min of A over the relevant window >= d*(1 - t)".
  - Sliding-window minimum (monotonic deque) handles windows of size L;
    a suffix-minimum array handles windows that run past packet N.
  - Scan t = 1..N and print the first valid t (earliest start).

Complexity:
  Time : O(N)  (each index enters/leaves the deque once)
  Space: O(N)  (prefix/suffix/window arrays)
"""


# ----------------------------------------- Solution -------------------------------------------------


from collections import deque

N, d = map(int, input().split())
X = list(map(int, input().split()))
total = sum(X)
if total == 0:
    print(0)
    exit()
video_length = total // d
A = [0] * (N + 1)
prefix = 0
for i in range(1, N + 1):
    prefix += X[i - 1]
    A[i] = prefix - i * d
suffix_min = [0] * (N + 2)
suffix_min[N] = A[N]
for i in range(N - 1, 0, -1):
    suffix_min[i] = min(A[i], suffix_min[i + 1])
window_min = [0] * (N + 1)
if video_length < N:
    dq = deque()
    for i in range(1, N + 1):
        while dq and dq[0] <= i - video_length:
            dq.popleft()
        while dq and A[dq[-1]] >= A[i]:
            dq.pop()
        dq.append(i)
        if i >= video_length:
            start = i - video_length + 1
            window_min[start] = A[dq[0]]
for t in range(1, N + 1):
    if video_length >= N or t > N - video_length + 1:
        min_balance = suffix_min[t]
    else:
        min_balance = window_min[t]
    required = d * (1 - t)
    if min_balance >= required:
        print(t)
        break
