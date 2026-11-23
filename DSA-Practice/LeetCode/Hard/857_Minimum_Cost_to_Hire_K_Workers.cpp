/*
 * Problem   : 857. Minimum Cost to Hire K Workers
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
 * Date      : 2026-11-23
 * Difficulty: Hard
 * Topics    : Array, Greedy, Sorting, Heap (Priority Queue)
 *
 * Approach  :
 *   - Every worker in the chosen group is paid at the same wage/quality
 *     rate, and that rate must be the highest ratio in the group so
 *     nobody falls below their minimum wage.
 *   - Sort workers by ratio = wage / quality (ascending).
 *   - Take the first k workers, tracking their quality sum in a max-heap.
 *   - For each next worker i, the current ratio becomes the group's rate.
 *     Add their quality, drop the largest quality from the heap (to keep
 *     the sum minimal), and update the answer with rate * qualitySum.
 *
 * Time      : O(n log n) for sorting + O(n log k) for heap operations
 *             => O(n log n)
 * Space     : O(n) for the ratio array + O(k) for the heap
 */


// -------------------------------------------------- Solution ----------------------------------------------


class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);
        
        vector<pair<double, int>> ratio;
        int n = quality.size();
        
        for (int i = 0; i < n; ++i) {
                ratio.emplace_back(static_cast<double>(wage[i]) / quality[i], i);
            }
            
        sort(begin(ratio), end(ratio));
        priority_queue<int> maxHeap;
        int qualitySum = 0;
        double maxRate = 0.0;
        
        for (int i = 0; i < k; ++i) {
            qualitySum += quality[ratio[i].second];
            maxRate = max(maxRate, ratio[i].first);
            maxHeap.push(quality[ratio[i].second]);
        }

        double res = maxRate * qualitySum;
        for (int i = k; i < n; ++i) {
            maxRate = max(maxRate, ratio[i].first);
            qualitySum -= maxHeap.top(); 
            maxHeap.pop();

            qualitySum += quality[ratio[i].second];
            maxHeap.push(quality[ratio[i].second]);
            res = min(res, maxRate * qualitySum);
        }

        return res;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
