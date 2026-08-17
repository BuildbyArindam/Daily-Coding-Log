"""
Problem   : Book Cricket
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bookcricket-bd707e2d/
Difficulty: Easy
Topic     : Basic Programming, Implementation, Simulation
Date      : 2026-08-17

Approach:
    Simulate a book-cricket innings ball by ball. Maintain striker/non-striker
    indices, track runs scored and out/not-out/DNB status per player.
    - On a run ('0'-'6'): add to striker's score; swap strike if runs are odd.
    - On 'W': mark striker out, bring in the next player (if any remain).
    - After every 6 balls (end of over): swap strike, regardless of last ball's parity.
    Players who never got to bat are marked DNB; not-out batsmen get a '*'.

Complexity:
    Time : O(total balls across all test cases)
    Space: O(p) per test case, for scores/is_out/batted arrays
"""


# ----------------------- Solution -----------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for case_num in range(1, t + 1):
        n = int(input_data[idx])
        p = int(input_data[idx + 1])
        balls = input_data[idx + 2]
        idx += 3
        scores = [0] * (p + 1)
        is_out = [False] * (p + 1)
        batted = [False] * (p + 1)
        striker, non_striker = 1, 2
        batted[1] = batted[2] = True
        next_player = 3
        for ball_num, ch in enumerate(balls):
            if ch == 'W':
                is_out[striker] = True
                striker = next_player
                if next_player <= p:
                    batted[next_player] = True
                    next_player += 1
            else:
                runs = int(ch)
                scores[striker] += runs
                if runs % 2 != 0:
                    striker, non_striker = non_striker, striker
            if (ball_num + 1) % 6 == 0:
                striker, non_striker = non_striker, striker
        print(f"Case {case_num}:")
        for i in range(1, p + 1):
            if not batted[i]:
                print(f"Player {i}: DNB")
            elif is_out[i]:
                print(f"Player {i}: {scores[i]}")
            else:
                print(f"Player {i}: {scores[i]}*")

if __name__ == '__main__':
    solve()
