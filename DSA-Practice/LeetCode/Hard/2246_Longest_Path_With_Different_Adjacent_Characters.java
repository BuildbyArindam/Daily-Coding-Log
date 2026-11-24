/**
 * Problem   : 2246. Longest Path With Different Adjacent Characters
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
 * Date      : 2026-11-24
 * Difficulty: Hard
 * Topics    : Tree, DFS, Graph, Topological Sort, String
 *
 * Approach  : Build a children adjacency map from the parent array, then run a
 *             post-order DFS. For each node, track the two longest downward
 *             chains among children whose character differs from the node's.
 *             The best path through that node is longest + secondLongest + 1,
 *             which updates the global answer. The node returns longest + 1 to
 *             its parent as its own best downward chain.
 *
 * Time      : O(n), each node and edge is visited once.
 * Space     : O(n), for the children map plus recursion stack (O(h), up to O(n) on a skewed tree).
 */


// ----------------------------------------- Solution -----------------------------------------------------------


class Solution {
    private int longestPath = 1;

    public int dfs(int currentNode, Map<Integer, List<Integer>> children, String s) {
        if (!children.containsKey(currentNode)) {
            return 1;
        }
        int longestChain = 0, secondLongestChain = 0;
        for (int child : children.get(currentNode)) {
            int longestChainStartingFromChild = dfs(child, children, s);
            if (s.charAt(currentNode) == s.charAt(child)) {
                continue;
            }
            if (longestChainStartingFromChild > longestChain) {
                secondLongestChain = longestChain;
                longestChain = longestChainStartingFromChild;
            } else if (longestChainStartingFromChild > secondLongestChain) {
                secondLongestChain = longestChainStartingFromChild;
            }
        }
        longestPath = Math.max(longestPath, longestChain + secondLongestChain + 1);
        return longestChain + 1;
    }

    public int longestPath(int[] parent, String s) {
        int n = parent.length;
        Map<Integer, List<Integer>> children = new HashMap<>();
        for (int i = 1; i < n; i++) {
            children.computeIfAbsent(parent[i], value -> new ArrayList<Integer>()).add(i);
        }
        dfs(0, children, s);
        return longestPath;
    }
}
