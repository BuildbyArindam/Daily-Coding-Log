/*
 * Problem   : 2536. Number of Unique Subjects Taught by Each Teacher
 * Platform  : LeetCode  
 * Difficulty: Easy
 * Topic     : Database
 * Link      : https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
 * Date      : 2026-10-08
 *
 * Approach  : Group rows by teacher_id and count DISTINCT subject_id, since
 *             a teacher may teach the same subject in several departments.
 *
 * Time      : O(n) to scan and group (O(n log n) if the engine sorts to group)
 * Space     : O(k) where k = number of distinct teachers (plus distinct
 *             subject tracking per group)
 */


------------------------------------------- Solution ---------------------------------------------------


-- # Write your MySQL query statement below
SELECT teacher_id, COUNT(distinct subject_id) AS cnt FROM Teacher 
GROUP BY teacher_id;
