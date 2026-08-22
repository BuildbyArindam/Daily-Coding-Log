"""
Problem   : Fredo and Game
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/fredo-and-game/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-22

Approach:
Simulate the game turn by turn. Track ammo starting at 'a'. For each
element: if it's 1, gain 2 ammo (reward round); otherwise lose 1 ammo
(cost round). If ammo hits exactly 0 before the last index, Fredo loses
at that round -> print "No <round>". If ammo never hits 0 before the
last round (or hits 0 exactly on the last round), Fredo survives ->
print "Yes <remaining ammo>".

Time Complexity : O(n) per test case (single linear pass)
Space Complexity: O(n) for storing the array (O(1) extra)
"""


# ------------------------- Solution ------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        n = int(data[idx + 1])
        idx += 2
        arr = [int(x) for x in data[idx : idx + n]]
        idx += n
        ammo = a
        game_over = False
        for i in range(n):
            if arr[i] == 1:
                ammo += 2 
            else:
                ammo -= 1 
            if ammo == 0:
                if i < n - 1:
                    print(f"No {i + 1}")
                    game_over = True
                    break
        if not game_over:
            print(f"Yes {ammo}")

if __name__ == "__main__":
    solve()
