/*
 * Problem   : 1463. Cherry Pickup II
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/cherry-pickup-ii/
 * Difficulty: Hard
 * Topics    : Array, Dynamic Programming, Matrix
 * Date      : 2026-10-08
 *
 * Approach (Top-Down DP + Memoization):
 *   - Both robots move down one row per step, so they are always on the same row.
 *     State = (row, col of robot 1, col of robot 2).
 *   - At each state, collect cherries at the current cell(s). If both robots share
 *     a cell, count it only once.
 *   - Try all 9 combinations of next moves (each robot goes to col-1, col, col+1
 *     in the next row) and take the best result.
 *   - Out-of-bounds columns or rows past the last row contribute 0.
 *   - Memoize results in dp[r][c0][c1] to avoid recomputation.
 *
 * Time Complexity : O(R * C * C * 9) = O(R * C^2)
 * Space Complexity: O(R * C^2) for the memo table, plus O(R) recursion stack
 */


// -------------------------------------------- Solution -------------------------------------------------


class Solution {
public:
    int dp[70][70][70];
    int row, col;
    int f(int r, int c0, int c1, vector<vector<int>>& grid){
        if (r>=row || c0<0 || c0>=col || c1<0 || c1>=col) return 0;
        if (dp[r][c0][c1]!=-1) return dp[r][c0][c1];
        // whether 2 robots are in different cell
        int ans=(c0!=c1)?grid[r][c0]+grid[r][c1]:grid[r][c0];
        int next=0;
        //9 possiblities for the next moves for the robots
        for (int d0: {c0-1, c0, c0+1})
            for( int d1: { c1-1, c1, c1+1}){
                next=max(next, f(r+1, d0, d1, grid));//take max
            }
        ans+=next;// add the max cherries from r+1th row to ans
        return dp[r][c0][c1]=ans;
    }
    int cherryPickup(vector<vector<int>>& grid) {
        row=grid.size(), col=grid[0].size();
        memset(dp, -1, sizeof(dp));
        int ans=f(0, 0, col-1, grid);
        return ans;
    }
};

auto init = []()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();
