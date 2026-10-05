/*
 * Problem:    1661. Average Time of Process per Machine
 * Link:       https://leetcode.com/problems/average-time-of-process-per-machine/
 * Platform:   LeetCode
 * Difficulty: Easy
 * Topics:     Database, Self Join, Aggregation
 * Date:       2026-10-05
 *
 * Approach:
 *   Self-join Activity on (machine_id, process_id), pairing each 'start' row (a1)
 *   with its matching 'end' row (a2). The process duration is
 *   a2.timestamp - a1.timestamp. Group by machine_id and take the average,
 *   rounded to 3 decimal places.
 *
 * Complexity (engine-dependent, assuming no index / hash join):
 *   Time:  O(N) with a hash join on (machine_id, process_id); O(N^2) worst case
 *          with a nested-loop join and no index.
 *   Space: O(N) for the join and grouping intermediates.
 */


-------------------------------------- Solution --------------------------------------------------


-- # Write your MySQL query statement below
select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time 
from Activity a1
join Activity a2 
on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id
