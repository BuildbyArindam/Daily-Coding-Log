/*
 * Problem:    570. Managers with at Least 5 Direct Reports
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
 * Difficulty: Medium
 * Topics:     Database
 * Date:       2026-10-05
 *
 * Approach:
 *   1. Inner query groups Employee rows by managerId and keeps only
 *      managers with COUNT(*) >= 5 (HAVING filters after aggregation).
 *   2. Outer query returns the names of employees whose id appears in
 *      that set of qualifying manager IDs.
 *
 * Time Complexity:  O(n) to scan and group, plus the IN lookup
 *                   (O(n log n) if the grouping sorts; the IN lookup is
 *                   typically a hash or index lookup)
 * Space Complexity: O(k) for the grouped manager IDs, where k is the
 *                   number of distinct managers
 */


--------------------------------------------- Solution --------------------------------------------------------


-- # Write your MySQL query statement below
SELECT e1.name
FROM Employee e1
WHERE e1.id IN (
   SELECT managerId
   FROM Employee
   GROUP BY managerId
   HAVING COUNT(*) >= 5
);
