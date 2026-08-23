"""
Problem   : Airport Boarding Reshuffle
Platform  : Unstop
Link      : https://unstop.com/code/practice/656217
Difficulty: Easy
Topics    : Queue, Simulation, Data Structures & Algorithms
Date      : 2026-08-23

Approach:
Maintain the boarding line as a doubly linked list (prev[]/next[] arrays
indexed by passenger id) instead of a plain queue, so a passenger can be
pulled out from anywhere and reinserted at the front in O(1).
  - 'A'      -> append new passenger to the back of the line
  - 'P x'    -> unlink passenger x from wherever they are and relink
                them at the front (priority boarding)
  - 'B'      -> pop and record the passenger currently at the front
state[] tracks each passenger as unadded/in-line/boarded to guard against
invalid moves.

Time complexity : O(n + m) — every operation (add, priority-move, board)
                   is O(1) with the doubly linked list.
Space complexity : O(n) — prev[], next[], state[] arrays sized to n passengers.
"""


# --------------------------- Solution --------------------------------


from sys import stdin, stdout, setrecursionlimit

from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10**6)
def solve():
    input = stdin.readline
    n, m = map(int, input().split())
    prev = [0] * (n + 1)
    next = [0] * (n + 1)
    front = 0
    back = 0
    state = [0] * (n + 1)
    next_id = 1
    out = []
    def add_passenger(x):
        nonlocal front, back
        state[x] = 1
        if front == 0:
            front = back = x
        else:
            next[back] = x
            prev[x] = back
            back = x
    def move_to_front(x):
        nonlocal front, back
        if state[x] != 1 or x == front:
            return
        p = prev[x]
        q = next[x]
        next[p] = q
        if q != 0:
            prev[q] = p
        else:
            back = p
        prev[x] = 0
        next[x] = front
        prev[front] = x
        front = x
    def board():
        nonlocal front, back
        if front == 0:
            out.append("0")
            return
        x = front
        new_front = next[x]
        if new_front == 0:
            front = back = 0
        else:
            front = new_front
            prev[front] = 0
        next[x] = 0
        prev[x] = 0
        state[x] = 2
        out.append(str(x))
    for _ in range(m):
        parts = input().split()
        if parts[0] == 'A':
            add_passenger(next_id)
            next_id += 1
        elif parts[0] == 'P':
            x = int(parts[1])
            move_to_front(x)
        else:  
            board()
    stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
