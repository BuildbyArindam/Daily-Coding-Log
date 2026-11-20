/*
 * Problem   : 1688. Count of Matches in Tournament
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/count-of-matches-in-tournament/
 * Difficulty: Easy
 * Topics    : Math, Simulation
 * Date      : 2026-10-03
 *
 * Approach:
 *   Every match eliminates exactly one team, regardless of whether the
 *   current round has an even or odd number of teams. To crown a single
 *   winner from n teams, n - 1 teams must be eliminated, so exactly
 *   n - 1 matches are played. No simulation is needed.
 *
 * Time Complexity : O(1)
 * Space Complexity: O(1)
 */


// -------------------------------------- Solution --------------------------------------------------


class Solution {
public:
    int numberOfMatches(int n) {
        return n - 1;
    }
};
