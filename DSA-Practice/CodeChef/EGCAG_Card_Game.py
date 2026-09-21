"""
Problem   : Card Game
Platform  : CodeChef
Link      : http://codechef.com/DSAMONDAY021/problems/EGCAG
Date      : 2026-09-21
Difficulty: Hard
Topics    : Two Pointers, Sliding Window, Greedy, Arrays

Approach:
Greedily scan the deck left to right with a sliding window [left_edge, right_edge).
Expand the window, accumulating running_total, until it reaches at least `low`.
  - If the total also fits within `high`, count it as a "win" and reset the
    window to start fresh right after it (greedy: take the win as early as
    possible to leave more cards for future wins).
  - If the total overshoots `high`, shrink from the left (removing the
    leftmost card) until it's back in range or the window empties.
Stop when the window can no longer reach `low` before running out of cards.

Why greedy works: taking the earliest valid window never hurts future
options, since any win must be a contiguous block, and ending a win as
early as possible only leaves more (or equal) cards for subsequent wins.

Complexity:
  Time : O(n) — left_edge and right_edge each move forward at most n times
         total (amortized two-pointer / sliding-window bound).
  Space: O(1) extra (excluding the input array).
"""


# ----------------------------------- Solution ---------------------------------------


import sys

def count_max_wins(deck, low, high):
    deck_size = len(deck)
    left_edge = 0
    right_edge = 0
    running_total = 0
    wins = 0
    while left_edge < deck_size:
        if right_edge < left_edge:
            right_edge = left_edge
        while right_edge < deck_size and running_total < low:
            running_total += deck[right_edge]
            right_edge += 1
        if running_total >= low:
            if running_total <= high:
                wins += 1
                left_edge = right_edge
                running_total = 0
            else:
                running_total -= deck[left_edge]
                left_edge += 1
        else:
            break
    return wins

def main():
    data = sys.stdin.read().split()
    pos = 0
    n = int(data[pos]); pos += 1
    lo = int(data[pos]); pos += 1
    hi = int(data[pos]); pos += 1
    cards = [int(data[pos + idx]) for idx in range(n)]
    print(count_max_wins(cards, lo, hi))

if __name__ == "__main__":
    main()
