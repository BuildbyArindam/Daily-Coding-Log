"""
Problem   : Traffic Lights
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/traffic-lights_1467065?kunjiRedirection=true
Difficulty: Medium
Topics    : Binary Search, Max-Heap (Lazy Deletion), Hashing, Ordered Set Simulation
Date      : 2026-09-02

Approach:
  Maintain `lights` as a sorted list of installed light positions (starts
  with [0, x]). For each new light position p, binary-search its insertion
  index, compute the gap it splits (old_gap = right - left), decrement that
  gap's count in a Counter, and add the two new sub-gaps (left_gap, right_gap)
  with incremented counts. Push both new gaps onto a max-heap (negated for
  min-heap-as-max-heap). Lazily pop heap entries whose count has dropped to
  zero before reading the top, so the top always reflects a currently-valid
  max gap. Append the current max gap to the answer after each insertion.

Time Complexity : O(n^2) overall — bisect_left is O(log n) but list.insert
                  is O(n) per insertion (shifting elements), which dominates.
                  The heap/Counter bookkeeping is O(log n) amortized per op.
                  (Note: an order-statistics/balanced-BST structure would
                  bring this down to O(n log n) if list.insert becomes the
                  bottleneck on large inputs.)
Space Complexity : O(n) for lights, gap_count, max_heap, and ans.
"""


# ------------------------ Solution --------------------------------


def trafficLights(n, x, pos):
    import bisect
    import heapq
    from collections import Counter
    lights = [0, x]
    max_heap = [-(x)]
    gap_count = Counter({x: 1})
    ans = []
    for p in pos:
        idx = bisect.bisect_left(lights, p)
        left = lights[idx - 1]
        right = lights[idx]
        old_gap = right - left
        gap_count[old_gap] -= 1
        left_gap = p - left
        right_gap = right - p
        gap_count[left_gap] += 1
        gap_count[right_gap] += 1
        heapq.heappush(max_heap, -left_gap)
        heapq.heappush(max_heap, -right_gap)
        lights.insert(idx, p)
        while max_heap and gap_count[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        ans.append(-max_heap[0])
    return ans
