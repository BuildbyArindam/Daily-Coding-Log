/*
 * Problem : 1235. Maximum Profit in Job Scheduling
 * Platform: LeetCode
 * Link    : https://leetcode.com/problems/maximum-profit-in-job-scheduling/
 * Difficulty: Hard
 * Topics  : Array, Binary Search, Dynamic Programming, Sorting
 * Date    : 2026-10-08
 *
 * Approach:
 *   Sort jobs by start time. Let dp[i] = max profit using jobs[i:].
 *   For each job i, either:
 *     - skip it:   dp[i+1]
 *     - take it:   profit[i] + dp[j], where j is the first job with
 *                  startTime >= endTime[i] (found via binary search).
 *   dp[i] = max(take, skip). Memoized top-down recursion.
 *
 * Time Complexity : O(n log n)  (sort + n binary searches)
 * Space Complexity: O(n)        (jobs, dp memo, recursion stack)
 */



// ---------------------------------------------- Solution -------------------------------------------------------


struct Job {
  int startTime;
  int endTime;
  int profit;
  Job(int startTime, int endTime, int profit)
      : startTime(startTime), endTime(endTime), profit(profit) {}
};
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        const int n = startTime.size();
    // dp[i] := max profit to schedule jobs[i:]
    dp.resize(n + 1);
    vector<Job> jobs;

    for (int i = 0; i < n; ++i)
      jobs.emplace_back(startTime[i], endTime[i], profit[i]);

    sort(begin(jobs), end(jobs), [](const auto& a, const auto& b) {
      return a.startTime < b.startTime;
    });

    // Will use binary search to find the first available startTime
    for (int i = 0; i < n; ++i)
      startTime[i] = jobs[i].startTime;

    return jobScheduling(jobs, startTime, 0);
  }

 private:
  vector<int> dp;

  int jobScheduling(const vector<Job>& jobs, const vector<int>& startTime,
                    int i) {
    if (i == jobs.size())
      return 0;
    if (dp[i] > 0)
      return dp[i];

    const int j = firstGreaterEqual(startTime, i + 1, jobs[i].endTime);
    const int choose = jobs[i].profit + jobScheduling(jobs, startTime, j);
    const int skip = jobScheduling(jobs, startTime, i + 1);
    return dp[i] = max(choose, skip);
  }

  int firstGreaterEqual(const vector<int>& A, int startFrom, int target) {
    return lower_bound(begin(A) + startFrom, end(A), target) - begin(A);
    }
};
