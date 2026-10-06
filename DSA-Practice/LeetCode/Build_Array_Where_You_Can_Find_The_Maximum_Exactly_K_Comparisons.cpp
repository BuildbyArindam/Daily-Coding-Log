/*
 * Problem : 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
 * Link    : https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
 * Platform: LeetCode 
 * Difficulty: Hard
 * Topics  : Dynamic Programming, Prefix Sum
 * Date    : 2026-10-07
 *
 * Approach:
 *   dp[i][j][l] = number of arrays of length i+1 with every element <= j
 *                 and search cost exactly l (a prefix-sum over the max value).
 *   Subtracting dp[i][j-1][l] from dp[i][j][l] gives arrays whose max is exactly j.
 *
 *   Transition for arrays whose max is exactly j:
 *     - Last element is not a new max: the prefix already has max j and cost l,
 *       so the last element can be any of j values.
 *           (dp[i-1][j][l] - dp[i-1][j-1][l]) * j
 *     - Last element is a new max (= j): the prefix has max <= j-1 and cost l-1.
 *           dp[i-1][j-1][l-1]
 *   Then add dp[i][j-1][l] to make the new state cumulative.
 *   Base case: dp[0][j][1] = j.
 *   Only two layers are kept (i & 1), and l is bounded by min(i+1, j, k).
 *
 * Complexity:
 *   Time  : O(n * m * k)
 *   Space : O(m * k)
 */


// --------------------------------------- Solution ----------------------------------------------------------


class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        if(m<k)return 0;
        int dp[2][m+1][k+1],mod=1e9+7;
        memset(dp,0,sizeof(dp));
        for(int j=1;j<=m;++j)
            dp[0][j][1]=j;
        for(int i=1;i<n;++i)
            for(int j=1;j<=m;++j)
                for(int l=1;l<=min(i+1,min(j,k));++l)
                    dp[i&1][j][l]=(dp[i&1][j-1][l]+(long)(dp[(i-1)&1][j][l]-dp[(i-1)&1][j-1][l])*j+dp[(i-1)&1][j-1][l-1])%mod;
        return (dp[(n-1)&1][m][k]+mod)%mod;
    }
};
