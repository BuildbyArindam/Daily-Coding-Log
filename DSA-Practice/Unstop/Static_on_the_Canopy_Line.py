"""
Problem   : Static on the Canopy Line
Platform  : Unstop 
Link      : https://unstop.com/code/practice/662950
Date      : 2026-10-12
Difficulty: Hard
Topics    : Binary Trie, Bit Manipulation, Hashing, Heap (Priority Queue)

Approach:
    - Keep a 20-bit binary trie of the codes of all currently registered
      animals. Each node stores a count, so RETIRE is a decrement and
      REGISTER is an increment.
    - A hash map (name -> code) gives O(1) lookup for RETIRE and PING.
    - PING: walk the trie from the top bit down, greedily taking the opposite
      bit when that subtree still has count > 0, which maximizes the XOR.
      If fewer than 2 animals are registered, the answer is -1.
    - A min-heap of size K tracks the K largest interference values seen
      across all PINGs, printed in descending order at the end
      (or "NONE" if no value was recorded).

Complexity (B = 20 bits, N = number of operations):
    Time  : O(N * B) overall; each operation is O(B) trie work plus
            O(log K) for the heap on PING.
    Space : O(N * B) trie nodes in the worst case, plus O(N) for the
            hash map and O(K) for the heap.
"""


# -------------------------------------------------- Solution -------------------------------------------------------------


import sys
import heapq
from array import array

data = sys.stdin.buffer.read().split()

if not data:
    sys.exit()
n = int(data[0])
K = int(data[1])
pos = 2
left = array('i', [-1])
right = array('i', [-1])
count = array('i', [0])
def update(code, delta):
    node = 0
    count[node] += delta
    for bit in range(19, -1, -1):
        b = (code >> bit) & 1
        if b == 0:
            nxt = left[node]
            if nxt == -1:
                nxt = len(count)
                left[node] = nxt
                left.append(-1)
                right.append(-1)
                count.append(0)
        else:
            nxt = right[node]
            if nxt == -1:
                nxt = len(count)
                right[node] = nxt
                left.append(-1)
                right.append(-1)
                count.append(0)
        node = nxt
        count[node] += delta

def max_xor(code):
    node = 0
    result = 0
    for bit in range(19, -1, -1):
        b = (code >> bit) & 1
        if b == 0:
            preferred = right[node]
            same = left[node]
        else:
            preferred = left[node]
            same = right[node]
        if preferred != -1 and count[preferred] > 0:
            result |= (1 << bit)
            node = preferred
        else:
            node = same
    return result
animals = {}
top_k = []
output = []
for _ in range(n):
    operation = data[pos]
    pos += 1
    if operation == b'REGISTER':
        name = data[pos]
        code = int(data[pos + 1])
        pos += 2
        animals[name] = code
        update(code, 1)
    elif operation == b'RETIRE':
        name = data[pos]
        pos += 1
        code = animals.pop(name)
        update(code, -1)
    elif operation == b'PING':
        name = data[pos]
        pos += 1
        code = animals[name]
        if count[0] <= 1:
            output.append("-1")
        else:
            interference = max_xor(code)
            output.append(str(interference))
            if K > 0:
                if len(top_k) < K:
                    heapq.heappush(top_k, interference)
                elif interference > top_k[0]:
                    heapq.heapreplace(top_k, interference)
if top_k:
    output.append(" ".join(map(str, sorted(top_k, reverse=True))))
else:
    output.append("NONE")

sys.stdout.write("\n".join(output) + "\n")
