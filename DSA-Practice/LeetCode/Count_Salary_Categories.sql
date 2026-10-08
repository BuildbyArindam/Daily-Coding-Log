/*
 * Problem   : 1907. Count Salary Categories
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/count-salary-categories/
 * Difficulty: Medium
 * Topics    : Database
 * Date      : 2026-10-08
 *
 * Approach  : Run three separate aggregate queries, one per salary bracket
 *             (Low < 20000, Average 20000-50000 inclusive, High > 50000),
 *             and combine them with UNION ALL. Each query uses
 *             SUM(IF(condition, 1, 0)) as a conditional count. This ensures
 *             every category appears in the output, even when its count is 0
 *             (a GROUP BY approach would drop empty categories).
 *
 * Time      : O(3n) -> O(n), one table scan per category
 * Space     : O(1), only three result rows
 */


--------------------------------------------- Solution ------------------------------------------------------


-- # Write your MySQL query statement below
select "Low Salary" as category,sum(if(income<20000,1,0)) as accounts_count from accounts 
UNION ALL
select "Average Salary" as category,sum(if(income>=20000 and income<=50000,1,0)) as accounts_count from accounts 
UNION ALL
select "High Salary" as category,sum(if(income>50000,1,0)) as accounts_count from accounts 
