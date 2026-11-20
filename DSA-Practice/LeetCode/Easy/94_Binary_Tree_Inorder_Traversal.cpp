/*
 * Problem : 94. Binary Tree Inorder Traversal (LeetCode)
 * Link    : https://leetcode.com/problems/binary-tree-inorder-traversal/
 * Date    : 2026-10-03
 * Difficulty : Easy
 * Topics  : Stack, Tree, Depth-First Search
 *
 * Approach:
 *   Recursive DFS. Visit the left subtree, record the current node's value,
 *   then visit the right subtree. A helper function appends values to a
 *   shared result vector passed by reference, avoiding extra copies.
 *
 * Complexity:
 *   Time  : O(n) - every node is visited exactly once.
 *   Space : O(h) - recursion stack depth, where h is the tree height
 *           (O(log n) if balanced, O(n) if skewed). The output vector is
 *           not counted.
 */


// ---------------------------------- Solution -------------------------------------------------------


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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        helper(root, result);
        return result;
    }

    void helper(TreeNode* root, vector<int>& result) {
        if (root != nullptr) {
            helper(root->left, result);
            result.push_back(root->val);
            helper(root->right, result);
        }
    }
};
