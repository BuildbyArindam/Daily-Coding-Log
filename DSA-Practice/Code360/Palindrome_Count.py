"""
Problem   : Palindrome Count
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/palindrome-count_2409873?kunjiRedirection=true
Difficulty: Hard
Date      : 2026-09-06
Topics    : Bit Manipulation, Hashing, Prefix XOR

Approach:
    A substring s[i..j] can be rearranged into a palindrome iff at most one
    character has an odd frequency in it. Track a running XOR "mask" (26 bits,
    one per lowercase letter) representing the parity of each character's
    count over the prefix ending at the current index.
    For two prefix indices p < q, the substring between them has all-even
    character counts iff mask[p] == mask[q] (zero odd chars -> palindrome-
    rearrangeable), or exactly one odd char iff mask[p] and mask[q] differ in
    exactly one bit.
    So for each new prefix mask, count previously seen masks equal to it
    (even case) plus previously seen masks that are one bit away (odd case),
    using a frequency dict keyed by mask value. Update the dict after counting.

Time complexity : O(26 * n)   -- 26 bit flips checked per character
Space complexity: O(min(2^26, n)) -- frequency dict keyed by distinct XOR masks
"""


# ----------------------- Solution --------------------------------


def palinCount(string: str) -> int:
    freq = {0: 1}
    mask = 0
    ans = 0
    for ch in string:
        bit = ord(ch) - ord('a')
        mask ^= (1 << bit)
        ans += freq.get(mask, 0)
        for i in range(26):
            one_bit_diff = mask ^ (1 << i)
            ans += freq.get(one_bit_diff, 0)
        freq[mask] = freq.get(mask, 0) + 1
    return ans
