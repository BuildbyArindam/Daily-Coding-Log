"""
Problem   : City Group
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/city-group-3/
Difficulty: Easy
Topic     : Basic Programming / Implementation

Approach:
    - Read N cities and K groups; for each group, record every city's
      group index (1..K) in a hashmap (city_to_group).
    - For each query (x, y), look up their group indices g1, g2.
    - Since groups are arranged in a circle of size K, the minimum
      distance between two groups is min(|g1 - g2|, K - |g1 - g2|).
    - Answer each query in O(1) after O(N) preprocessing.

Time Complexity : O(N + Q)   -> N for building the map, Q for answering queries
Space Complexity: O(N)       -> city_to_group hashmap
"""


# ---------------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    n = int(input_data[idx])
    k = int(input_data[idx + 1])
    idx += 2
    city_to_group = {}
    for group_idx in range(1, k + 1):
        s_i = int(input_data[idx])
        idx += 1
        for _ in range(s_i):
            city = int(input_data[idx])
            city_to_group[city] = group_idx
            idx += 1
    q = int(input_data[idx])
    idx += 1
    output = []
    for _ in range(q):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2
        g1 = city_to_group[x]
        g2 = city_to_group[y]
        diff = abs(g1 - g2)
        min_dist = min(diff, k - diff)
        output.append(str(min_dist))
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
