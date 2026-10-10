"""
Problem   : Deep Space Uplink Balancer
Platform  : Unstop
Link      : https://unstop.com/code/practice/661682
Difficulty: Medium
Topics    : Heap (Priority Queue), Hashing, Simulation
Date      : 2026-10-10

Approach:
    Keep a min-heap of (load, channel_id) so the least-loaded channel
    (lowest id on ties) is always at the top.
    - Assign (type 1): pop the top channel, add the request's load d,
      push it back with its updated load, and record
      request_id -> (channel, d) in a hash map.
    - Release (type 2): look up the request in the hash map, subtract its
      load from that channel, and print the channel and its new load.
      Heap entries can't be updated in place, so the heap is rebuilt from
      the current load array and heapified.

Complexity:
    Assign : O(log K)
    Release: O(K) because of the rebuild + heapify
    Total  : O(Q log K + R * K), where R is the number of releases
             (worst case O(Q * K))
    Space  : O(K + A), where A is the number of active requests
"""


# ------------------------------------------ Solution --------------------------------------------------------


import sys
import heapq

def main():
    input = sys.stdin.readline
    K, Q = map(int, input().split())
    heap = [(0, i) for i in range(1, K + 1)]
    heapq.heapify(heap)
    active = {}
    load = [0] * (K + 1)
    output = []
    for _ in range(Q):
        event = list(map(int, input().split()))
        if event[0] == 1:
            _, request_id, d = event
            current_load, channel = heapq.heappop(heap)
            load[channel] += d
            active[request_id] = (channel, d)
            heapq.heappush(heap, (load[channel], channel))
            output.append(str(channel))
        else:
            _, request_id = event
            channel, d = active.pop(request_id)
            load[channel] -= d
            output.append(f"{channel} {load[channel]}")
            heap = [
                (load[ch], ch)
                for ch in range(1, K + 1)
            ]
            heapq.heapify(heap)
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
