/*
 * Problem   : 1637. Widest Vertical Area Between Two Points Containing No Points
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
 * Difficulty: Easy
 * Topics    : Array, Sorting
 * Date      : 2026-10-03
 *
 * Approach:
 *   The y-coordinates don't matter, since a vertical area extends infinitely
 *   along the y-axis. Sort the points by x-coordinate, then the widest area
 *   is the largest gap between two adjacent x-values.
 *
 * Time Complexity : O(n log n), dominated by sorting
 * Space Complexity: O(log n), for the sort's recursion stack (no extra data structures)
 */


// --------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
       int n = points.size();
       sort(points.begin(), points.end());
       int maxWidth = 0;
       for (int i = 1; i < n; i++) {
           int width = points[i][0] - points[i - 1][0]; 
           maxWidth = max(maxWidth, width); 
       }
       return maxWidth;
    }
};
