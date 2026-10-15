"""
Problem   : Maximum Without 3 Consecutive Set Bits
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/geek-hates-too-many-1s--170647/1
Difficulty: Medium
Topics    : Bit Magic
Date      : 2026-10-15

Approach:
    Scan the binary representation of n from MSB to LSB while tracking the
    length of the current run of kept 1s. A 1 is kept only if fewer than two
    1s have been kept in a row. Otherwise it is turned off, which breaks the
    run. A 0 also resets the run. Turning off the third 1 of a run (not an
    earlier one) preserves the higher-order bits, so the result is as large
    as possible.

Time Complexity : O(log n) - one pass over the bits of n
Space Complexity: O(log n) - binary string (O(1) if bits are read via shifts)
"""


# ----------------------------------------- Solution ----------------------------------------------------------


class Solution:
    def maxValue(self, n: int) -> int:
        """code here"""
        bits = bin(n)[2:]
        result = 0
        consecutive = 0
        for bit in bits:
            result <<= 1
            if bit == '1' and consecutive < 2:
                result |= 1
                consecutive += 1
            else:
                consecutive = 0
        return result
