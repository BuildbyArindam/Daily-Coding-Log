/*
 * Problem   : 1337. The K Weakest Rows in a Matrix
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
 * Difficulty: Easy
 * Topics    : Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
 * Date      : 07-Oct-2026
 *
 * Approach:
 *   For each row, count the soldiers (1s) and push {count, rowIndex} into a
 *   min-heap. Pairs compare by count first, then by row index, so ties are
 *   resolved in favour of the smaller index. Pop the top k entries and
 *   collect their row indices.
 *
 * Complexity:
 *   Time : O(m * n + m log m)  -> counting every cell + heap push/pop for m rows
 *   Space: O(m)                -> heap holds one pair per row
 *   (m = rows, n = columns)
 */


// --------------------------------------------- Solution ------------------------------------------------------------


class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<int>ans;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>pq;

        for(int i = 0; i<mat.size(); i++)
        {
            pair<int, int>p = {0, 0};
            for(int j = 0; j<mat[0].size(); j++)
            {
                if(mat[i][j] == 1)
                {
                    p.first++;
                }
                   p.second = i;
            }
            pq.push(p);
        }
        while(pq.size() && k>0)
        {
            ans.push_back(pq.top().second);
            pq.pop();
            k--;
        }
        return ans;
    }
};
