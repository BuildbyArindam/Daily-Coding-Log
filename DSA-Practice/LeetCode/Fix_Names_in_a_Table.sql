/*
 * Problem : 1667. Fix Names in a Table
 * Platform: LeetCode 
 * Difficulty: Easy
 * Topic   : Database
 * Link    : https://leetcode.com/problems/fix-names-in-a-table/
 * Date    : 2026-10-08
 *
 * Approach:
 *   Capitalize only the first character and lowercase the rest.
 *   - UPPER(SUBSTR(name, 1, 1))  -> first letter in uppercase
 *   - LOWER(SUBSTR(name, 2))     -> remaining letters in lowercase
 *   - CONCAT joins the two parts; ORDER BY user_id gives the required order.
 *
 * Time Complexity : O(n log n) for n rows, dominated by the ORDER BY
 *                   (O(n) if user_id is the primary key and the index is used);
 *                   the string operations are O(L) per row, L = name length.
 * Space Complexity: O(n) for the result set / sort buffer.
 */


------------------------------------------ Solution --------------------------------------------------------


-- # Write your MySQL query statement below
SELECT user_id,CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(name,2,length(name)))) AS name
FROM Users ORDER BY user_id;
# SUBSTR(string_name , start_index ,end_index)
