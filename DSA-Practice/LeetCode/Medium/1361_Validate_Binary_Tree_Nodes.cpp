/*
 * Problem: 1361. Validate Binary Tree Nodes
 * Link:    https://leetcode.com/problems/validate-binary-tree-nodes/
 * Platform: LeetCode 
 * Difficulty: Medium
 * Topics:  Tree, DFS, BFS, Union-Find, Graph Theory, Binary Tree
 * Date:    2026-10-07
 *
 * Approach:
 *   1. Find the root: the only node that never appears as anyone's child.
 *      If no such node exists, the graph has a cycle or no root, so return false.
 *   2. Run an iterative DFS from the root, marking nodes as seen.
 *      Reaching an already-seen node means it has two parents or there is
 *      a cycle, so return false.
 *   3. After traversal, the structure is a valid tree only if every node
 *      was visited (seen.size() == n). This catches disconnected components
 *      and multiple roots.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)  (child set + seen set + stack)
 */


// -------------------------------------------- Solution --------------------------------------------------------


class Solution {
public:
    int findRoot(int n, vector<int>& left, vector<int>& right) {
        unordered_set<int> children;
        for(int i = 0; i < left.size(); i++) {
            children.insert(left[i]);
        }
        for(int i = 0; i < right.size(); i++) {
            children.insert(right[i]);
        }
        for(int i = 0; i < n; i++) {
            if(children.find(i) == children.end()) {
                return i;
            }
        }
        return -1;
    }
    
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        int root = findRoot(n, leftChild, rightChild);
        if(root == -1) {
            return false;
        }
        unordered_set<int> seen;
        stack<int> st;
        seen.insert(root);
        st.push(root);
        while(!st.empty()) {
            int node = st.top();
            st.pop();
            int children[] = {leftChild[node], rightChild[node]};
            for(int i : children) {
                if(i != -1) {
                    if(seen.find(i) != seen.end()) {
                        return false;
                    }
                    st.push(i);
                    seen.insert(i);
                }
            }
        }
        return seen.size() == n;
    }
};
