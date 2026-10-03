/*
 * Problem   : 935. Knight Dialer
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/knight-dialer/
 * Difficulty: Medium
 * Topics    : Dynamic Programming
 * Date      : 2026-10-03
 *
 * Approach  : Top-down DP (memoization) over (digit, remaining_length).
 *             adj[i] lists the digits a knight can jump to from digit i.
 *             f(i, n) = number of distinct numbers of length n that start
 *             at digit i = sum of f(j, n-1) over all j in adj[i].
 *             Base case: n == 1 -> 1 (a single digit). Digit 5 has no
 *             knight moves, so it contributes only when n == 1.
 *             The answer is the sum of f(i, n) for i in 0..9, modulo 1e9+7.
 *
 * Time      : O(10 * n * k) where k <= 3 is the max moves per digit -> O(n)
 * Space     : O(n) for the memo table (10 * n) plus O(n) recursion depth
 */


// ------------------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    const int mod=1e9+7;
    vector<vector<int>> adj={
        {4, 6},{6, 8},{7, 9},{4, 8}, {3, 9, 0},
        {}, {1, 7, 0},{2, 6}, {3, 1},{2,4}
    };
   
    vector<vector<int>> dp;
    int f(int i, int n){
        if (n==1) return 1;
        if (i==5) return 0;
        if (dp[i][n]!=-1) return dp[i][n];
        int ans=0;
        #pragma unroll
        for(int j: adj[i]){
            ans=(ans+f(j, n-1))%mod;
        }
        return dp[i][n]=ans;
    }
    int knightDialer(int n) {
        int ans=0;
        dp.assign(10, vector<int>(n+1, -1));
        #pragma unroll
        for(int i=0; i<=9; i++)
            ans=(ans+f(i, n))%mod;
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
