-- ============================================================
-- Problem   : Employees Whose Manager Left the Company
-- Platform  : LeetCode
-- Link      : https://leetcode.com/quest/database-quest/quiz/employees-whose-manager-left-the-company/
-- Date      : 2026-08-23
-- Difficulty: Easy
-- Topic     : SQL Schema, Pandas Schema
--
-- Approach  : Select employees earning below 30000 whose manager_id
--             is not NULL, then filter out any manager_id that still
--             exists as a valid employee_id (i.e., the manager left).
--             A NOT IN subquery against Employees.employee_id isolates
--             "orphaned" manager references. Result ordered by employee_id.
--
-- Time      : O(n) for the outer scan + O(n) for building the subquery
--             set → effectively O(n) with proper indexing on employee_id.
-- Space     : O(n) for the subquery result set materialized for NOT IN.
-- ============================================================


----------------------------- Solution ---------------------------------

SELECT employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id IS NOT NULL
  AND manager_id NOT IN (
      SELECT employee_id
      FROM Employees
  )
ORDER BY employee_id;
