"""
Problem   : Utkarsh and Distributing Books
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/utkarsh-and-distributing-books-february-easy/
Difficulty: Easy
Topic     : Math
Date      : 2026-08-25

Approach:
    Utkarsh always wants to minimize the maximum number of extra books
    any single friend gets removed from him, so his optimal k is
    (minimum pile size - 1) — the largest k such that every pile still
    has at least 1 book left after removing k from each.
    Saharsh instead wants to maximize total books collected, so his
    optimal k is just the sum of (books[i] - 1) across all friends,
    since he doesn't care about leaving friends with 0 books.

Time complexity : O(n) per test case (single pass to compute min and sum)
Space complexity: O(n) per test case (storing the book counts array)
"""


# ----------------------- Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        b = [int(x) for x in input_data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        utkarsh_k = min(b) - 1
        saharsh_k = sum(x - 1 for x in b)
        out.append(f"{utkarsh_k} {saharsh_k}")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
