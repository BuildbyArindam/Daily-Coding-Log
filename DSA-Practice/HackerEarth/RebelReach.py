"""
Problem: RebelReach
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/rebelreach-e1a2d3d1/
Date solved: 2026-09-25
Difficulty: Hard
Topics: Binary Search, Trees, Math, Algorithms

Approach:
    - Root the tree at node 1 via iterative DFS, computing each node's
      parent (ancestor_of) and prefix sum of garrison strength from the
      root (prefix_sum).
    - Build a binary-lifting table (hop[lvl][node]) over ancestors so any
      ancestor 2^lvl steps up can be found in O(1).
    - For each query, walk up from start_town using the largest jumps
      first (like binary search on the ancestor chain): take a jump only
      if the cumulative garrison cost along it is less than the remaining
      mob_size, greedily climbing as high as the budget allows.

Complexity:
    Time:  O((N + Q) log N)   — O(N log N) to build binary lifting table,
                                 O(log N) per query to walk it.
    Space: O(N log N)         — dominated by the hop[][] lifting table.
"""


# ------------------------------------------- Solution ------------------------------------------------


import sys
from array import array

def crack_kingdom():
    raw = sys.stdin.buffer.read().split()
    cursor = iter(raw)
    pull = cursor.__next__
    out_chunks = []
    case_count = int(pull())
    for _case in range(case_count):
        town_total = int(pull())
        edge_total = town_total - 1
        eu = array('i', bytes(4 * edge_total))
        ev = array('i', bytes(4 * edge_total))
        deg = array('i', bytes(4 * (town_total + 2)))
        for i in range(edge_total):
            a = int(pull())
            b = int(pull())
            eu[i] = a
            ev[i] = b
            deg[a] += 1
            deg[b] += 1
        offset = array('i', bytes(4 * (town_total + 2)))
        running = 0
        for town in range(1, town_total + 1):
            offset[town] = running
            running += deg[town]
        offset[town_total + 1] = running
        deg = None
        fill_ptr = array('i', offset)
        flat_nb = array('i', bytes(4 * (2 * edge_total)))
        for i in range(edge_total):
            a = eu[i]
            b = ev[i]
            flat_nb[fill_ptr[a]] = b
            fill_ptr[a] += 1
            flat_nb[fill_ptr[b]] = a
            fill_ptr[b] += 1
        eu = ev = fill_ptr = None
        garrison_strength = array('q', bytes(8 * (town_total + 1)))
        for town in range(1, town_total + 1):
            garrison_strength[town] = int(pull())
        ancestor_of = array('i', bytes(4 * (town_total + 1)))
        prefix_sum = array('q', bytes(8 * (town_total + 1)))
        seen = bytearray(town_total + 1)
        seen[1] = 1
        prefix_sum[1] = garrison_strength[1]
        dfs_stack = array('i', [1])
        while dfs_stack:
            here = dfs_stack.pop()
            lo = offset[here]
            hi = offset[here + 1]
            here_ps = prefix_sum[here]
            for pos in range(lo, hi):
                nb = flat_nb[pos]
                if not seen[nb]:
                    seen[nb] = 1
                    ancestor_of[nb] = here
                    prefix_sum[nb] = here_ps + garrison_strength[nb]
                    dfs_stack.append(nb)
        seen = None
        flat_nb = None
        offset = None
        top_rung = 1
        while (1 << top_rung) < town_total:
            top_rung += 1
        top_rung += 1
        hop = [ancestor_of] 
        for lvl in range(1, top_rung):
            prev = hop[lvl - 1]
            cur_level = array('i', bytes(4 * (town_total + 1)))
            for town in range(1, town_total + 1):
                mid = prev[town]
                if mid:
                    cur_level[town] = prev[mid]
            hop.append(cur_level)
        query_total = int(pull())
        for _q in range(query_total):
            start_town = int(pull())
            mob_size = int(pull())
            here = start_town
            for lvl in range(top_rung - 1, -1, -1):
                jump_to = hop[lvl][here]
                if jump_to:
                    cost = prefix_sum[here] - prefix_sum[jump_to]
                    if cost < mob_size:
                        mob_size -= cost
                        here = jump_to
            out_chunks.append(str(here))
        hop = None
        prefix_sum = None
        garrison_strength = None
        ancestor_of = None
    sys.stdout.write('\n'.join(out_chunks) + '\n')

if __name__ == '__main__':
    crack_kingdom()
