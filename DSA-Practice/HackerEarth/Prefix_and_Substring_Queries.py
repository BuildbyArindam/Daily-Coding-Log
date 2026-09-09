"""
Problem   : Prefix and Substring Queries
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/codemonk/3/1504681/
Difficulty: Hard
Topics    : KMP, Trees, HLD, LCA, Fenwick Tree, Offline Queries
Date      : 2026-09-09

Approach
--------
Reads the full input first (including all "append character" queries), so the
final string is known before any processing — this makes the append queries
free and lets the rest of the algorithm work on the whole string offline.

1. Build the KMP prefix-function (pi) array over the final string.
2. Build the "failure-function tree" (pi[i] -> i), where each node i
   represents the prefix of length i. A node's ancestors are exactly its
   borders.
3. Compute Euler tour (tin/tout) for subtree ranges, plus heavy-light
   decomposition (size/heavy/chain_head) to answer LCA queries in O(log M).
4. Query type 2 (x, y): LCA of two prefix-nodes via HLD chain jumping.
5. Query type 3 (p, l, r): count occurrences of prefix p as a substring of
   s[l..r]. An occurrence ending at position i exists iff i lies in the
   subtree of node p in the failure tree, so this reduces to counting nodes
   with tin in [tin[p], tout[p]] and position i in [l+p-1, r]. Answered
   offline with a Fenwick tree over positions, sweeping the Euler tour and
   using an add-at-tout / subtract-at-(tin-1) trick per query.

Complexity
----------
Time : O((M + Q) log M)   where M = final string length, Q = number of queries
       - prefix function / tree build: O(M)
       - each type-2 query (HLD LCA): O(log M)
       - each type-3 query (Fenwick range count via Euler sweep): O(log M)
Space: O(M + Q)
"""


# ------------------------- Solution ---------------------------------


import sys
from array import array

def main():
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    s = bytearray(input().strip())
    ops = []
    answers = [None] * Q
    for qi in range(Q):
        parts = input().split()
        typ = int(parts[0])
        if typ == 1:
            s.append(parts[1][0])
            ops.append((1,))
        elif typ == 2:
            x = int(parts[1])
            y = int(parts[2])
            ops.append((2, x, y))
        else:
            p = int(parts[1])
            l = int(parts[2])
            r = int(parts[3])
            ops.append((3, p, l, r))
    M = len(s)
    pi = array('i', [0]) * (M + 1)
    j = 0
    for i in range(2, M + 1):
        c = s[i - 1]
        while j > 0 and c != s[j]:
            j = pi[j]
        if c == s[j]:
            j += 1
        pi[i] = j
    size = array('i', [1]) * (M + 1)
    for i in range(M, 0, -1):
        size[pi[i]] += size[i]
    heavy = array('i', [0]) * (M + 1)
    for i in range(1, M + 1):
        p = pi[i]
        if size[i] > size[heavy[p]]:
            heavy[p] = i
    depth = array('i', [0]) * (M + 1)
    chain_head = array('i', [0]) * (M + 1)
    for i in range(1, M + 1):
        p = pi[i]
        depth[i] = depth[p] + 1
        if heavy[p] == i:
            chain_head[i] = chain_head[p]
        else:
            chain_head[i] = i
    first_child = array('i', [-1]) * (M + 1)
    next_sibling = array('i', [-1]) * (M + 1)
    for i in range(1, M + 1):
        p = pi[i]
        next_sibling[i] = first_child[p]
        first_child[p] = i
    tin = array('i', [0]) * (M + 1)
    tout = array('i', [0]) * (M + 1)
    node_at_tin = array('i', [0]) * (M + 1)
    timer = 0
    stack = [0]
    while stack:
        v = stack.pop()
        if v >= 0:
            tin[v] = timer
            node_at_tin[timer] = v
            timer += 1
            stack.append(~v)
            c = first_child[v]
            while c != -1:
                stack.append(c)
                c = next_sibling[c]
        else:
            v = ~v
            tout[v] = timer - 1
    del first_child
    del next_sibling
    del size
    del heavy
    def lca(a, b):
        while chain_head[a] != chain_head[b]:
            ha = chain_head[a]
            hb = chain_head[b]
            if depth[ha] > depth[hb]:
                a = pi[ha]
            else:
                b = pi[hb]
        return a if depth[a] < depth[b] else b
    A3 = []   
    B3 = []  
    global_id = []  
    event_head = array('i', [-1]) * (M + 1)
    event_next = array('i')
    event_query = array('i')
    event_sign = array('b')
    for qi, op in enumerate(ops):
        typ = op[0]
        if typ == 2:
            _, x, y = op
            answers[qi] = lca(x, y)
        elif typ == 3:
            _, p, l, r = op
            qid = len(A3)
            A = l + p - 1
            B = r
            A3.append(A)
            B3.append(B)
            global_id.append(qi)
            t = tout[p]
            eid = len(event_query)
            event_query.append(qid)
            event_sign.append(1)
            event_next.append(event_head[t])
            event_head[t] = eid
            t = tin[p] - 1
            eid = len(event_query)
            event_query.append(qid)
            event_sign.append(-1)
            event_next.append(event_head[t])
            event_head[t] = eid
    bit = array('i', [0]) * (M + 1)
    def bit_add(pos):
        while pos <= M:
            bit[pos] += 1
            pos += pos & -pos
    def bit_sum(pos):
        total = 0
        while pos > 0:
            total += bit[pos]
            pos -= pos & -pos
        return total
    for t in range(M + 1):
        if t > 0:
            e = node_at_tin[t]
            bit_add(e)
        event = event_head[t]
        while event != -1:
            qid = event_query[event]
            cnt = bit_sum(B3[qid]) - bit_sum(A3[qid] - 1)
            qi = global_id[qid]
            if answers[qi] is None:
                answers[qi] = 0
            answers[qi] += event_sign[event] * cnt
            event = event_next[event]
    out = []
    for value in answers:
        if value is not None:
            out.append(str(value))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
