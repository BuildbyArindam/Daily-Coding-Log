/*
 * Problem   : 2225. Find Players With Zero or One Losses
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/find-players-with-zero-or-one-losses/
 * Difficulty: Medium
 * Topics    : Array, Hash Table, Sorting, Counting
 * Date      : 2026-10-03
 *
 * Approach:
 *   Count losses per player in an ordered map. Every winner is inserted
 *   with 0 losses if not already present, and every loser's count is
 *   incremented. Because std::map iterates in sorted key order, a single
 *   pass over it collects players with 0 or 1 losses already sorted, so
 *   no separate sort is needed. ans[nLosses] maps directly to the
 *   required output rows (index 0 = no losses, index 1 = exactly one).
 *
 * Complexity:
 *   Time  : O(n log p), n = number of matches, p = distinct players (p <= 2n)
 *   Space : O(p) for the map
 */


// ------------------------------------- Solution -------------------------------------------------------


class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        vector<vector<int>> ans(2);
    map<int, int> lossesCount;

    for (const vector<int>& m : matches) {
      const int winner = m[0];
      const int loser = m[1];
      if (!lossesCount.count(winner))
        lossesCount[winner] = 0;
      ++lossesCount[loser];
    }
    for (const auto& [player, nLosses] : lossesCount)
      if (nLosses < 2)
        ans[nLosses].push_back(player);
    return ans;
    }
};
