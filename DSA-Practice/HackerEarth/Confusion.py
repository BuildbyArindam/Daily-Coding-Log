"""
Problem   : Confusion
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/confusion-1/
Date      : 2026-08-24
Difficulty: Easy
Topic     : Implementation / Arrays (Suffix Distinct-Count)

Approach:
    For each query index l, count the number of distinct elements in a[l-1:].
    Precompute this for every starting index in one right-to-left pass using
    a running hash set — ans[i] = size of the set of distinct values in a[i:].
    Each query is then answered in O(1).

Complexity:
    Time  : O(n + q)  -- one pass to build ans[], O(1) per query
    Space : O(n)       -- 'seen' set (up to n distinct values) + ans array
"""


# --------------------------- Solution ---------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    ptr = 2
    a = [int(x) for x in input_data[ptr:ptr + n]]
    ptr += n
    ans = [0] * n
    seen = set()
    for i in range(n - 1, -1, -1):
        seen.add(a[i])
        ans[i] = len(seen)
    out = []
    for _ in range(q):
        l = int(input_data[ptr])
        ptr += 1
        out.append(str(ans[l - 1]))
    print('\n'.join(out))

if __name__ == "__main__":
    solve()
