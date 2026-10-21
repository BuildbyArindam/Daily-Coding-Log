"""
Problem   : End of Corruption
Platform  : CodeChef (ZCO/INOI practice)
Link      : https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/ENDCORR
Date      : 2026-10-21
Difficulty: Medium
Topics    : Heap / Priority Queue, Greedy

Approach  : Process the events in order. Each positive value is a bribe
            and is pushed onto a max-heap (Python's heapq is a min-heap,
            so values are stored negated). Each -1 is a visit, which
            takes the largest bribe currently in the heap. Since each
            visit always takes the current maximum, the greedy choice
            is optimal.

Complexity: Time  - O((N + M) log N), where N = bribes and M = visits
            Space - O(N) for the heap, plus O(M) for the output
"""


# ------------------------------------------ Solution -------------------------------------------------------


import sys
from heapq import heappush as put, heappop as take

def solve():
    tokens = sys.stdin.read().split()
    total_people = int(tokens[0])
    total_visits = int(tokens[1])
    events = tokens[2:2 + total_people + total_visits]
    answers = []
    vault = [] 
    for item in events:
        value = int(item)
        if value == -1:
            answers.append(-take(vault))
        else:
            put(vault, -value)
    sys.stdout.write("\n".join(map(str, answers)) + "\n")

if __name__ == "__main__":
    solve()
