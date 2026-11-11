"""
Problem   : Twilight Census of the Camera Traps
Platform  : Unstop 
Link      : https://unstop.com/code/practice/671309
Date      : 2026-11-11
Difficulty: Easy
Topics    : Sliding Window, Hashing, Frequency Counting, Queue, Array

Approach  :
    Process the camera-trap records in timestamp order with a sliding
    window over time. For each new record, add its species to a frequency
    map (increment the distinct count if it is new), then evict records from
    the tail whose timestamp is <= now - span. When a species' count hits
    zero, remove it and decrement the distinct count. Track the first
    moment the distinct count reaches a new maximum.

Complexity:
    Time  : O(N). Each record enters and leaves the window at most once.
    Space : O(K). K is the number of distinct species in the window, plus
            O(N) for the stored input tokens.
"""


# --------------------------------------------- Solution -----------------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    total = int(tokens[0])
    span = int(tokens[1])
    stamps = tokens[2:2 + 2 * total:2]
    kinds = tokens[3:3 + 2 * total:2]
    tally = {}
    distinct = 0
    tail = 0
    best_variety = 0
    best_minute = -1
    for head in range(total):
        now = int(stamps[head])
        sp = kinds[head]
        c = tally.get(sp, 0)
        if c == 0:
            distinct += 1
        tally[sp] = c + 1
        limit = now - span
        while int(stamps[tail]) <= limit:
            old = kinds[tail]
            left = tally[old] - 1
            if left == 0:
                del tally[old]
                distinct -= 1
            else:
                tally[old] = left
            tail += 1
        if distinct > best_variety:
            best_variety = distinct
            best_minute = now
    sys.stdout.write("PEAK %d AT %d\n" % (best_variety, best_minute))

main()
