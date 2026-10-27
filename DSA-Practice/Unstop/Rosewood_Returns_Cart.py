"""
Problem   : Rosewood Returns Cart
Platform  : Unstop 
Link      : https://unstop.com/code/practice/670074
Date      : 2026-10-27
Difficulty: Easy
Topics    : Stack, Array, Counting, Implement

Approach  :
    Simulate the cart with a stack (list) of item codes. Alongside it,
    keep a frequency map (code -> count in stack) and a running counter
    of distinct codes currently in the stack.
      "+ x" : push x; if its count was 0, distinct += 1; count[x] += 1
      "-"   : pop top; count[x] -= 1; if it hits 0, distinct -= 1
      "?"   : print "<top> <distinct>", or "0 0" if the stack is empty
    Distinct count is maintained incrementally, so every query is O(1).
    Input is read in one shot via sys.stdin.buffer for speed.

Complexity:
    Time  : O(N), with O(1) per operation
    Space : O(N), for the stack and frequency map
"""


# --------------------------------------------- Solution ----------------------------------------------------


import sys

def run():
    raw = sys.stdin.buffer.read().split(b"\n")
    total = int(raw[0])
    tally = {}  
    pile = []   
    kinds = 0     
    out = []
    for idx in range(1, total + 1):
        note = raw[idx].split()
        sym = note[0]
        if sym == b"?":
            if pile:
                out.append("%d %d" % (pile[-1], kinds))
            else:
                out.append("0 0")
        elif sym == b"+":
            code = int(note[1])
            seen = tally.get(code, 0)
            if seen == 0:
                kinds += 1
            tally[code] = seen + 1
            pile.append(code)
        else:
            code = pile.pop()
            left = tally[code] - 1
            tally[code] = left
            if left == 0:
                kinds -= 1
    sys.stdout.write("\n".join(out))
    if out:
        sys.stdout.write("\n")

run()
