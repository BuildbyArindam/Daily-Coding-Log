"""
Problem   : Lead Game (LEADGAME)
Platform  : CodeChef (ZCO/INOI practice, IARCSJUD)
Link      : https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/LEADGAME
Date      : 2026-10-21
Difficulty: Easy
Topics    : Simulation, Prefix Sums, Implementation

Approach  : Keep a running difference of cumulative scores (Player 1 - Player 2)
            after each round. The absolute value of this difference is the lead,
            and its sign tells who holds it. Track the largest lead seen and
            who had it at that moment. Update only on a strictly greater lead.

Time      : O(N), one pass over the rounds
Space     : O(N), because all input tokens are read at once
            (O(1) extra beyond that)
"""


# ----------------------------------------- Solution --------------------------------------------------------------


import sys

def solve(tokens):
    rounds = int(tokens[0])
    diff = 0        
    best_gap = 0  
    best_who = 1  
    for k in range(rounds):
        a = int(tokens[1 + 2 * k])
        b = int(tokens[2 + 2 * k])
        diff += a - b
        gap = -diff if diff < 0 else diff
        if gap > best_gap:
            best_gap = gap
            best_who = 2 if diff < 0 else 1
    return best_who, best_gap

def main():
    data = sys.stdin.read().split()
    who, gap = solve(data)
    print(who, gap)

if __name__ == "__main__":
    main()
