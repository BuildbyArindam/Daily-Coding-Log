"""
Problem : Devu and his Class (DEVCLASS)
Platform: CodeChef
Link    : https://www.codechef.com/problems/DEVCLASS
Rating  : 2007
Topics  : String, Greedy, Data Structures, Algorithms
Date    : 2026-10-17

Approach:
    Boys and girls must alternate, so it is impossible if |B - G| > 1.
    Otherwise the boys must occupy either the even or the odd positions,
    and I try each start parity whose position count equals B.
      - type 0 (swap any two): cost = number of boys not already on a
        target position (each swap fixes one misplaced boy).
      - type 1 (swap adjacent): match the i-th boy to the i-th target
        position in order; cost = sum of |boy_i - target_i|.
    Answer is the minimum over valid parities.

Complexity:
    Time : O(N) per test case
    Space: O(N)
"""


# ------------------------------------------------ Solution -----------------------------------------------------------


import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    T = int(data[0])
    idx = 1
    results = []

    for _ in range(T):
        typ = int(data[idx])
        s = data[idx + 1]
        idx += 2

        n = len(s)
        boys = [i for i, ch in enumerate(s) if ch == 'B']
        B = len(boys)
        G = n - B

        if abs(B - G) > 1:
            results.append("-1")
            continue

        ans = float('inf')

        for start in (0, 1):
            targets = list(range(start, n, 2))

            if len(targets) != B:
                continue

            if typ == 0:
                target_set = set(targets)
                cost = sum(1 for b in boys if b not in target_set)
            else:
                cost = sum(abs(b - t) for b, t in zip(boys, targets))

            ans = min(ans, cost)

        results.append(str(ans))

    print("\n".join(results))


if __name__ == "__main__":
    solve()
