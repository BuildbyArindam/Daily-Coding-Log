"""
Problem: LFU Cache
Platform: Coding Ninjas - Code360
Link: https://www.naukri.com/code360/problems/lfucache_3622709?kunjiRedirection=true
Difficulty: Hard
Date Solved: 2026-08-21

Approach:
Maintain a dict mapping key -> [value, frequency, last_used_time], using a
global monotonically increasing counter as a tie-breaker timestamp. On
eviction, linearly scan the cache to find the entry with the lowest
frequency, breaking ties by the oldest timestamp, then remove it.

Time Complexity:
- get(): O(1) average (single dict lookup/update)
- put(): O(1) average when the cache isn't full; O(n) in the eviction case,
  since finding the LFU/LRU victim requires scanning all n = capacity
  entries. (Note: a true O(1) LFU needs a freq -> DLL bucket structure;
  this scan-based version trades some throughput for simplicity.)

Space Complexity: O(capacity)
"""


# ----------------------------- Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.time = 0
    def get(self, key: int) -> int:
        self.time += 1
        if key not in self.cache:
            return -1
        value, frequency, _ = self.cache[key]
        frequency += 1
        self.cache[key] = [value, frequency, self.time]
        return value
    def put(self, key: int, value: int) -> None:
        self.time += 1
        if self.capacity == 0:
            return
        if key in self.cache:
            _, frequency, _ = self.cache[key]
            frequency += 1
            self.cache[key] = [value, frequency, self.time]
            return
        if len(self.cache) == self.capacity:
            lfu_key = None
            min_frequency = float('inf')
            min_time = float('inf')
            for k, (v, freq, last_time) in self.cache.items():
                if freq < min_frequency or (
                    freq == min_frequency and last_time < min_time
                ):
                    min_frequency = freq
                    min_time = last_time
                    lfu_key = k
            del self.cache[lfu_key]
        self.cache[key] = [value, 1, self.time]

def main():
    input = stdin.readline
    T = int(input())
    for _ in range(T):
        capacity, M = map(int, input().split())
        lfu = LFUCache(capacity)
        answer = []
        for _ in range(M):
            operation = list(map(int, input().split()))
            if operation[0] == 1:
                _, key, value = operation
                lfu.put(key, value)
            else:
                _, key = operation
                answer.append(lfu.get(key))
        print(*answer)

if __name__ == "__main__":
    main()
