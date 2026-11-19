"""
Problem   : Audio Guide Allocation Log
Platform  : Unstop 
Link      : https://unstop.com/code/practice/672666
Date      : 2026-11-19
Difficulty: Easy
Topics    : Min Heap, PriorityQueue, Simulation, Greedy

Approach:
    Simulate guests in arrival order using two min-heaps.
      - ready_pool: IDs of devices available now (smallest ID first).
      - cooling   : (available_time, device_id) for devices in cooldown,
                    where available_time = arrive + stay + cool.
    For each guest, move every device whose cooldown has ended
    (available_time <= arrive) from `cooling` to `ready_pool`. Then assign
    the smallest ready ID, or create a new device with the next ID if none
    is ready. Push the device into `cooling` with its new available_time.
    Finally, print each guest's device ID and the total devices used.

Complexity:
    Time  : O(N log N), each guest causes O(1) amortized heap push/pops
    Space : O(N), heaps plus the result list
"""


# ------------------------------------------------ Solution -----------------------------------------------------


import sys
from heapq import heappush as hpush, heappop as hpop

def solve():
    raw = sys.stdin.buffer.read().split()
    total_guests = int(raw[0])
    cool = int(raw[1])
    ready_pool = []     
    cooling = []         
    highest = 0          
    result = [0] * total_guests
    pos = 2
    for idx in range(total_guests):
        arrive = int(raw[pos])
        stay = int(raw[pos + 1])
        pos += 2
        while cooling and cooling[0][0] <= arrive:
            _, dev = hpop(cooling)
            hpush(ready_pool, dev)
        if ready_pool:
            chosen = hpop(ready_pool)
        else:
            highest += 1
            chosen = highest
        result[idx] = chosen
        hpush(cooling, (arrive + stay + cool, chosen))
    sys.stdout.write(" ".join(map(str, result)) + "\n" + str(highest) + "\n")

solve()
