"""
Problem   : Number of Arrays (Invert It)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/invert-it-b06fd53a/
Difficulty: Easy
Topic     : Basic Programming, Basics of Implementation, Implementation
Date      : 2026-08-19

Approach:
For each test case, based on value of k, compute a summary statistic s
over the array:
    k == 1 -> s = max(arr)
    k == 2 -> s = min(first element, last element)
    else   -> s = min(arr)
Compare s against threshold q. If s < q, output s; otherwise output "NO".

Time Complexity : O(n) per test case  (single pass to find max/min)
Space Complexity: O(n) per test case  (storing the array), O(1) extra
"""


# ----------------------- Solution -------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        q = int(data[idx + 2])
        idx += 3
        arr = [int(x) for x in data[idx:idx + n]]
        idx += n
        if k == 1:
            s = max(arr)
        elif k == 2:
            s = min(arr[0], arr[-1])
        else:
            s = min(arr)
        if s < q:
            results.append(str(s))
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == '__main__':
    solve()
