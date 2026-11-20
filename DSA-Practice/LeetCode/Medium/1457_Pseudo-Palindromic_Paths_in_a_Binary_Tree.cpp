/**
 * Problem: 1457. Pseudo-Palindromic Paths in a Binary Tree
 * Link:    https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
 * Date:    2026-10-05
 * Difficulty: Medium
 * Topics:  Bit Manipulation, Tree, DFS, BFS, Binary Tree
 *
 * Approach:
 *   DFS from root to every leaf, carrying a 10-bit mask where bit d is
 *   toggled (XOR) each time digit d appears on the path. A root-to-leaf
 *   path can be rearranged into a palindrome iff at most one digit has an
 *   odd count, i.e. the mask has at most one set bit. That is checked with
 *   (mask & (mask - 1)) == 0.
 *
 * Time Complexity:  O(n), each node is visited once.
 * Space Complexity: O(h), recursion stack, where h is the tree height
 *                   (O(n) worst case for a skewed tree, O(log n) if balanced).
 */


// -------------------------------------------- Solution ------------------------------------------------------


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        int ans = 0;
    dfs(root, 0, ans);
    return ans;
  }

 private:
  void dfs(TreeNode* root, int path, int& ans) {
    if (!root)
      return;
    if (!root->left && !root->right) {
      path ^= 1 << root->val;
      if ((path & (path - 1)) == 0)
        ++ans;
      return;
    }

    dfs(root->left, path ^ 1 << root->val, ans);
    dfs(root->right, path ^ 1 << root->val, ans);
    }
};
