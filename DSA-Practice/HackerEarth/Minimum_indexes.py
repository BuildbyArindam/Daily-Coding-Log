"""
Problem   : Minimum indexes
Platform  : HackerEarth (Data Structures > Stacks > Basics of Stacks)
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/yassers-conditions-6cc26a09/
Difficulty: Medium
Topics    : Data Structures, Stacks
Date      : 2026-09-28

Approach:
  For each queried index i, find the smallest j > i with A[j] > A[i] and
  digit_sum(A[j]) < digit_sum(A[i]).
  1. Precompute the digit sum of every element (max 81 for values up to 10^9).
  2. Group queries by the digit sum of A[i].
  3. Sweep digit sums d = 1..81. Before answering queries with sum d, insert
     every element with digit sum d-1 into a max segment tree, so the tree
     always holds exactly the elements with digit sum < d.
  4. Answer each query with a "first index >= i+1 whose value > A[i]" descent
     on the iterative segment tree.

Time : O(N log N + Q log N + 81)
Space: O(N + Q)
"""


# ----------------------------------------- Solution --------------------------------------------


import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    N = next(it)
    Q = next(it)
    A = [next(it) for _ in range(N)]
    def digit_sum(x):
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s
    ds = [digit_sum(x) for x in A]
    MAX_SUM = 81
    positions_by_sum = [[] for _ in range(MAX_SUM + 1)]
    for i in range(N):
        positions_by_sum[ds[i]].append(i)
    queries_by_sum = [[] for _ in range(MAX_SUM + 1)]
    for query_number in range(Q):
        i = next(it) - 1
        queries_by_sum[ds[i]].append((i, query_number))
    size = 1
    while size < N:
        size <<= 1
    tree = [-1] * (2 * size)
    def update(pos, value):
        p = pos + size
        tree[p] = value
        p >>= 1
        while p:
            left = tree[p << 1]
            right = tree[p << 1 | 1]
            new_value = left if left > right else right
            if tree[p] == new_value:
                break
            tree[p] = new_value
            p >>= 1
    def first_greater(left_index, value):
        if left_index >= N or tree[1] <= value:
            return -1
        p = left_index + size
        if tree[p] > value:
            return p - size
        while p > 1:
            if (p & 1) == 0:
                sibling = p + 1
                if tree[sibling] > value:
                    p = sibling
                    while p < size:
                        left_child = p << 1
                        if tree[left_child] > value:
                            p = left_child
                        else:
                            p = left_child | 1
                    answer = p - size
                    if answer < N:
                        return answer
                    return -1
            p >>= 1
        return -1
    answers = [-1] * Q
    for d in range(1, MAX_SUM + 1):
        for pos in positions_by_sum[d - 1]:
            update(pos, A[pos])
        for i, query_number in queries_by_sum[d]:
            j = first_greater(i + 1, A[i])
            if j == -1:
                answers[query_number] = -1
            else:
                answers[query_number] = j + 1
    sys.stdout.write("\n".join(map(str, answers)))

if __name__ == "__main__":
    solve()
