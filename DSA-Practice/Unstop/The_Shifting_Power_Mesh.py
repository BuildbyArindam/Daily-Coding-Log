"""
Problem   : The Shifting Power Mesh
Platform  : Unstop 
Link      : https://unstop.com/code/practice/662952
Date      : 2026-10-17
Difficulty: Hard
Topics    : DSU, Leftist (Meldable) Heap, Lazy Deletion, Dynamic Connectivity

Approach
--------
Maintain components with a DSU. Each component root owns a leftist heap of
activation records, keyed by (-capacity, station, version), so the top is the
highest-capacity active station, with ties going to the smallest station id.
  - LINK  : union by size, then meld the two component heaps.
  - ON    : bump the station's version, push a new record into its component's heap.
  - OFF   : mark inactive (O(1)). The stale record is removed lazily.
  - QUERY : pop the top of the component heap until it is active and its
            version matches the station's current version; answer with that
            station, or "-1 -1" if the heap empties.

Complexity
----------
Time  : O((n + m) log m) amortized. Meld is O(log m), DSU is near O(α(n)),
        and each record is popped at most once.
Space : O(n + m), for the DSU arrays plus one heap node per ON operation.
"""


# ------------------------------------------- Solution -----------------------------------------------------


import sys

sys.setrecursionlimit(1000000)
input_data = sys.stdin.buffer.read().split()

if not input_data:
    sys.exit()

idx = 0

n = int(input_data[idx])
idx += 1

capacity = [0] + list(map(int, input_data[idx:idx + n]))
idx += n

m = int(input_data[idx])
idx += 1

parent = list(range(n + 1))
size = [1] * (n + 1)

active = [False] * (n + 1)
version = [0] * (n + 1)

left_child = [0]
right_child = [0]
npl = [0]
keys = [None]
heap_station = [0]
heap_version = [0]
heap_root = [0] * (n + 1)


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def meld(x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    if keys[x] > keys[y]:
        x, y = y, x

    right_child[x] = meld(right_child[x], y)

    if npl[left_child[x]] < npl[right_child[x]]:
        left_child[x], right_child[x] = (
            right_child[x], left_child[x]
        )

    npl[x] = npl[right_child[x]] + 1
    return x


def add_activation(s):
    keys.append((-capacity[s], s, version[s]))
    heap_station.append(s)
    heap_version.append(version[s])
    left_child.append(0)
    right_child.append(0)
    npl.append(1)

    node = len(keys) - 1
    root = find(s)
    heap_root[root] = meld(heap_root[root], node)


def link(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]

    heap_root[ra] = meld(heap_root[ra], heap_root[rb])
    heap_root[rb] = 0


def query(s):
    root = find(s)
    h = heap_root[root]
    while h != 0:
        station = heap_station[h]

        if (
            active[station]
            and heap_version[h] == version[station]
        ):
            break

        heap_root[root] = meld(left_child[h], right_child[h])
        h = heap_root[root]

    if h == 0:
        return "-1 -1"

    station = heap_station[h]
    return f"{capacity[station]} {station}"


answers = []

for _ in range(m):
    op = input_data[idx]
    idx += 1

    if op == b"LINK":
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        link(a, b)

    elif op == b"ON":
        s = int(input_data[idx])
        idx += 1

        active[s] = True
        version[s] += 1
        add_activation(s)

    elif op == b"OFF":
        s = int(input_data[idx])
        idx += 1

        active[s] = False

    elif op == b"QUERY":
        s = int(input_data[idx])
        idx += 1

        answers.append(query(s))

sys.stdout.write("\n".join(answers))
if answers:
    sys.stdout.write("\n")
