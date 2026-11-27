"""
Problem   : Layered Calibration Trials
Platform  : Unstop
Link      : https://unstop.com/code/practice/674448
Difficulty: Medium
Topics    : Array, Stack, Hashing, Simulation, Data Structures
Date      : 2026-11-27

Approach:
    Simulate a key-value store with nested transactions.
    - `cfg` (hash map) holds the current key -> value pairs.
    - `state[0]` is a running total of all values, so the "T" query is O(1).
    - `undo` is a stack of (key, previous_value) entries, recorded only while
      at least one transaction is open.
    - `marks` is a stack of undo-stack lengths, one per open transaction.
      Rollback pops undo entries back down to the saved length, restoring
      each key (or deleting it if it didn't exist before) and adjusting
      the running total.
    - Commit pops the mark. When the outermost transaction commits,
      the undo log is cleared, since nothing can be rolled back anymore.

Complexity:
    Time : O(n) overall. Every operation is O(1), and each undo entry is
           pushed and popped at most once, so rollbacks are amortized O(1).
    Space: O(n) for the map and the undo stack.
"""


# ----------------------------------------------- Solution --------------------------------------------------------------


import sys

def run_script(items):
    cfg = {}       
    undo = []        
    marks = []      
    state = [0]       
    answers = []
    def rollback(limit):
        while len(undo) > limit:
            key, prev = undo.pop()
            cur = cfg[key]
            state[0] -= cur
            if prev is None:
                del cfg[key]
            else:
                cfg[key] = prev
                state[0] += prev
    for tok in items:
        head = tok[0]
        if head == 'S':
            left, right = tok[1:].split('=')
            key = int(left)
            val = int(right)
            prev = cfg.get(key)
            if marks:
                undo.append((key, prev))
            if prev is not None:
                state[0] -= prev
            cfg[key] = val
            state[0] += val
        elif head == 'G':
            answers.append(cfg.get(int(tok[1:]), -1))
        elif head == 'T':
            answers.append(state[0])
        elif head == 'B':
            marks.append(len(undo))
        elif head == 'D':
            rollback(marks.pop())
        else:  
            marks.pop()
            if not marks:
                undo.clear()  
    return answers

def main():
    data = sys.stdin.read().split()
    count = int(data[0])
    result = run_script(data[1:1 + count])
    print(' '.join(map(str, result)))

main()
