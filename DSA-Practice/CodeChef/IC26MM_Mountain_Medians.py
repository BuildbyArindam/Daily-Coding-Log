"""
Problem   : Mountain Medians (IC26MM)
Platform  : CodeChef (ICPCOL26POST)
Link      : https://www.codechef.com/ICPCOL26POST/problems/IC26MM
Date      : 2026-10-06
Difficulty: Hard (~2500 est.)
Topics    : Combinatorics, Lattice-path DP, Casework, Bitset packing, NumPy

Approach:
  1. lattice_rules(): for each position k, derive its median window
     (h = ceil(k/2), q = floor((m+2-k)/2)) and compare the target value
     w[k] against the thresholds (edge, fa, fb). Each case yields O(1)
     constraints on a monotone lattice path: pinned x-values at step t,
     lower/upper bounds, and banned cells (column / diagonal / row bans).
     If w[k] exceeds both fa and fb, the answer is 0.
  2. Count lattice paths over t = 1..m. Each step moves x -> x+1 or x -> x,
     and the pins, bans and bounds from step 1 are applied at every step.
  3. m < 60: pack the per-x counts into wd-bit fields of one Python big
     integer. Counts are at most 2^m, so they never overflow a field and
     no modulo is needed until the end. Shifts and masks do the transitions.
  4. m >= 60: NumPy int64 vector DP with boolean ban matrices, reduced
     mod 998244353 each step.

Complexity (per test, m = array length):
  Rule derivation : O(m)
  NumPy DP        : O(m^2) time, O(m^2) space (ban matrices)
  Packed DP       : roughly O(m^4 / w) time, only used for m < 60
"""


# ------------------------------------------ Solution -----------------------------------------------------


import sys
import numpy as np

MODP = 998244353

def lattice_rules(m, arr):
    pinA = [None] * (m + 2) 
    pinB = [None] * (m + 2)   
    lowB = [0] * (m + 2)   
    upB = [m] * (m + 2)   
    colBan = []        
    diagBan = []   
    rowBan = []   
    def merge(store, t, val):
        old = store[t]
        if old is None:
            store[t] = val
        elif old != val:
            store[t] = -1
    for k in range(1, m + 1):
        h = (k + 1) >> 1
        q = (m + 2 - k) >> 1
        edge = h + q - 1
        fa = q + k - 1
        fb = h + m - k
        w = arr[k - 1]
        xl = h - 1 if w - h >= 0 else -1
        xr = w - q if w - q >= 0 else -1
        if w <= edge:
            if w == edge and (k == 1 or k == m):
                continue
            merge(pinA, w, xl)
            merge(pinB, w, xr)
            continue
        if w > fa and w > fb:
            return None
        if w > fa:
            if w < fb:
                merge(pinA, w, xl)
                merge(pinB, w, -1)
            else:
                colBan.append((h - 1, edge + 1, fb - 1))
                upB[edge] = min(upB[edge], h - 1)
        elif w == fa:
            if k - 2 >= h:
                diagBan.append((q, h, k - 2))
            if w < fb:
                colBan.append((h - 1, edge + 1, fa - 1))
                colBan.append((h - 1, fa + 1, m))
                lowB[fa] = max(lowB[fa], h)
            elif w == fb:
                colBan.append((h - 1, edge + 1, fb - 1))
            else:
                lowB[edge] = max(lowB[edge], h)
        else:
            if w < fb:
                merge(pinA, w, xl)
                merge(pinB, w, xr)
            elif w == fb:
                colBan.append((h - 1, edge + 1, fb - 1))
                rowBan.append((q, edge + 1, m, fb))
                upB[fb] = min(upB[fb], fb - q)
            else:
                merge(pinA, w, -1)
                merge(pinB, w, xr)
    return pinA, pinB, lowB, upB, colBan, diagBan, rowBan

def count_packed(m, arr):
    res = lattice_rules(m, arr)
    if res is None:
        return 0
    pinA, pinB, lowB, upB, colBan, diagBan, rowBan = res
    wd = m + 2
    one = (1 << wd) - 1
    everything = (1 << (wd * (m + 2))) - 1
    banA = [0] * (m + 2)
    banB = [0] * (m + 2)
    for x, t1, t2 in colBan:
        u = one << (x * wd)
        for t in range(t1, t2 + 1):
            banA[t] |= u
    for c, x1, x2 in diagBan:
        for x in range(x1, x2 + 1):
            banB[x + c] |= one << (x * wd)
    for c, t1, t2, sk in rowBan:
        for t in range(max(t1, c), t2 + 1):
            if t != sk:
                banB[t] |= one << ((t - c) * wd)
    cur = 1
    for t in range(1, m + 1):
        pa = pinA[t]
        part = cur & (everything ^ banA[t])
        if pa is not None:
            part = (part & (one << (pa * wd))) if pa >= 0 else 0
        nxt = part << wd
        if t < m:
            pb = pinB[t]
            part = cur & (everything ^ banB[t])
            if pb is not None:
                part = (part & (one << (pb * wd))) if pb >= 0 else 0
            nxt += part
        if lowB[t] > 0:
            nxt &= everything ^ ((1 << (lowB[t] * wd)) - 1)
        if upB[t] < m:
            nxt &= (1 << ((upB[t] + 1) * wd)) - 1
        cur = nxt
        if not cur:
            return 0
    total = 0
    while cur:
        total += cur & one
        cur >>= wd
    return total % MODP

def count_numpy(m, arr):
    res = lattice_rules(m, arr)
    if res is None:
        return 0
    pinA, pinB, lowB, upB, colBan, diagBan, rowBan = res
    sz = m + 2
    banAT = np.zeros((sz, sz), dtype=np.bool_)
    banB = np.zeros((sz, sz), dtype=np.bool_)
    for x, t1, t2 in colBan:
        if t1 <= t2:
            banAT[x, t1:t2 + 1] = True
    for c, x1, x2 in diagBan:
        xs = np.arange(x1, x2 + 1)
        banB[xs + c, xs] = True
    for c, t1, t2, sk in rowBan:
        ts = np.arange(max(t1, c), t2 + 1)
        ts = ts[ts != sk]
        banB[ts, ts - c] = True
    banA = np.ascontiguousarray(banAT.T)
    del banAT
    state = np.zeros(sz + 1, dtype=np.int64)
    state[0] = 1
    for t in range(1, m + 1):
        head = state[:t]
        fresh = np.zeros(sz + 1, dtype=np.int64)
        pa = pinA[t]
        if pa is None:
            a1 = np.where(banA[t, :t], 0, head)
        else:
            a1 = np.zeros(t, dtype=np.int64)
            if 0 <= pa < t and not banA[t, pa]:
                a1[pa] = head[pa]
        fresh[1:t + 1] = a1
        if t < m:
            pb = pinB[t]
            if pb is None:
                b1 = np.where(banB[t, :t], 0, head)
            else:
                b1 = np.zeros(t, dtype=np.int64)
                if 0 <= pb < t and not banB[t, pb]:
                    b1[pb] = head[pb]
            fresh[:t] += b1
        fresh %= MODP
        if lowB[t] > 0:
            fresh[:lowB[t]] = 0
        if upB[t] < m:
            fresh[upB[t] + 1:] = 0
        state = fresh
    return int(state.sum() % MODP)

def main():
    tokens = sys.stdin.buffer.read().split()
    cases = int(tokens[0])
    ptr = 1
    answers = []
    for _ in range(cases):
        m = int(tokens[ptr])
        ptr += 1
        arr = list(map(int, tokens[ptr:ptr + m]))
        ptr += m
        answers.append(count_packed(m, arr) if m < 60 else count_numpy(m, arr))
    sys.stdout.write("\n".join(map(str, answers)) + "\n")

main()
