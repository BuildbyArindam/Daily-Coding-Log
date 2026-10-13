"""
Problem   : Bugs
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/victory-over-power-4a0cb459/
Date      : 2026-10-13
Difficulty: Hard
Topics    : Heap, Binary Search, Fenwick Tree (alternative), Searching

Approach  : Maintain two heaps over all enemies inserted so far:
            - `top`  : min-heap holding the largest floor(size/3) powers
            - `rest` : max-heap (negated values) holding everything else
            The answer to a query is top[0], the smallest element of `top`,
            i.e. the floor(size/3)-th largest power. After every insert, the
            heaps are rebalanced so len(top) == size // 3. Each insert moves
            at most a constant number of elements between heaps.
            If size < 3, print "Not enough enemies".

Time      : O(N log N) overall, O(log N) per insert, O(1) per query
Space     : O(N)
"""


# ------------------------------------------------ Solution ------------------------------------------------------------


import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    N = data[0]
    idx = 1
    top = []
    rest = []
    size = 0
    result = []
    for _ in range(N):
        op = data[idx]
        idx += 1
        if op == 1:
            x = data[idx]
            idx += 1
            size += 1
            if top and x > top[0]:
                heapq.heappush(top, x)
            else:
                heapq.heappush(rest, -x)
            target = size // 3
            while len(top) > target:
                heapq.heappush(rest, -heapq.heappop(top))
            while len(top) < target:
                heapq.heappush(top, -heapq.heappop(rest))
        else:
            if size < 3:
                result.append("Not enough enemies")
            else:
                result.append(str(top[0]))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
