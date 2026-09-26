"""
Problem: Dyslexic Gollum
Platform: CodeChef (ICPC Trinity Practice Course)
Link: https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/PSTRINGS
Date: 2026-09-26
Difficulty: Hard
Topics: Dynamic Programming, Bitmasking, Finite-State Automaton, Combinatorics, Palindromes

Approach:
    For each distinct k in the queries, count binary strings of length n that
    contain no palindromic substring of length k or k+1.
    - For n < k, every string qualifies -> 2^n.
    - For n >= k, run a DP over states = last k bits (as a k-bit mask).
      A state is valid only if it doesn't already end in a length-k palindrome.
      Precompute, for each state, the next state reached by appending a 0 or 1,
      rejecting transitions that would create a palindrome of length k or k+1
      in the new k+1-bit window. Transition the DP forward one character at a
      time up to the maximum required n, recording sum(dp) at each length as
      the answer for that length.
    - Precompute all k's needed across queries once, then answer each query
      in O(1) by table lookup.

Complexity (let K = set of distinct k values across queries, N = max n):
    Time:  O(sum over k in K of (2^k * k  +  N * 2^k))
           (2^k * k to build palindrome-check tables, N * 2^k for the DP transitions)
    Space: O(sum over k in K of (2^k + N))   (DP states + answer table per k)
"""


# ------------------------------------- Solution -----------------------------------------------


import sys
MOD = 1_000_000_007
MAX_N = 400

def make_pal_table(length):
    size = 1 << length
    result = [False] * size
    for x in range(size):
        ok = True
        half = length // 2
        for i in range(half):
            if ((x >> i) & 1) != ((x >> (length - 1 - i)) & 1):
                ok = False
                break
        result[x] = ok
    return result

def build_answers(k, limit):
    ans = [0] * (limit + 1)
    if k == 1:
        return ans
    cur_limit = min(limit, k - 1)
    for n in range(1, cur_limit + 1):
        ans[n] = pow(2, n, MOD)
    if limit < k:
        return ans
    states = 1 << k
    mask = states - 1
    pal_k = make_pal_table(k)
    pal_k1 = make_pal_table(k + 1)
    dp = [0] * states
    for x in range(states):
        if not pal_k[x]:
            dp[x] = 1
    ans[k] = sum(dp) % MOD
    next_zero = [-1] * states
    next_one = [-1] * states
    for state in range(states):
        candidate = state << 1
        suffix_k = candidate & mask
        if not pal_k[suffix_k] and not pal_k1[candidate]:
            next_zero[state] = suffix_k
        candidate |= 1
        suffix_k = candidate & mask
        if not pal_k[suffix_k] and not pal_k1[candidate]:
            next_one[state] = suffix_k
    for length in range(k + 1, limit + 1):
        new_dp = [0] * states
        for state, ways in enumerate(dp):
            if ways == 0:
                continue
            dest = next_zero[state]
            if dest != -1:
                value = new_dp[dest] + ways
                if value >= MOD:
                    value -= MOD
                new_dp[dest] = value
            dest = next_one[state]
            if dest != -1:
                value = new_dp[dest] + ways
                if value >= MOD:
                    value -= MOD
                new_dp[dest] = value
        dp = new_dp
        ans[length] = sum(dp) % MOD
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    queries = []
    p = 1
    maximum_n = 0
    needed_k = set()
    for _ in range(t):
        n = data[p]
        k = data[p + 1]
        p += 2
        queries.append((n, k))
        maximum_n = max(maximum_n, n)
        needed_k.add(k)
    precomputed = {}
    for k in needed_k:
        precomputed[k] = build_answers(k, maximum_n)
    output = []
    for n, k in queries:
        output.append(str(precomputed[k][n]))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
