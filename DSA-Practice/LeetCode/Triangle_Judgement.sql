/*
 * Problem:    610. Triangle Judgement
 * Platform:   LeetCode 
 * Link:       https://leetcode.com/problems/triangle-judgement/
 * Date:       2026-10-08
 * Difficulty: Easy
 * Topic:      Database
 *
 * Approach:   Three lengths x, y, z form a triangle only if the sum of any
 *             two sides is strictly greater than the third. Check all three
 *             inequalities in a single IF() per row and label the result
 *             "Yes" or "No".
 *
 * Time:       O(n) - one pass over the Triangle table, constant work per row
 * Space:      O(1) - no extra structures beyond the output rows
 */


--------------------------------------- Solution ------------------------------------------------


-- # Write your MySQL query statement below
SELECT *, IF(x+z>y AND x+y>z AND z+y>x, "Yes", "No") AS triangle
FROM Triangle
