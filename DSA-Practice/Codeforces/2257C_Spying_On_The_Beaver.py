"""
Problem   : 2257C - Spying on the Beaver
Link      : https://codeforces.com/contest/2257/problem/C
Date      : 2026-08-18
Topics    : dfs and similar, dsu, graphs, trees

Approach:
  Root the tree at vertex 1. Do a single bottom-up (post-order) pass.
  For each vertex v track:
    - reach[v]: number of dams in v's subtree
    - need[v] : minimum cameras required inside v's subtree to uniquely
                identify which dam the beaver reached, GIVEN that the
                edge into v itself is not yet decided
    - zero_ok[v]: whether v's subtree can be resolved with 0 "extra"
                  cameras charged to the parent (i.e. this subtree can
                  absorb one free/unmarked path down to a single dam)
  A child c contributes a forced camera on edge (v -> c) unless c is
  allowed to stay "free" (zero_ok[c] true) - and at most one child can
  stay free per vertex, except when v itself is a dam, in which case
  every child with a reachable dam needs a camera (no free pass, since
  the dam at v itself already resolves the "beaver stopped here" case).
  Cameras placed are exactly the edges leading into 'forced' children;
  these are collected as the marked list, and need[1] is the answer.

Complexity:
  Time  : O(n) per test case (single pass over vertices + edges)
  Space : O(n) per test case (kids/reach/need/zero_ok arrays)
  Total : O(sum of n) across test cases
"""


# ----------------------- Solution --------------------------


import sys

def run():
    buf = sys.stdin.buffer.read().split()
    pos = 0
    def grab():
        nonlocal pos
        v = buf[pos]
        pos += 1
        return v
    total_cases = int(grab())
    answer_chunks = []
    for _case in range(total_cases):
        vertex_count = int(grab())
        kids = [[] for _ in range(vertex_count + 1)]
        for child_id in range(2, vertex_count + 1):
            p = int(grab())
            kids[p].append(child_id)
        m = int(grab())
        is_dam = bytearray(vertex_count + 1)
        for _k in range(m):
            a = int(grab())
            is_dam[a] = 1
        reach = [0] * (vertex_count + 1)
        need = [0] * (vertex_count + 1)
        zero_ok = bytearray(vertex_count + 1)
        marked = []
        for v in range(vertex_count, 0, -1):
            active_sum = 0
            reach_sum = 0
            zero_children = []
            for c in kids[v]:
                rc = reach[c]
                reach_sum += rc
                if rc >= 1:
                    active_sum += need[c]
                    if zero_ok[c]:
                        zero_children.append(c)
            here = is_dam[v]
            if here:
                force = zero_children
                zero_ok[v] = 1
            else:
                if zero_children:
                    force = zero_children[1:]
                    zero_ok[v] = 1
                else:
                    force = []
                    zero_ok[v] = 0
            need[v] = active_sum + len(force)
            if force:
                marked.extend(force)
            reach[v] = here + reach_sum
        k_value = need[1]
        if marked:
            answer_chunks.append(str(k_value) + ' ' + ' '.join(map(str, marked)))
        else:
            answer_chunks.append(str(k_value))
    sys.stdout.write('\n'.join(answer_chunks) + '\n')

run()
