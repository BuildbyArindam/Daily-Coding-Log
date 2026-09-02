"""
Problem: Computer Game
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/37/B
Date Solved: 2026-09-02
Difficulty: *1800
Topics: Greedy, Implementation

Approach:
Sort spells by HP threshold (descending). Simulate second-by-second:
at each step, unlock all spells whose threshold has been reached
(health <= threshold), then greedily cast the strongest available
spell (max-heap by damage) that hasn't been used yet. Apply damage
then regeneration each second, capping at MAX_HP. Boss dies when
health <= 0 at the end of a second. If no spell is available and
total damage <= regeneration, the fight can never be won -> "NO".

Time Complexity: O(N log N) — each spell pushed/popped from the heap once.
Space Complexity: O(N) — for spells list, heap, and used-spell log.
"""


# ------------------------- Solution ------------------------------------


import sys
import heapq

def solve():
    input = sys.stdin.readline
    N, MAX_HP, REG = map(int, input().split())
    spells = []
    for i in range(1, N + 1):
        p, dmg = map(int, input().split())
        spells.append((p * MAX_HP, dmg, i))
    spells.sort(reverse=True)
    available = []
    ptr = 0
    health = MAX_HP
    total_damage = 0
    time = 0
    used = []
    while True:
        while ptr < N and health * 100 <= spells[ptr][0]:
            threshold, dmg, idx = spells[ptr]
            heapq.heappush(available, (-dmg, idx))
            ptr += 1
        if available:
            neg_dmg, idx = heapq.heappop(available)
            total_damage += -neg_dmg
            used.append((time, idx))
        health = health - total_damage + REG
        if health > MAX_HP:
            health = MAX_HP
        if health <= 0:
            print("YES")
            print(time + 1, len(used))
            for t, idx in used:
                print(t, idx)
            return
        if not available and total_damage <= REG:
            print("NO")
            return
        time += 1

if __name__ == "__main__":
    solve()
