"""
Problem   : Gallery Turnstile Ledger
Platform  : Unstop
Link      : https://unstop.com/code/practice/673227
Difficulty: Easy
Date      : 2026-11-21
Topics    : Array, Sliding Window, Queue, Hashing, Counting

Approach  :
    Sliding window over time-ordered (timestamp, visitor_id) entries using a
    two-pointer queue (head = newest entry, tail = oldest entry still in window).
    For each entry, evict from the tail every entry with stamp <= now - span.
    A hash map counts occurrences per visitor, and a visitor is removed from the
    map when their count hits 0, so len(census) is the number of unique visitors
    in the window. That value is recorded per entry, and the first strict
    maximum (and the time it occurred) is tracked.

Complexity:
    Time  : O(n)  - each entry is added once and evicted at most once.
    Space : O(n)  - input tokens and answers array; the map holds at most
                    the number of distinct visitors in the window.
"""


# ------------------------------------------- Solution ----------------------------------------------------------


import sys

def run():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    span = int(tokens[1])
    stamps = tokens[2:2 + 2 * n:2]
    ids = tokens[3:3 + 2 * n:2]
    stamps = list(map(int, stamps))
    census = {}       
    tail = 0         
    unique = 0         
    answers = [0] * n
    peak = -1
    peak_minute = -1
    for head in range(n):
        now = stamps[head]
        who = ids[head]
        limit = now - span
        while stamps[tail] <= limit:
            old = ids[tail]
            census[old] -= 1
            if census[old] == 0:
                del census[old]
                unique -= 1
            tail += 1
        seen = census.get(who, 0)
        if seen == 0:
            unique += 1
        census[who] = seen + 1
        answers[head] = unique
        if unique > peak:
            peak = unique
            peak_minute = now
    sys.stdout.write(str(peak) + " " + str(peak_minute) + "\n")
    sys.stdout.write(" ".join(map(str, answers)) + "\n")

run()
