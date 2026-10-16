"""
Problem   : The First to Peak
Platform  : Unstop
Link      : https://unstop.com/code/practice/662453
Difficulty: Medium
Topics    : Sliding Window, Monotonic Queue, Hashing, Sorting
Date      : 2026-10-16

Approach:
    Slide a window of size K over the readings. A monotonic decreasing deque
    of indices keeps the window's maximum at the front. Elements smaller than
    the incoming one are popped from the back, and indices that have left the
    window are popped from the front. Equal temperatures are not popped, so
    the earliest index among ties stays at the front and wins.
    Once the first full window is formed (i >= K - 1), credit the sensor at
    dq[0] with one win in a hash map. Finally, sort sensors by credits
    (descending), then by sensor ID (ascending).

Complexity:
    Time  : O(N + S log S), where S is the number of distinct winning sensors.
            Each index is pushed and popped at most once.
    Space : O(N) for the input arrays, plus O(K) for the deque and O(S) for
            the credits map.
"""


# ---------------------------------------------- Solution -------------------------------------------------------------


import sys
from collections import deque, defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    N, K = data[0], data[1]
    sensors = []
    temperatures = []
    idx = 2
    for _ in range(N):
        sensors.append(data[idx])
        temperatures.append(data[idx + 1])
        idx += 2
    dq = deque()
    credits = defaultdict(int)
    for i in range(N):
        while dq and dq[0] <= i - K:
            dq.popleft()
        while dq and temperatures[dq[-1]] < temperatures[i]:
            dq.pop()
        dq.append(i)
        if i >= K - 1:
            winning_sensor = sensors[dq[0]]
            credits[winning_sensor] += 1
    result = sorted(credits.items(), key=lambda x: (-x[1], x[0]))
    print(len(result))
    for sensor_id, count in result:
        print(sensor_id, count)

if __name__ == "__main__":
    main()
