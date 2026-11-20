/*
 * Problem:    1527. Patients With a Condition
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/patients-with-a-condition/
 * Difficulty: Easy
 * Topics:     Database
 * Date:       2026-10-08
 *
 * Approach:
 *   `conditions` is a space-separated list of codes. A code starts with
 *   'DIAB1' only if it is either the first token (LIKE 'DIAB1%') or follows
 *   a space (LIKE '% DIAB1%'). Matching ' DIAB1' with the leading space
 *   avoids false positives such as 'ADIAB1xx' where DIAB1 appears mid-token.
 *
 * Time Complexity:  O(N * L), N = rows, L = length of `conditions`
 *                   (full table scan, pattern match per row)
 * Space Complexity: O(1) extra (O(K) for the K rows returned)
 */


--------------------------------------- Solution --------------------------------------------


-- # Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%' 
ORDER BY patient_id;
