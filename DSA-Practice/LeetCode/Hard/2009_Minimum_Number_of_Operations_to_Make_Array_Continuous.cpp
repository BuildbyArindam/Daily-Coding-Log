/*
 * Problem   : 2009. Minimum Number of Operations to Make Array Continuous
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
 * Date      : 07-Oct-2026
 * Difficulty: Hard
 * Topics    : Array, Hash Table, Binary Search, Sliding Window
 *
 * Approach  :
 *   An array is continuous if all elements are unique and max - min == n - 1.
 *   1. Sort and remove duplicates (duplicates must always be changed).
 *   2. Treat each unique value nums[i] as the window minimum. The window
 *      is [nums[i], nums[i] + n - 1].
 *   3. Binary search (upper_bound) for the end of the window. Unique values
 *      inside it are kept; all others are changed.
 *   4. Operations = n - (number of unique values in window) = n - (j - i).
 *   5. Answer is the minimum over all i.
 *
 * Time      : O(n log n)  (sort + n binary searches)
 * Space     : O(1) extra  (in-place sort/unique)
 */


// ------------------------------------------------ Solution ------------------------------------------------------------


class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n=nums.size();
        int ans=n-1;
        sort(nums.begin(), nums.end());
        auto it=unique(nums.begin(), nums.end());
        nums.erase(it, nums.end());//erase the repetive elements
        int m=nums.size(), k=n-m;
    //    cout<<"n="<<n<<" , m="<<m<<", k="<<k<<endl;
        #pragma unroll
        for(int i=0; i<m; i++){
            int l=nums[i], r=l+n-1;
            int j=upper_bound(nums.begin()+i, nums.end(), r)-nums.begin();
            ans=min(ans, n-j+i);
        }
        
        return ans;
    }
};
