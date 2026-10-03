/*
 * Problem   : 2385. Amount of Time for Binary Tree to Be Infected
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
 * Date      : 2026-10-03
 * Difficulty: Medium
 * Topics    : Hash Table, Tree, DFS, BFS, Binary Tree
 *
 * Approach  :
 *   A tree only lets you move downward, but the infection spreads in all
 *   directions, so I convert the tree into an undirected graph (adjacency
 *   map) with a DFS that links each node to its parent and children.
 *   Then I run a level-order BFS from the `start` node, tracking visited
 *   nodes. Each BFS level is one minute, so the answer is the number of
 *   levels minus 1 (the starting level takes no time).
 *
 * Time      : O(n) - one DFS to build the graph + one BFS over all nodes
 * Space     : O(n) - adjacency map, visited set, queue, recursion stack
 */


// ---------------------------------------- Solution ---------------------------------------------------------


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
    int amountOfTime(TreeNode* root, int start) {
        unordered_map<int, unordered_set<int>> map;
        convert(root, 0, map);
        queue<int> q;
        q.push(start);
        int minute = 0;
        unordered_set<int> visited;
        visited.insert(start);
        while (!q.empty()) {
            int levelSize = q.size();
            while (levelSize > 0) {
                int current = q.front();
                q.pop();

                for (int num : map[current]) {
                    if (visited.find(num) == visited.end()) {
                        visited.insert(num);
                        q.push(num);
                    }
                }
                levelSize--;
            }
            minute++;
        }
        return minute - 1;
    }

    void convert(TreeNode* current, int parent, unordered_map<int, unordered_set<int>>& map) {
        if (current == nullptr) {
            return;
        } 
        if (map.find(current->val) == map.end()) {
            map[current->val] = unordered_set<int>();
        }
        unordered_set<int>& adjacentList = map[current->val];
        if (parent != 0) {
            adjacentList.insert(parent);
        } 
        if (current->left != nullptr) {
            adjacentList.insert(current->left->val);
        } 
        if (current->right != nullptr) {
            adjacentList.insert(current->right->val);
        }
        convert(current->left, current->val, map);
        convert(current->right, current->val, map);
    }
};
