/*
 * Problem   : 458. Poor Pigs
 * Link      : https://leetcode.com/problems/poor-pigs/
 * Platform  : LeetCode
 * Difficulty: Hard
 * Topics    : Math, Dynamic Programming, Combinatorics
 * Date      : 2026-10-07
 *
 * Approach:
 *   Each pig can be in (periods + 1) states, where
 *   periods = minutesToTest / minutesToDie:
 *   it dies in one of the `periods` rounds, or survives all of them.
 *   With p pigs, we can distinguish (periods + 1)^p buckets.
 *   So find the smallest p such that (periods + 1)^p >= buckets.
 *   (Integer loop used instead of log/ceil to avoid floating-point error.)
 *
 * Time Complexity : O(log(buckets) / log(periods + 1)), i.e. O(log buckets)
 * Space Complexity: O(1)
 */


// ----------------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int states = minutesToTest / minutesToDie + 1;
        int pigs = 0;
        long long covered = 1;
        while (covered < buckets) {
            covered *= states;
            pigs++;
        }
        return pigs;
    }
};
