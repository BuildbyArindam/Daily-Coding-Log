"""
Problem   : Districts of Meridian City
Platform  : Unstop
Link      : https://unstop.com/code/practice/661273
Difficulty: Medium
Date      : 2026-10-01
Topics    : DSU, Hashing, Graph, Union Find, Component Queries

Approach:
    - Map each district code to an index with a hash map.
    - Use DSU (path compression + union by size) to track linked districts.
    - Keep one lazy-deletion max-heap per component root, storing
      (-rating, index, version).
    - BOOST: bump the district's rating and version, push a fresh entry.
    - LINK: union the components and merge heaps small-to-large.
    - QUERY: pop stale entries (version/rating mismatch) from the root's
      heap, then read the top as the component's max rating.

Complexity:
    Time  : O((N + Q) log^2 N) worst case, from small-to-large heap merging.
            Each stale entry is popped at most once overall.
    Space : O(N + Q), one heap entry per district plus one per BOOST.
"""


# --------------------------------------- Solution ---------------------------------------------------


def process_events(n, district_data, q, events):
    import heapq
    parent = list(range(n))
    size = [1] * n
    rating = [0] * n
    version = [0] * n
    district_id = {}
    heaps = [[] for _ in range(n)]
    for i, (code, initial_rating) in enumerate(district_data):
        district_id[code] = i
        rating[i] = initial_rating
        heaps[i].append((-initial_rating, i, 0))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return ra
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        if len(heaps[ra]) < len(heaps[rb]):
            heaps[ra], heaps[rb] = heaps[rb], heaps[ra]
        large_heap = heaps[ra]
        small_heap = heaps[rb]
        for entry in small_heap:
            heapq.heappush(large_heap, entry)
        heaps[rb] = []
        return ra
    results = []
    for event in events:
        parts = event.split()
        operation = parts[0]
        if operation == "LINK":
            x = district_id[parts[1]]
            y = district_id[parts[2]]
            union(x, y)
        elif operation == "BOOST":
            x = district_id[parts[1]]
            v = int(parts[2])
            rating[x] += v
            version[x] += 1
            root = find(x)
            heapq.heappush(
                heaps[root],
                (-rating[x], x, version[x])
            )
        else: 
            x = district_id[parts[1]]
            root = find(x)
            heap = heaps[root]
            while heap:
                neg_value, idx, ver = heap[0]
                if ver == version[idx] and -neg_value == rating[idx]:
                    break
                heapq.heappop(heap)
            results.append(-heap[0][0])
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    n = int(data[0])
    district_data = []
    for i in range(1, n + 1):
        district_code, initial_rating = data[i].split()
        district_data.append((district_code, int(initial_rating)))
    q = int(data[n + 1]) 
    events = data[n + 2:n + 2 + q]  
    results = process_events(n, district_data, q, events)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
