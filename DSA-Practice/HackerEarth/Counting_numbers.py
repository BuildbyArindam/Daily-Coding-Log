"""
Problem: Counting numbers
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/counting-2-a88e8d45/
Date: 2026-09-21
Difficulty: Hard
Topics: Searching, Binary Search, Recursion

Approach:
Build a max-Cartesian-tree over the string using a monotonic stack,
then do a DFS deletion order (root -> left -> right, reversed) that
gives the order in which characters get removed. Use a Fenwick tree
(BIT) over positions to support "find k-th remaining character"
queries after offline-sorting queries by number of deletions so far
(processed incrementally in increasing order of k).

Time complexity: O((n + m) log n)
Space complexity: O(n + m)
"""


# ----------------------------------------- Solution ------------------------------------------


import sys
input = sys.stdin.buffer.readline
s = input().strip()
n = len(s)
m = int(input())
queries = []
for i in range(m):
    k, l = map(int, input().split())
    queries.append((n - k, l, i))
left = [-1] * n
right = [-1] * n
stack = []
for i in range(n):
    last = -1
    while stack and s[stack[-1]] < s[i]:
        last = stack.pop()
    if stack:
        right[stack[-1]] = i
    if last != -1:
        left[i] = last
    stack.append(i)
root = stack[0]
tmp = []
st = [root]
while st:
    u = st.pop()
    tmp.append(u)
    if left[u] != -1:
        st.append(left[u])
    if right[u] != -1:
        st.append(right[u])
deletion_order = tmp[::-1]
bit = [0] * (n + 1)
for i in range(1, n + 1):
    bit[i] = i & -i

def add(pos, delta):
    while pos <= n:
        bit[pos] += delta
        pos += pos & -pos

def kth(k):
    idx = 0
    step = 1 << (n.bit_length() - 1)
    while step:
        nxt = idx + step
        if nxt <= n and bit[nxt] < k:
            idx = nxt
            k -= bit[nxt]
        step >>= 1
    return idx + 1
queries.sort()
answer = bytearray(m)
deleted = 0
for deletions, l, query_index in queries:
    while deleted < deletions:
        pos = deletion_order[deleted] + 1 
        add(pos, -1)
        deleted += 1
    pos = kth(l)
    answer[query_index] = s[pos - 1]
sys.stdout.write(answer.decode())
