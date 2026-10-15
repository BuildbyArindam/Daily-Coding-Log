"""
Problem   : Shelf Popularity Watch
Platform  : Unstop
Link      : https://unstop.com/code/practice/662454
Date      : 2026-10-15
Difficulty: Medium
Topics    : Fenwick Tree, Coordinate Compression, Binary Search, Hashing

Approach:
    Process all events offline. Collect every score that can be inserted,
    then coordinate-compress them to ranks 1..n. Keep a Fenwick Tree (BIT)
    over those ranks that counts active books per score, plus a hash map
    {book_id: score} so a removal knows which rank to decrement.
      - Type 1: store the book's score and BIT +1 at its rank.
      - Type 2: pop the book's score from the map and BIT -1 at its rank.
      - Type 3: bisect_left finds how many compressed scores are below the
        threshold, and a BIT prefix sum gives the number of active books
        with a score strictly less than it.

Complexity:
    Time : O(M log M)   (sorting plus O(log n) per BIT operation)
    Space: O(M)         (events, compressed scores, BIT, hash map)
"""


# ---------------------------------------------- Solution --------------------------------------------------------


import sys
from bisect import bisect_left

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    m = data[0]
    events = []
    scores = []
    p = 1
    for _ in range(m):
        op = data[p]
        p += 1
        if op == 1:
            book_id, score = data[p], data[p + 1]
            p += 2
            events.append((1, book_id, score))
            scores.append(score)
        elif op == 2:
            book_id = data[p]
            p += 1
            events.append((2, book_id, 0))
        else:
            threshold = data[p]
            p += 1
            events.append((3, threshold, 0))
    scores = sorted(set(scores))
    ranks = {score: i + 1 for i, score in enumerate(scores)}
    n = len(scores)
    bit = [0] * (n + 1)
    active = {}
    answers = []

    def update(i, delta):
        while i <= n:
            bit[i] += delta
            i += i & -i

    def prefix_sum(i):
        total = 0
        while i > 0:
            total += bit[i]
            i -= i & -i
        return total
    for op, x, y in events:
        if op == 1:
            active[x] = y
            update(ranks[y], 1)
        elif op == 2:
            score = active.pop(x)
            update(ranks[score], -1)
        else:
            idx = bisect_left(scores, x)
            answers.append(str(prefix_sum(idx)))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
