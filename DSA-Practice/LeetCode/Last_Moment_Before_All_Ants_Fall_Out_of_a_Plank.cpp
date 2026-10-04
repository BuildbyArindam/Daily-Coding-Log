/*
 * Problem:    1503. Last Moment Before All Ants Fall Out of a Plank
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
 * Difficulty: Medium
 * Topics:     Array, Brainteaser, Simulation
 * Date:       2026-10-04
 *
 * Approach:
 *   When two ants collide and reverse, it is equivalent to them passing
 *   through each other, so collisions can be ignored. Each ant then walks
 *   straight to its exit:
 *     - Left-moving ant at position p exits after p moves.
 *     - Right-moving ant at position p exits after (n - p) moves.
 *   The answer is the maximum of all these exit times.
 *
 * Time Complexity:  O(L + R), where L = left.size() and R = right.size()
 * Space Complexity: O(1)
 */


// ------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int mx = 0;
        for(auto i:left){
            mx = max(mx,i);
        }
        for(auto i:right){
            mx = max(mx,n-i);
        }
        return mx;
    }
};
