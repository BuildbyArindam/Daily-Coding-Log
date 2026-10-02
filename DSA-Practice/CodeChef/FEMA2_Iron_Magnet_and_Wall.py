"""
Problem   : Iron, Magnet and Wall (FEMA2)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FEMA2
Difficulty: 1725
Date      : 2026-10-02
Topics    : Greedy, Two Pointers, Queue, Strings

Approach:
    Scan the string left to right, tracking each character's effective
    position as index + (number of ':' seen so far), so every ':' adds
    extra distance. Keep two FIFO queues (lists with a head pointer) of
    unmatched magnets and unmatched irons. For each new 'M' or 'I':
      1. Pop stale entries from the front of the opposite queue (those
         farther than K away).
      2. If an entry remains, match it with the earliest one (greedy:
         the oldest unmatched element is the first to go out of range)
         and increment the answer.
      3. Otherwise, push the current element into its own queue.
    'X' is a wall, so both queues and their pointers are reset.

Time  : O(N) per test case (each element is pushed and popped at most once)
Space : O(N) for the queues
"""


# --------------------------------------- Solution -------------------------------------------------


import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    p = 1
    for _ in range(t):
        n = int(data[p])
        k = int(data[p + 1])
        s = data[p + 2].decode()
        p += 3
        magnets = []
        irons = []
        mh = 0
        ih = 0
        sheets = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == 'X':
                magnets.clear()
                irons.clear()
                mh = 0
                ih = 0
                continue
            if ch == ':':
                sheets += 1
                continue
            cur = i + sheets
            if ch == 'M':
                while ih < len(irons) and cur - irons[ih] > k:
                    ih += 1
                if ih < len(irons):
                    ans += 1
                    ih += 1
                else:
                    magnets.append(cur)
            elif ch == 'I':
                while mh < len(magnets) and cur - magnets[mh] > k:
                    mh += 1
                if mh < len(magnets):
                    ans += 1
                    mh += 1
                else:
                    irons.append(cur)
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
