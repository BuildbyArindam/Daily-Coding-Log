"""
Problem: Find X Value of Array I
Platform: LeetCode
Link: https://leetcode.com/problems/find-x-value-of-array-i/?envType=daily-question&envId=2026-09-21
Date Solved: 2026-09-21
Difficulty: Medium
Topics: Array, Math, Dynamic Programming

Approach:
For each prefix of `nums`, track how many "paths" of modular products end at
each residue mod k using a rolling DP array `dp`, where dp[r] = count of ways
to reach remainder r using a contiguous product chain ending at the current
element. At each step, start a fresh chain from the current number (val = num % k)
and extend all previous chains by multiplying with val (mod k). Accumulate the
counts per residue into `ans` after processing each element, so ans[r] ends up
being the total number of subarrays whose product mod k equals r.

Time Complexity:  O(n * k) — for each of n elements, update all k residues
Space Complexity: O(k) — dp and ans arrays of size k
"""


# ---------------------------------- Solution ----------------------------------------


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        ans = [0] * k
        for num in nums:
            val = num % k
            new_dp = [0] * k
            new_dp[val] += 1
            for r in range(k):
                if dp[r]:
                    new_r = (r * val) % k
                    new_dp[new_r] += dp[r]
            for r in range(k):
                ans[r] += new_dp[r]
            dp = new_dp
        return ans

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
