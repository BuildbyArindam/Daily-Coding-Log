/*
 * Problem   : 341. Flatten Nested List Iterator
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/flatten-nested-list-iterator/
 * Date      : 2026-10-07
 * Difficulty: Medium
 * Topics    : Stack, Tree, DFS, Design, Queue, Iterator
 *
 * Approach  : Eager flattening. In the constructor, run a recursive DFS over
 *             the nested list and store every integer, in order, in a vector.
 *             Then next() returns v[index++] and hasNext() checks index < size.
 *
 * Complexity:
 *   Constructor : O(N) time, where N = total number of integers and lists
 *   next()      : O(1)
 *   hasNext()   : O(1)
 *   Space       : O(M + D), where M = number of integers stored and
 *                 D = max nesting depth (recursion stack)
 *
 * Trade-off : Simple, but it flattens everything upfront. A stack-based lazy
 *             iterator uses less extra memory if the list is huge.
 */


// ----------------------------------------- Solution -------------------------------------------------------


/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    vector<int> v;
    int index;

    void Recursion(vector<NestedInteger>& nums) {
        int i=0;
        while(i<nums.size()){
            if(nums[i].isInteger()){
                v.push_back(nums[i].getInteger());
            }
            else{
                Recursion(nums[i].getList());
            }
            i++;
        }
    }
    NestedIterator(vector<NestedInteger> &nestedList) {
        index=0;
        Recursion(nestedList);
    }
    
    int next() {
        if(hasNext()){
            return v[index++];
        }
        return -1;
    }
    
    bool hasNext() {
        if(index<v.size()){
            return true;
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
