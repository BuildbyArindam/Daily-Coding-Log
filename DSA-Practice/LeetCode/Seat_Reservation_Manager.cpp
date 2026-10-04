/*
 * Problem   : 1845. Seat Reservation Manager
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/seat-reservation-manager/
 * Difficulty: Medium
 * Topics    : Design, Heap (Priority Queue)
 * Date      : 2026-10-04
 *
 * Approach:
 *   Seats are always handed out lowest-first. Keep a counter `c` for the
 *   highest seat ever given out, plus a min-heap of seats that were
 *   unreserved. On reserve(), if the heap has a returned seat, pop the
 *   smallest one (it is always <= c, so it beats any fresh seat).
 *   Otherwise hand out the next fresh seat, c + 1. On unreserve(), push
 *   the seat back into the heap. This avoids pre-filling the heap with
 *   all n seats.
 *
 * Complexity:
 *   Time : reserve() O(log k), unreserve() O(log k), constructor O(1),
 *          where k = number of currently unreserved seats below c
 *   Space: O(k)
 */


// ------------------------------------------- Solution -----------------------------------------------------------


class SeatManager {
public:
    priority_queue<int, vector<int>, greater<int>>pq;
    int c = 0;
    SeatManager(int n) {
    }
    int reserve() {
        if (pq.size() && pq.top() <= c) {
            int t = pq.top();
            pq.pop();
            return t;
        }
        c++;
        return c;
    }
    
    void unreserve(int seatNumber) {
        pq.push(seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
