"""
Problem   : Benny and Balls
Platform  : Unstop
Link      : https://unstop.com/code/practice/657215
Difficulty: Hard
Date      : 2026-08-24
Topics    : Trie, Persistent Trie, Bit Manipulation, XOR, Range Query, Binary Trie

Approach:
  Build a persistent binary trie (max-XOR trie) over MAX_BIT+1 = 31 bits,
  inserting prefix values one at a time so version `roots[i]` represents the
  trie containing a[1..i]. Each insertion only allocates new nodes along the
  root-to-leaf path (path copying), sharing the rest of the structure with
  the previous version — O(MAX_BIT) new nodes per insert.

  For a query (l, r, x): walk roots[r] and roots[l-1] together, bit by bit
  from MSB to LSB, always trying to move into the child that maximizes the
  XOR with x. If the child counts differ between the two versions (rr != rl),
  that subtree contains elements exclusive to [l, r], so descend there and
  set that bit in the answer; otherwise the two versions overlap completely
  on that branch, so move into the "matching" child on both sides without
  setting the bit.

Time complexity : O((N + Q) * MAX_BIT)  ~ O(N log(max_value))
Space complexity : O(N * MAX_BIT) for trie nodes (persistent, path-copied)
"""


# ---------------------------- Solution ------------------------------


import sys
from array import array
input = sys.stdin.buffer.readline
MAX_BIT = 30
N = int(input())
a = list(map(int, input().split()))
left = array('I', [0])
right = array('I', [0])
roots = array('I', [0]) * (N + 1)
for i, value in enumerate(a, 1):
    old_root = roots[i - 1]
    new_root = len(left)
    left.append(left[old_root])
    right.append(right[old_root])
    roots[i] = new_root
    old_node = old_root
    new_node = new_root
    for bit in range(MAX_BIT, -1, -1):
        if (value >> bit) & 1:
            old_child = right[old_node]
        else:
            old_child = left[old_node]
        new_child = len(left)
        left.append(left[old_child])
        right.append(right[old_child])
        if (value >> bit) & 1:
            right[new_node] = new_child
        else:
            left[new_node] = new_child
        old_node = old_child
        new_node = new_child
del a
Q = int(input())
out = []
for _ in range(Q):
    l, r, x = map(int, input().split())
    root_r = roots[r]
    root_l = roots[l - 1]
    ans = 0
    for bit in range(MAX_BIT, -1, -1):
        xb = (x >> bit) & 1
        if xb == 0:
            rr = right[root_r]
            rl = right[root_l]
            if rr != rl:
                ans |= (1 << bit)
                root_r = rr
                root_l = rl
            else:
                root_r = left[root_r]
                root_l = left[root_l]
        else:
            rr = left[root_r]
            rl = left[root_l]
            if rr != rl:
                ans |= (1 << bit)
                root_r = rr
                root_l = rl
            else:
                root_r = right[root_r]
                root_l = right[root_l]
    out.append(str(ans))

sys.stdout.write("\n".join(out))
