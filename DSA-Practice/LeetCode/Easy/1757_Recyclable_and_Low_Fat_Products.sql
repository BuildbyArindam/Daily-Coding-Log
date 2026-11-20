/*
 * Problem:    1757. Recyclable and Low Fat Products
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/recyclable-and-low-fat-products/
 * Difficulty: Easy
 * Topics:     Database
 * Date:       2026-10-04
 *
 * Approach:
 *   Filter the products table with a WHERE clause that keeps only rows
 *   where both low_fats = 'Y' and recyclable = 'Y', then select product_id.
 *
 * Time Complexity:  O(n) - a single scan over the products table
 * Space Complexity: O(1) - no extra storage beyond the result set
 */


----------------------------------------- Solution --------------------------------------------------


-- # Write your MySQL query statement below
SELECT product_id
FROM products
WHERE low_fats = 'Y' AND recyclable = 'Y';
