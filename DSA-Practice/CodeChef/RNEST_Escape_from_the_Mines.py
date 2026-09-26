"""
Problem   : Dyslexic Gollum (RNEST)
Platform  : CodeChef (ICPC Practice Course — ICPCTR07)
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/RNEST
Date      : 2026-09-26
Difficulty: Hard
Topics    : Sweep Line, Offline Processing, Treap (Randomized BST),
            Balanced BST, Interval Stack, Data Structures

Approach:
    Sweep rectangles left-to-right by x1 (start). Maintain a treap keyed on
    y1, where each node also stores y2 and is augmented with `top`
    (max hi in its subtree) to support "find rightmost interval whose
    y-range covers a query point" in O(log n).

    For each rectangle (x1, y1, x2, y2), in x1 order:
      1. Evict all "active" rectangles whose x2 <= current x1 (they've
         closed before this one opens) — tracked via a min-heap on x2.
      2. Query the treap for the rightmost still-open interval [ylo, yhi)
         that covers y1 -> that's this rectangle's immediate parent
         (the tightest enclosing rectangle still active).
      3. Insert this rectangle's y-interval into the treap, keyed by y1,
         and push (x2, y1) onto the min-heap for future eviction.

    The `containing_room` split/rejoin + `rightmost_covering` walk is the
    core trick: split the treap at y1, then walk down the right side
    preferring the rightmost subtree whose max-hi still exceeds y1,
    finally checking whether the found node's own hi covers y1.

Complexity:
    Time : O(n log n) expected (treap split/join/insert/erase are all
           O(log n) expected height; heap ops are O(log n)).
    Space: O(n) for the treap nodes and the eviction heap.
"""


# ------------------------------------ Solution --------------------------------------------


import sys
import heapq
import random

class BoxNode:
    __slots__ = ("lo", "hi", "num", "priority", "left", "right", "top")
    def __init__(self, lo, hi, num, priority):
        self.lo = lo
        self.hi = hi
        self.num = num
        self.priority = priority
        self.left = None
        self.right = None
        self.top = hi

def refresh(t):
    if t is None:
        return
    best = t.hi
    if t.left is not None and t.left.top > best:
        best = t.left.top
    if t.right is not None and t.right.top > best:
        best = t.right.top
    t.top = best

def cut(t, key):
    if t is None:
        return None, None
    if t.lo <= key:
        a, b = cut(t.right, key)
        t.right = a
        refresh(t)
        return t, b
    a, b = cut(t.left, key)
    t.left = b
    refresh(t)
    return a, t

def join(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.priority > b.priority:
        a.right = join(a.right, b)
        refresh(a)
        return a
    b.left = join(a, b.left)
    refresh(b)
    return b

def put(root, item):
    if root is None:
        return item
    if item.priority > root.priority:
        item.left, item.right = cut(root, item.lo)
        refresh(item)
        return item
    if item.lo < root.lo:
        root.left = put(root.left, item)
    else:
        root.right = put(root.right, item)
    refresh(root)
    return root
    
def erase(root, key):
    if root is None:
        return None
    if key == root.lo:
        return join(root.left, root.right)
    if key < root.lo:
        root.left = erase(root.left, key)
    else:
        root.right = erase(root.right, key)
    refresh(root)
    return root

def rightmost_covering(t, y):
    if t is None:
        return None
    if t.right is not None and t.right.top > y:
        return rightmost_covering(t.right, y)
    if t.hi > y:
        return t
    return rightmost_covering(t.left, y)

def containing_room(root, y):
    left_part, right_part = cut(root, y)
    found = rightmost_covering(left_part, y)
    root = join(left_part, right_part)
    if found is None:
        return root, -1
    return root, found.num

def solve(rectangles):
    n = len(rectangles)
    order = list(range(n))
    order.sort(key=lambda idx: rectangles[idx][0])
    ending = []
    root = None
    answer = [-1] * n
    rng = random.Random(712367821)
    for idx in order:
        x1, y1, x2, y2 = rectangles[idx]
        # cannot contain the new room.
        while ending and ending[0][0] <= x1:
            _, old_y1 = heapq.heappop(ending)
            root = erase(root, old_y1)
        root, parent = containing_room(root, y1)
        answer[idx] = parent
        node = BoxNode(
            y1,
            y2,
            idx,
            rng.getrandbits(64)
        )
        root = put(root, node)
        heapq.heappush(ending, (x2, y1))
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    rectangles = []
    pos = 1
    for _ in range(n):
        x1, y1, x2, y2 = data[pos:pos + 4]
        pos += 4
        rectangles.append((x1, y1, x2, y2))
    result = solve(rectangles)
    sys.stdout.write("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
