/*
 * Problem:    1561. Maximum Number of Coins You Can Get
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
 * Difficulty: Medium
 * Topics:     Array, Math, Greedy, Sorting, Game Theory
 * Date:       2026-10-04
 *
 * Approach:   Greedy + sorting. In each round Alice takes the largest pile,
 *             you take the second largest, and Bob takes the smallest.
 *             After sorting, Bob's share is the lowest n/3 piles, so they
 *             are skipped. From index n/3 onward, the piles pair up as
 *             (yours, Alice's), so we sum every second element.
 *
 * Time:       O(n log n), dominated by the sort
 * Space:      O(1) extra, ignoring the sort's internal stack usage
 */


// ----------------------------------------------- Solution --------------------------------------------------------


class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());
        int res = 0;

        for (int i = piles.size() / 3; i < piles.size(); i += 2) {
            res += piles[i];
        }
        return res;   
    }
};
