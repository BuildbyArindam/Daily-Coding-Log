"""
Problem   : Cells in a matrix
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/easy-23-6031def9/
Difficulty: Easy
Topics    : Algorithms, Data Structures, Hash Tables, Math
Date      : 2026-09-30

Approach:
    Marking cell (i, j) covers row i and column j. A cell stays empty only if
    neither its row nor its column has been marked, so after each task the
    empty count is (N - marked_rows) * (N - marked_cols). Two hash sets track
    the distinct marked rows and columns, so each task is handled in O(1).

Complexity:
    Time  : O(K), one O(1) set update and product per task
    Space : O(K), for the two sets (at most min(N, K) entries each) plus the output
"""


# ------------------------------------ Solution -------------------------------------------


def cells_sol(N, K, task):
    rows = set()
    cols = set()
    out = []
    for i, j in task:
        rows.add(i)
        cols.add(j)
        empty_cells = (N - len(rows)) * (N - len(cols))
        out.append(empty_cells)
    return out

N, K = map(int, input().split())
task = []
for _ in range(K):
    i, j = map(int, input().split())
    X = i, j
    task.append(X)

out_ = cells_sol(N, K, task)
for elements in out_:
    print(elements, end=' ')
print()
