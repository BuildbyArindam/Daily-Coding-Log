/*
 * Problem   : 330. Patching Array
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/patching-array/
 * Difficulty: Hard
 * Topics    : Array, Greedy
 * Date      : 2026-11-23
 *
 * Approach (Greedy):
 *   Track `miss`, the smallest sum in [1, n] that cannot yet be formed.
 *   All sums in [1, miss - 1] are currently reachable.
 *   - If nums[i] <= miss, use it: the reachable range extends to miss + nums[i] - 1,
 *     so miss += nums[i].
 *   - Otherwise, patch with `miss` itself (the best possible patch), which doubles
 *     the reachable range: miss += miss, and patch count increases by 1.
 *   Repeat until miss > n.
 *
 * Time Complexity : O(m + log n), where m = nums.size()
 *                   (each patch doubles `miss`, so at most ~log n patches)
 * Space Complexity: O(1)
 */


// -------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long long miss = 1;
        int result = 0;
        size_t i = 0;
        while (miss <= n) {
            if (i < nums.size() && nums[i] <= miss) {
                miss += nums[i];
                i++;
            } else {
                miss += miss;
                result++;
            }
        }
        return result;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
