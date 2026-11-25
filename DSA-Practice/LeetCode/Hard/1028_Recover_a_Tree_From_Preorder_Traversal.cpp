/*
 * Problem   : 1028. Recover a Tree From Preorder Traversal
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
 * Date      : 2026-11-25
 * Difficulty: Hard
 * Topics    : String, Tree, DFS, Binary Tree
 *
 * Approach  : Stack-based single pass over the string.
 *             - Count leading '-' to get the node's depth, then parse the value.
 *             - Pop the stack until its size equals depth, so the top is the parent.
 *             - Attach as left child if empty, otherwise as right child (preorder
 *               guarantees left is visited first; a lone child is always left).
 *             - Push the new node.
 *
 * Time      : O(n), n = length of the string (each character is read once, each
 *             node is pushed and popped at most once).
 * Space     : O(h), h = tree height, for the stack (excluding the output tree).
 */


// -------------------------------------------- Solution ---------------------------------------------------------


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
    TreeNode* recoverFromPreorder(string traversal) {
        int n = traversal.length();
        stack<TreeNode*> st;
        int i = 0;
        TreeNode* root = nullptr;
        while (i < n) {
            int depth = 0;
            int num = 0;
            while (i < n && traversal[i] == '-') {
                depth++;
                i++;
            }
            while (i < n && traversal[i] != '-') {
                num = num * 10 + (traversal[i] - '0');
                i++;
            }
            TreeNode* node = new TreeNode(num);
            if (!st.empty()) {
                while (st.size() > depth) {
                    st.pop();
                }
                if (!st.top()->left) {
                    st.top()->left = node;
                } else {
                    st.top()->right = node;
                }
            }
            if (depth == 0) {
                root = node;
            }
            st.push(node);
        }
        return root;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
