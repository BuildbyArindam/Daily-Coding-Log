# Problem   : Too Chocolatey
# Platform  : HackerEarth
# Link      : https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/too-chocolatey-232e97e0/
# Difficulty: Easy
# Topics    : Greedy, Implementation, Hashmap
# Date      : 2026-11-24
#
# Approach:
#   Count the stock of each chocolate value in a frequency array. Players
#   alternate turns, and each greedily takes the largest value that is still
#   in stock and that they haven't taken before. Each player keeps a pointer
#   that only moves downward, plus a "used" table, so no value is rescanned.
#   The game ends when both players are stuck in a row. The higher total wins.
#
# Complexity (per test case):
#   Time : O(N + V), where V = max value (1000). Each pointer sweeps at most
#          V values in total, and each pick is O(1).
#   Space: O(V) for the stock and used tables.


# ------------------------------------------------ Solution ---------------------------------------------------------


def solve(n, arr):
    LIMIT = 1000
    stock = [0] * (LIMIT + 1)
    for v in arr:
        stock[v] += 1
    score = [0, 0]
    used = [[False] * (LIMIT + 1) for _ in range(2)]
    ptr = [LIMIT, LIMIT]
    def take(p):
        k = ptr[p]
        while k > 0 and (stock[k] == 0 or used[p][k]):
            k -= 1
        ptr[p] = k
        if k == 0:
            return False
        stock[k] -= 1
        used[p][k] = True
        score[p] += k
        return True
    who = 0
    stuck = 0
    while stuck < 2:
        stuck = 0 if take(who) else stuck + 1
        who ^= 1
    return "Alex" if score[0] > score[1] else "Bob"

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    out_ = solve(n, arr)
    print (out_)
