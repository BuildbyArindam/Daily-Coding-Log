"""
Problem   : Monk and Power of Time
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-power-of-time/
Difficulty: Easy
Topics    : Data Structures, Queue, Arrays (1-D)
Date      : 2026-08-30

Approach:
Simulate the calling order against the ideal order using a queue (deque).
At each second, if the front of the calling queue matches the front of the
ideal queue, pop both (that person's turn is "resolved"). Otherwise, rotate
the front of the calling queue to the back (they wait one more unit of time).
Each iteration of the loop costs 1 unit of time, so the total loop count is
the answer. This is the classic "round-robin until match" simulation pattern.

Time Complexity : O(n^2) worst case — each mismatch requeues the front element,
                  and in the worst case this can happen O(n) times per match.
Space Complexity: O(n) — two deques of size n.
"""


# -------------------------- Solution -------------------------------


from collections import deque

def solve():
    n = int(input())
    calling_order = deque(map(int, input().split()))
    ideal_order = deque(map(int, input().split()))
    total_time = 0
    while calling_order:
        if calling_order[0] == ideal_order[0]:
            calling_order.popleft()
            ideal_order.popleft()
        else:
            calling_order.append(calling_order.popleft())
        total_time += 1
    print(total_time)

if __name__ == '__main__':
    solve()
