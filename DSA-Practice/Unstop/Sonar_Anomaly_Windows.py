"""
Problem   : Sonar Anomaly Windows
Platform  : Unstop
Link      : https://unstop.com/code/practice/657890
Difficulty: Hard
Topics    : Trie, Persistent Data Structure, Bitwise, Greedy, Maths
Date      : 2026-09-03

Approach:
    Build a persistent binary trie over 20-bit integers, where roots[i]
    is the trie containing the prefix a[1..i]. Each insertion creates
    O(20) new nodes by path-copying from the previous root, so the
    array of nodes never mutates old versions.

    For a query (l, r, x): walk roots[r] and roots[l-1] in lockstep,
    greedily choosing the bit of x's XOR-partner that maximizes the
    result at each level, but only descend into a child if
    cnt[child_r] - cnt[child_l] > 0 (i.e. at least one element in the
    range a[l..r] actually lives under that child). This restricts
    the classic "max XOR trie" trick to an arbitrary subarray using
    the offline prefix-version subtraction trick.

Complexity:
    Time : O((N + Q) * B)   where B = 20 (bits per value)
    Space: O((N + Q) * B)   for the persistent trie nodes
"""


# ------------------------ Solution --------------------------------------


import sys
from array import array
data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
N = next(it)
a = [next(it) for _ in range(N)]
Q = next(it)
left = array('i', [0])
right = array('i', [0])
cnt = array('i', [0])
roots = array('i', [0]) * (N + 1)
for pos, value in enumerate(a, 1):
    old_root = roots[pos - 1]
    new_root = len(left)
    left.append(left[old_root])
    right.append(right[old_root])
    cnt.append(cnt[old_root] + 1)
    prev = old_root
    cur = new_root
    for bit in range(19, -1, -1):
        if (value >> bit) & 1:
            old_child = right[prev]
            new_child = len(left)
            left.append(left[old_child])
            right.append(right[old_child])
            cnt.append(cnt[old_child] + 1)
            right[cur] = new_child
            prev = old_child
            cur = new_child
        else:
            old_child = left[prev]
            new_child = len(left)
            left.append(left[old_child])
            right.append(right[old_child])
            cnt.append(cnt[old_child] + 1)
            left[cur] = new_child
            prev = old_child
            cur = new_child
    roots[pos] = new_root
answers = []
for _ in range(Q):
    l = next(it)
    r = next(it)
    x = next(it)
    node_r = roots[r]
    node_l = roots[l - 1]
    result = 0
    for bit in range(19, -1, -1):
        xbit = (x >> bit) & 1
        if xbit == 0:
            preferred_r = right[node_r]
            preferred_l = right[node_l]
            if cnt[preferred_r] - cnt[preferred_l] > 0:
                result |= (1 << bit)
                node_r = preferred_r
                node_l = preferred_l
            else:
                node_r = left[node_r]
                node_l = left[node_l]
        else:
            preferred_r = left[node_r]
            preferred_l = left[node_l]
            if cnt[preferred_r] - cnt[preferred_l] > 0:
                result |= (1 << bit)
                node_r = preferred_r
                node_l = preferred_l
            else:
                node_r = right[node_r]
                node_l = right[node_l]
    answers.append(str(result))
sys.stdout.write("\n".join(answers))
