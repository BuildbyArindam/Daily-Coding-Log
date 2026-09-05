# Problem: The Excavation Ledger
# Platform: Unstop
# Link: https://unstop.com/code/practice/659206
# Difficulty: Easy
# Date Solved: 2026-09-05
# Topics: Prefix Sum, Hashing, Frequency Counting, Modular Arithmetic, Subarray Sum
#
# Approach:
# Count subarrays whose sum is divisible by k. Track running prefix sum mod k.
# Two prefix sums with the same remainder mean the subarray between them sums
# to a multiple of k. freq[r] stores how many prefixes so far have remainder r
# (freq[0] = 1 to account for the empty prefix). For each new prefix remainder,
# add freq[that remainder] to the answer, then increment its count.
#
# Time Complexity: O(n)      -- single pass over the array
# Space Complexity: O(k)     -- frequency array over remainders mod k


# ------------------------- Solution ----------------------------------


n, k = map(int, input().split())
a = list(map(int, input().split()))
freq = [0] * k
freq[0] = 1
prefix = 0
answer = 0
for x in a:
    prefix = (prefix + x) % k
    answer += freq[prefix]
    freq[prefix] += 1
print(answer)
