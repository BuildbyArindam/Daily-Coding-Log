"""
Platform   : CodeChef
Problem    : Houses Under Watch (HUNDW)
Link       : https://www.codechef.com/problems/HUNDW
Difficulty : 1242
Topics     : Arrays, Brute Force, Data Structures
Date       : 2026-10-12

Approach:
    Each watcher at position p covers every house in [p - R, p + R],
    where R = speed * mins, clamped to the range [1, 100].
    Collect all covered houses in a set (which removes overlaps between
    watchers), then the unwatched count is 100 - len(set).

Complexity:
    Time  : O(M * min(2R + 1, 100)) per test case, which is O(M) since
            the range is capped at 100 houses.
    Space : O(100) for the set of watched houses, plus O(input) for the
            read buffer.
"""


# ---------------------------------------------- Solution ------------------------------------------------------------


import sys

def solve_all():
    data = sys.stdin.read().split()
    idx = 0
    cases = int(data[idx])
    idx += 1
    answers = []
    while cases > 0:
        cases -= 1
        m = int(data[idx])
        speed = int(data[idx + 1])
        mins = int(data[idx + 2])
        idx += 3
        radius = speed * mins
        watched = set()
        for token in data[idx:idx + m]:
            pos = int(token)
            low = pos - radius
            high = pos + radius
            if low < 1:
                low = 1
            if high > 100:
                high = 100
            watched.update(range(low, high + 1))
        idx += m
        answers.append(str(100 - len(watched)))
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    solve_all()
