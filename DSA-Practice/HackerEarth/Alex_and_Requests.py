"""
Problem   : Alex and Requests
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/alex-and-requests-72568e72/
Difficulty: Easy
Topic     : Ad-Hoc / Implementation
Date      : 2026-08-21

Approach:
For each incoming request x, only systems with id <= min(n, x) are eligible
(since a system's id acts as a priority ceiling it can accept). Scan
eligible systems from highest id down to 1, and assign the request to the
first system whose current priority is strictly less than x, overwriting
that system's priority with x. If no eligible system qualifies, the
request is rejected.

Time complexity : O(Q * N) worst case (each query may scan up to N systems)
Space complexity: O(N) for the system_priority array
"""


# ----------------------------- Solution ---------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    q = int(data[1])
    system_priority = [0] * (n + 1)
    output = []
    for idx in range(2, 2 + q):
        x = int(data[idx])
        assigned = False
        max_system = min(n, x)
        for sys_id in range(max_system, 0, -1):
            if system_priority[sys_id] < x:
                system_priority[sys_id] = x
                assigned = True
                break
        if assigned:
            output.append("YES")
        else:
            output.append("NO")
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()
