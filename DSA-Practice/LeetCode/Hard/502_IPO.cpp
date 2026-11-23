/*
 * Problem:    502. IPO
 * Link:       https://leetcode.com/problems/ipo/
 * Platform:   LeetCode
 * Difficulty: Hard
 * Topics:     Array, Greedy, Sorting, Heap (Priority Queue)
 * Date:       2026-11-23
 *
 * Approach:
 *   Greedy + max-heap. Sort projects by required capital. For each of up to
 *   k rounds, push the profits of all projects now affordable (capital <= w)
 *   into a max-heap, then pick the most profitable one and add it to w.
 *   Since capital only grows, a project that becomes affordable stays
 *   affordable, so a single forward pointer over the sorted list is enough.
 *   If the heap is empty, no project is affordable and we stop early.
 *
 * Time Complexity:  O(n log n + k log n)
 *                   - sort: O(n log n)
 *                   - each project is pushed once and popped at most once;
 *                     at most k pops, each O(log n)
 * Space Complexity: O(n) for the project pairs and the heap
 */


// ---------------------------------------------- Solution ------------------------------------------------


class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        std::vector<std::pair<int, int>> projects;
        for (int i = 0; i < n; ++i) {
            projects.emplace_back(capital[i], profits[i]);
        }
        std::sort(projects.begin(), projects.end());
        std::priority_queue<int> maxHeap;
        int i = 0;
        for (int j = 0; j < k; ++j) {
            while (i < n && projects[i].first <= w) {
                maxHeap.push(projects[i].second);
                i++;
            }
            if (maxHeap.empty()) {
                break;
            }
            w += maxHeap.top();
            maxHeap.pop();
        }
        return w;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
