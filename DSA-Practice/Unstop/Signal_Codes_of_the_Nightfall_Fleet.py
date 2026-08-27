"""
Problem   : Signal Codes of the Nightfall Fleet
Platform  : Unstop
Link      : https://unstop.com/code/practice/657550
Difficulty: Hard
Date      : 2026-08-27
Topics    : Persistent Trie, Bit XOR, Offline/Version Queries,
            Greedy Bit Construction, Range-Constrained Maximum XOR

Approach:
    Build a persistent binary trie over 0..MAX_BIT bits, one version
    per prefix of the array (root[i] = trie after inserting a[0..i-1]).
    For a query (l, r, x), take the trie snapshot at r and subtract
    the snapshot at l-1 (via cnt differences at each node) to restrict
    the search to the subarray [l, r]. Walk the tries in parallel,
    greedily choosing the bit opposite to x's bit at each level
    whenever a node with cnt_r - cnt_l > 0 exists on that branch,
    which maximizes a[i] ^ x under the persistence trick.

Complexity:
    Build : O(n * B)  time and space   (B = MAX_BIT + 1 = 31)
    Query : O(B) time per query, O(1) extra space
    Total : O((n + q) * B) time, O(n * B) space
"""


# ---------------------------- Solution -------------------------------


import sys
from array import array
input = sys.stdin.buffer.readline
n = int(input())
a = list(map(int, input().split()))
MAX_BIT = 30
left = array('i', [0])
right = array('i', [0])
cnt = array('i', [0])
root = array('i', [0]) * (n + 1)
for i, value in enumerate(a, 1):
    old = root[i - 1]
    new_root = len(cnt)
    left.append(left[old])
    right.append(right[old])
    cnt.append(cnt[old] + 1)
    root[i] = new_root
    prev = old
    cur = new_root
    for bit in range(MAX_BIT, -1, -1):
        b = (value >> bit) & 1
        if b == 0:
            old_child = left[prev]
            if old_child == 0:
                new_child = len(cnt)
                left.append(0)
                right.append(0)
                cnt.append(1)
            else:
                new_child = len(cnt)
                left.append(left[old_child])
                right.append(right[old_child])
                cnt.append(cnt[old_child] + 1)
            left[cur] = new_child
            prev = old_child
            cur = new_child
        else:
            old_child = right[prev]
            if old_child == 0:
                new_child = len(cnt)
                left.append(0)
                right.append(0)
                cnt.append(1)
            else:
                new_child = len(cnt)
                left.append(left[old_child])
                right.append(right[old_child])
                cnt.append(cnt[old_child] + 1)
            right[cur] = new_child
            prev = old_child
            cur = new_child

def max_xor(l, r, x):
    """
    Find max(a[i] ^ x) for l <= i <= r.

    Compare the trie for prefix r against the trie for prefix l-1.
    At every bit, prefer the branch opposite to x's bit, provided that
    branch contains at least one element in [l, r].
    """
    nr = root[r]
    nl = root[l - 1]
    ans = 0
    for bit in range(MAX_BIT, -1, -1):
        xb = (x >> bit) & 1
        if xb == 0:
            want_r = right[nr]
            want_l = right[nl]
            if cnt[want_r] - cnt[want_l] > 0:
                ans |= 1 << bit
                nr = want_r
                nl = want_l
            else:
                nr = left[nr]
                nl = left[nl]
        else:
            want_r = left[nr]
            want_l = left[nl]
            if cnt[want_r] - cnt[want_l] > 0:
                ans |= 1 << bit
                nr = want_r
                nl = want_l
            else:
                nr = right[nr]
                nl = right[nl]
    return ans
q = int(input())
out = []
for _ in range(q):
    l, r, x = map(int, input().split())
    out.append(str(max_xor(l, r, x)))
sys.stdout.write("\n".join(out))
