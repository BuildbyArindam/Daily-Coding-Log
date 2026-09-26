"""
Problem   : Denethor's Decryption of Dequeue Permutations
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/DQPERMS
Difficulty: Hard
Topics    : Fenwick Tree / BIT, Combinatorics, Constructive Algorithms, Permutations & Rank computation, Modular Arithmetic, Binary Search on BIT
Date      : 2026-09-26

Approach:
  A permutation of [1..n] is built by repeatedly popping the front or back
  element of a deque. Each observation (i, j) tells us where the element that
  ends up at position j came from at step i, letting us derive the two
  boundary "values consumed so far" (z_i, z_i-1) at that step. These act as
  checkpoints on a number line: checkpoint[x] = value at time x.

  Checkpoints are stored in an order-statistics structure (Fenwick/BIT over
  positions), so for any new checkpoint x we can find its immediate left and
  right neighbours (already-fixed checkpoints) in O(log n) via prefix-sum +
  k-th element queries. Each new checkpoint must be consistent with its
  neighbours (value must lie within the reachable range given the gap in
  positions) - if not, the whole test case is marked "bad" (-1 from then on).

  The number of permutations consistent with the checkpoints so far is
  tracked incrementally as a minimum-rank / maximum-rank pair. Inserting a
  checkpoint only changes the contribution of the single interval it splits,
  so the running rank is updated by removing the old interval's contribution
  and adding the two new sub-intervals' contributions. Interval contributions
  are prefix sums of powers of 2 (mod 1e9+7), precomputed once per test case.

Complexity:
  Let n = size of permutation, m = n/2 = number of observations per test.
  Time  : O(n) precompute (powers, prefix sums) + O(m log n) per test case
          for Fenwick add/prefix/kth-order queries.
  Space : O(n) for Fenwick tree, checkpoint array, and power/prefix tables.
"""


# -------------------------------------------- Solution -------------------------------------------


import sys
MOD = 1_000_000_007

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, pos, delta=1):
        p = pos + 1
        while p <= self.n:
            self.tree[p] += delta
            p += p & -p

    def prefix(self, pos):
        if pos < 0:
            return 0
        p = min(pos + 1, self.n)
        ans = 0
        while p:
            ans += self.tree[p]
            p -= p & -p
        return ans

    def kth(self, k):
        idx = 0
        got = 0
        jump = 1 << (self.n.bit_length() - 1)
        while jump:
            nxt = idx + jump
            if nxt <= self.n and got + self.tree[nxt] < k:
                got += self.tree[nxt]
                idx = nxt
            jump >>= 1
        return idx

def process_test(n, observations):
    m = n // 2
    last_bit = n - 1
    powers = [1] * (last_bit + 1)
    for e in range(1, last_bit + 1):
        powers[e] = (powers[e - 1] * 2) % MOD
    pref = [0] * (last_bit + 1)
    for t in range(1, last_bit + 1):
        pref[t] = (pref[t - 1] + powers[last_bit - t]) % MOD
    checkpoint = [None] * (m + 1)
    checkpoint[0] = 0
    fenwick = Fenwick(m + 1)
    fenwick.add(0)
    active_points = 1
    minimum_rank = 0
    maximum_rank = pref[last_bit]
    bad = False
    answer = []
    def min_interval(a, b, za, zb):
        d = zb - za
        return (pref[b] - pref[a + d]) % MOD
        
    def max_interval(a, b, za, zb):
        d = zb - za
        return (pref[b - d] - pref[a]) % MOD
    def insert_checkpoint(x, value):
        nonlocal minimum_rank, maximum_rank
        nonlocal active_points, bad
        if bad:
            return
        if value < 0 or value > x:
            bad = True
            return
        if checkpoint[x] is not None:
            if checkpoint[x] != value:
                bad = True
            return
        before = fenwick.prefix(x - 1)
        left = fenwick.kth(before) if before else None
        upto = fenwick.prefix(x)
        right = fenwick.kth(upto + 1) if upto < active_points else None
        left_value = checkpoint[left]
        if value - left_value < 0 or value - left_value > x - left:
            bad = True
            return
        if right is not None:
            right_value = checkpoint[right]
            if right_value - value < 0 or right_value - value > right - x:
                bad = True
                return
        if right is None:
            old_min = 0
            old_max = (pref[last_bit] - pref[left]) % MOD
        else:
            old_min = min_interval(
                left, right, left_value, checkpoint[right]
            )
            old_max = max_interval(
                left, right, left_value, checkpoint[right]
            )
        new_min = min_interval(left, x, left_value, value)
        new_max = max_interval(left, x, left_value, value)
        if right is None:
            new_max += pref[last_bit] - pref[x]
            new_max %= MOD
        else:
            new_min += min_interval(
                x, right, value, checkpoint[right]
            )
            new_max += max_interval(
                x, right, value, checkpoint[right]
            )
            new_min %= MOD
            new_max %= MOD
        minimum_rank = (minimum_rank - old_min + new_min) % MOD
        maximum_rank = (maximum_rank - old_max + new_max) % MOD
        checkpoint[x] = value
        fenwick.add(x)
        active_points += 1
    for i, j in observations:
        if bad:
            answer.append(None)
            continue
        if j <= i:
            zi = j
            zim1 = j - 1
        elif j >= n - i + 1:
            zi = i + j - n - 1
            Z_im1_same = zi
            zim1 = Z_im1_same
        else:
            bad = True
            answer.append(None)
            continue
        insert_checkpoint(i - 1, zim1)
        insert_checkpoint(i, zi)
        if bad:
            answer.append(None)
        else:
            answer.append((minimum_rank, maximum_rank))
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    output = []
    for _ in range(t):
        n = next(it)
        m = n // 2
        observations = []
        for _ in range(m):
            i = next(it)
            j = next(it)
            observations.append((i, j))
        result = process_test(n, observations)
        for item in result:
            if item is None:
                output.append("-1")
            else:
                lo, hi = item
                output.append(f"{lo} {hi}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
