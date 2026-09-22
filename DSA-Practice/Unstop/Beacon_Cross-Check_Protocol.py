"""
Problem   : Beacon Cross-Check Protocol
Platform  : Unstop
Link      : https://unstop.com/code/practice/660867
Difficulty: Hard
Topics    : Array, Math, Segment Tree (solved via Binary Trie)
Date      : 2026-09-22

Approach:
    - Maintain a binary trie (20-bit, since codes fit in ~2^20) over the
      "code" values of all currently active beacon stations. Each trie
      node stores a live count so a station can be logically erased on OFF
      without rebuilding the trie.
    - ON station code   -> insert code into trie, mark station active,
                            push station id into a min-heap keyed by code
                            (for tie-breaking on smallest station id).
    - OFF station        -> erase that station's code from the trie,
                            remove from active map (heap entry becomes
                            stale and is lazily discarded later).
    - QUERY x             -> walk the trie greedily choosing the opposite
                            bit at each level when a live child exists,
                            to maximize x XOR code. Recover the matching
                            code as x XOR max_xor, then pop the smallest
                            active station with that code from its heap
                            (skipping stale/inactive entries lazily).

Complexity:
    - Insert / erase / query: O(20) per operation (bit length of codes).
    - get_smallest_station: amortized O(log M) per call due to lazy
      deletion from the heap.
    - Overall: O(M log M) time, O(M * 20) space for trie nodes.
"""


# -------------------------------------- Solution ----------------------------------------------


import sys
import heapq
from array import array
data = sys.stdin.buffer.read().split()
idx = 0
M = int(data[idx])
idx += 1
left = array('i', [-1])
right = array('i', [-1])
count = array('i', [0])
def new_node():
    left.append(-1)
    right.append(-1)
    count.append(0)
    return len(count) - 1
def insert(x):
    node = 0
    count[node] += 1
    for bit in range(19, -1, -1):
        b = (x >> bit) & 1
        if b == 0:
            nxt = left[node]
            if nxt == -1:
                nxt = new_node()
                left[node] = nxt
        else:
            nxt = right[node]
            if nxt == -1:
                nxt = new_node()
                right[node] = nxt
        node = nxt
        count[node] += 1
def erase(x):
    node = 0
    count[node] -= 1
    for bit in range(19, -1, -1):
        b = (x >> bit) & 1
        if b == 0:
            node = left[node]
        else:
            node = right[node]
        count[node] -= 1
def maximum_xor(x):
    node = 0
    value = 0
    for bit in range(19, -1, -1):
        b = (x >> bit) & 1
        if b == 0:
            nxt = right[node]
            if nxt != -1 and count[nxt] > 0:
                value |= (1 << bit)
                node = nxt
            else:
                node = left[node]
        else:
            nxt = left[node]
            if nxt != -1 and count[nxt] > 0:
                value |= (1 << bit)
                node = nxt
            else:
                node = right[node]
    return value, node
active = {}
stations = {}
def get_smallest_station(code):
    heap = stations[code]
    while heap:
        station = heap[0]
        if station in active and active[station] == code:
            return station
        heapq.heappop(heap)
    return -1
answer = []
for _ in range(M):
    operation = data[idx]
    idx += 1
    if operation == b'ON':
        station = int(data[idx])
        code = int(data[idx + 1])
        idx += 2
        active[station] = code
        insert(code)
        if code not in stations:
            stations[code] = []
        heapq.heappush(stations[code], station)
    elif operation == b'OFF':
        station = int(data[idx])
        idx += 1
        code = active.pop(station)
        erase(code)
    else:
        x = int(data[idx])
        idx += 1
        max_xor, node = maximum_xor(x)
        code = x ^ max_xor
        station = get_smallest_station(code)
        answer.append(str(max_xor) + " " + str(station))
sys.stdout.write("\n".join(answer))
